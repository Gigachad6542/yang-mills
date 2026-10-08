"""T54: checkpointed driver for the 4D SU(2) universality runs of t51.

Same Monte Carlo as t51_mc_universality_4d.run (heat bath + overrelaxation,
cold start, 150 thermalization updates, 200 measurements every 2 updates,
Balaban's average iterated N times to the terminal lattice), with two
additions:

- the terminal 2x2 Wilson loop W22 is measured next to P and W12;
- the state (configuration, random-generator state, counters, data) is saved
  to a checkpoint every `--every-ckpt` updates and the run resumes from it,
  so a long 32^4 run survives a killed process.

Usage: python3 t54_mc_checkpointed.py SEED D N n0 beta TAG
Writes t54_state_TAG.npz while running and appends the final line to
t54_TAG.out (format of t51 plus W22).
"""
import json
import os
import sys
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t51_mc_universality_4d as m  # noqa: E402

qmul, qinv = m.qmul, m.qinv


def loop_rect(V, R, T):
    """Mean of (1/2) tr of the R x T Wilson loop, over both orientations of
    each plane (mu != nu, R steps along mu, T along nu)."""
    D = V.shape[0]
    tot, cnt = 0.0, 0
    for mu in range(D):
        for nu in range(D):
            if mu == nu:
                continue
            steps = [(mu, 1)] * R + [(nu, 1)] * T + [(mu, -1)] * R + [(nu, -1)] * T
            tot += m.path_product(V, steps)[..., 0].mean(); cnt += 1
    return tot / cnt


def save(path, **kw):
    tmp = path + ".tmp.npz"
    np.savez(tmp, **kw)
    os.replace(tmp, path)


def main():
    seed, D, N, n0, beta, tag = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),
                                 int(sys.argv[4]), float(sys.argv[5]), sys.argv[6])
    every_ckpt = int(os.environ.get("T54_CKPT_EVERY", "10"))
    L, ntherm, nmeas, every = 2, 150, 200, 2
    rng = np.random.default_rng(seed)
    m.rng = rng
    m.q.rng = rng
    n = n0 * L ** N
    masks = m.parity_mask(D, n)
    ck = f"t54_state_{tag}.npz"
    if os.path.exists(ck):
        z = np.load(ck)
        U = z["U"].copy()
        rng.bit_generator.state = json.loads(str(z["rng"]))
        done = int(z["done"])
        data = [tuple(r) for r in z["data"]]
        elapsed = float(z["elapsed"])
        print(f"resumed {tag} at update {done}, {len(data)} measurements", flush=True)
    else:
        U = m.cold(D, n)
        done, data, elapsed = 0, [], 0.0
    total = ntherm + nmeas * every
    t0 = time.time()
    while done < total:
        m.heatbath(U, beta, masks)
        m.overrelax(U, masks)
        done += 1
        if done > ntherm and (done - ntherm) % every == 0:
            V = U
            for _ in range(N):
                V = m.average(V, L)
            data.append((m.plaq(V), m.w12(V), loop_rect(V, 2, 2), m.plaq(U)))
        if done % every_ckpt == 0 or done == total:
            save(ck, U=U, rng=np.array(json.dumps(rng.bit_generator.state)), done=done,
                 data=np.array(data).reshape(-1, 4), elapsed=elapsed + time.time() - t0)
    data = np.array(data)
    nb = 10
    bl = data[: (len(data) // nb) * nb].reshape(nb, -1, 4).mean(axis=1)
    mean, err = bl.mean(0), bl.std(0, ddof=1) / np.sqrt(nb)
    line = (f"D={D} N={N} n={n} beta={beta:.4f}: P={mean[0]:.5f}({err[0]:.5f}) "
            f"W12={mean[1]:.5f}({err[1]:.5f}) W22={mean[2]:.5f}({err[2]:.5f}) "
            f"fine plaq={mean[3]:.5f} [{elapsed + time.time() - t0:.0f}s] seed={seed}")
    print(line, flush=True)
    with open(f"t54_{tag}.out", "a") as f:
        f.write(line + "\n")
    np.save(f"t54_{tag}_data.npy", data)


if __name__ == "__main__":
    main()
