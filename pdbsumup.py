#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-05-29 14:37:24 (UTC+0200)

import sys
import numpy
from pymol import cmd

PDBFILENAME = sys.argv[1]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ruler(char='-', length=32):
    print(char * length)


cmd.load(PDBFILENAME, 'inpdb')
chains = cmd.get_chains('inpdb')
seqs = []
nres_per_chain = []
natoms_per_chain = []
for chain in chains:
    ruler()
    seq = cmd.get_fastastr(f'inpdb and chain {chain}')
    seqs.append(seq)
    nres = cmd.select(f'inpdb and polymer.protein and name CA and chain {chain}')
    natoms = cmd.select(f'inpdb and chain {chain}')
    nres_per_chain.append(nres)
    natoms_per_chain.append(natoms)
    print(bcolors.BOLD + f'chain {chain}' + bcolors.ENDC)
    print(f'number or residues:\t{nres}')
    print(f'number or atoms:\t{natoms}')
ruler('#', length=64)
nres_per_chain = numpy.asarray(nres_per_chain)
natoms_per_chain = numpy.asarray(natoms_per_chain)
print(bcolors.BOLD + f'Total number of chain:\t\t{len(chains)}')
print(f'Total number of residues:\t{nres_per_chain.sum()}')
print(f'Total number of atoms:\t\t{natoms_per_chain.sum()}' + bcolors.ENDC)
