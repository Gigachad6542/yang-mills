#!/bin/sh
# Sequential N = 0, 1, 2 runs for T54 (resumable: each run checkpoints).
cd "$(dirname "$0")"
run() { [ -s "t54_$1.out" ] || python3 -u t54_mc_checkpointed.py "$2" "$3" "$4" "$5" "$6" "$1"; }
for b in 2.40 2.50 2.60; do t=$(echo $b | tr -d .); run n0_b$t 540$t 4 0 4 $b; done
for b in 2.60 2.70 2.80 2.90; do t=$(echo $b | tr -d .); run n1_b$t 541$t 4 1 4 $b; done
for b in 2.85 3.00 3.15 3.30; do t=$(echo $b | tr -d .); run n2_b$t 542$t 4 2 4 $b; done
