#!/bin/sh
# Re-download the open-access primary sources cited by this project.
# Usage: sh sources/fetch_papers.sh   (run from the repository root)
# Balaban's CMP papers and Magnen-Rivasseau-Seneor are free on Project Euclid;
# the Dimock, Luscher, Luscher-Weisz and Ramos-Sint papers are on arXiv.
set -u
OUT="$(dirname "$0")/papers"
mkdir -p "$OUT"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
PE="https://projecteuclid.org/accountAjax/Download?downloadType=journal%20article&isResultClick=True&urlId=cmp%2F"
fetch() { # name url
  if [ -s "$OUT/$1" ] && file "$OUT/$1" | grep -q PDF; then echo "have $1"; return; fi
  curl -sSL -A "$UA" -o "$OUT/$1" "$2"
  if file "$OUT/$1" | grep -q PDF; then echo "ok   $1"; else echo "FAIL $1"; rm -f "$OUT/$1"; fi
  sleep 60
}
fetch Balaban1984-CMP95-propagators-I.pdf            "${PE}1103941451"
fetch Balaban1984-CMP96-propagators-II.pdf           "${PE}1103941783"
fetch Balaban1985-CMP98-averaging-operations.pdf     "${PE}1103942283"
fetch Balaban1985-CMP99-regular-configurations.pdf   "${PE}1103942611"
fetch Balaban1985-CMP99-background-propagators.pdf   "${PE}1103942769"
fetch Balaban1985-CMP102-UV-stability-3D.pdf         "${PE}1104114382"
fetch Balaban1985-CMP102-variational-problem.pdf     "${PE}1104114383"
fetch Balaban1987-CMP109-RG-I.pdf                    "${PE}1104116842"
fetch Balaban1988-CMP116-RG-II-cluster.pdf           "${PE}1104161193"
fetch Balaban1988-CMP119-convergent-expansions.pdf   "${PE}1104162401"
fetch Balaban1989-CMP122-large-field-I.pdf           "${PE}1104178393"
fetch Balaban1989-CMP122-large-field-II.pdf          "${PE}1104178467"
fetch MagnenRivasseauSeneor1993-CMP155-YM4-IR-cutoff.pdf "${PE}1104253284"
fetch Dimock-Balaban-RG-I-small-fields-1108.1335.pdf  "https://arxiv.org/pdf/1108.1335"
fetch Dimock-Balaban-RG-II-large-fields-1212.5562.pdf "https://arxiv.org/pdf/1212.5562"
fetch Dimock-Balaban-RG-III-convergence-1304.0705.pdf "https://arxiv.org/pdf/1304.0705"
fetch Dimock-QED3-1512.04373.pdf                      "https://arxiv.org/pdf/1512.04373"
fetch Dimock-QED3-overview-2204.07201.pdf             "https://arxiv.org/pdf/2204.07201"
fetch Luscher2010-Wilson-flow-1006.4518.pdf           "https://arxiv.org/pdf/1006.4518"
fetch LuscherWeisz2011-gradient-flow-1101.0963.pdf    "https://arxiv.org/pdf/1101.0963"
fetch RamosSint2016-gradient-flow-1508.05552.pdf      "https://arxiv.org/pdf/1508.05552"
fetch JaffeWitten-Clay-problem.pdf                    "https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf"
