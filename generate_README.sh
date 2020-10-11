#!/usr/bin/env zsh
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-05-29 23:23:44 (UTC+0200)

func runcmd () {
    OUTPUT=$(eval $1)
    echo "\`\`\`"
    echo "$ $1\n"
    echo "$OUTPUT"
    echo "\`\`\`"
}

cat << EOF
# pdbsumup
EOF

runcmd "./pdbsumup.py -h"
runcmd "./pdbsumup.py --pdb data/4ci0.pdb"
runcmd "./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A+B'"
runcmd "./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A' -s"
runcmd "./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A' -r"
runcmd "./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A' -sr"
runcmd "./pdbsumup.py --pdb data/5lcw.pdb --select 'chain E+F+H+G+W' --sym"
