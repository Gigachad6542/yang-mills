#!/bin/sh
# T73: reproduce the table of research/50 sec 2.6.6 (about 1 hour on 3 cores).
# usage: sh t73_run_all.sh OUTDIR
OUT=${1:-.}
cd "$(dirname "$0")" || exit 1
( for L in 2 3 4 6; do python3 t73_scalar_loop.py $L 8 3 0.05; done ) > "$OUT/t73_scalar_loop_NM3.out" 2>&1 &
( for L in 2 3 4 6 8; do python3 t73_scalar_loop.py $L 8 2 0.05; done ) > "$OUT/t73_scalar_loop_NM2.out" 2>&1 &
( python3 t73_scalar_loop.py 12 6 2 0.05; python3 t73_scalar_loop.py 8 8 3 0.05 ) > "$OUT/t73_scalar_loop_big.out" 2>&1 &
wait
