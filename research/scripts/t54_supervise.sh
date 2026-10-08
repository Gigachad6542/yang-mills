#!/bin/sh
# T54: start or resume every run that has not finished (idempotent).
# Each job: TAG SEED D N n0 beta. A finished job has a line in t54_TAG.out.
cd "$(dirname "$0")"
start() { # tag seed D N n0 beta
  if [ -s "t54_$1.out" ]; then echo "done    $1"; return; fi
  if pgrep -f "t54_mc_checkpointed.py $2 $3 $4 $5 $6 $1" > /dev/null; then echo "running $1"; return; fi
  setsid nohup nice -n 10 python3 -u t54_mc_checkpointed.py "$2" "$3" "$4" "$5" "$6" "$1" \
    >> "t54_$1.log" 2>&1 < /dev/null &
  echo "started $1"
}
# N = 3 (32^4): the new depth, betas bracketing the matching point P = 0.64.
start n3_b330 54330 4 3 4 3.30
start n3_b340 54340 4 3 4 3.40
start n3_b350 54350 4 3 4 3.50
# N = 0, 1, 2 with the 2x2 loop added (fresh seeds; the betas of note 56), run as
# one chain so that at most four cores are busy.
if [ -s t54_n2_b330.out ]; then echo "done    chain"
elif pgrep -f "sh t54_chain.sh" > /dev/null; then echo "running chain"
else
  setsid nohup nice -n 10 sh t54_chain.sh >> t54_chain.log 2>&1 < /dev/null &
  echo "started chain"
fi
