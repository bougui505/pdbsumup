#!/usr/bin/env sh
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-05-29 23:23:44 (UTC+0200)

cat << EOF
# pdbsumup

\`\`\`
EOF

./pdbsumup.py -h

cat << EOF
\`\`\`
Example output:
\`\`\`
EOF

./pdbsumup.py --pdb data/4ci0.pdb

cat << EOF
\`\`\`
EOF
