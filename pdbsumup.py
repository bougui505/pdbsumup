#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-05-29 14:37:24 (UTC+0200)

import argparse
import hashlib
import numpy
from pymol import cmd

parser = argparse.ArgumentParser(description='Get a sum up for a Protein structure file (e.g. pdb file) -- Example usage: ./pdbsumup.py --pdb data/4ci0.pdb')
parser.add_argument('--pdb', type=str, help='Protein structure file',
                    required=True)
parser.add_argument('--select', type=str, help='Select part of the structure',
                    required=False, default='all')
args = parser.parse_args()

PDBFILENAME = args.pdb


def ruler(char='-', length=32):
    print(char * length)


def md5sum(inp):
    inp = numpy.asarray(inp)
    inp = inp.flatten()
    instr = [str(e) for e in inp]
    instr = ''.join(instr)
    instr = instr.encode('utf-8')
    return hashlib.sha224(instr).hexdigest()


cmd.load(PDBFILENAME, 'inpdb')
cmd.remove(f'not (inpdb and {args.select})')
chains = cmd.get_chains('inpdb')
seqs = []
nres_per_chain = []
natoms_per_chain = []
for chain in chains:
    ruler()
    seq = cmd.get_fastastr(f'inpdb and chain {chain} and polymer.protein')
    seqs.append(seq)
    nres = cmd.select(f'inpdb and polymer.protein and name CA and chain {chain}')
    natoms = cmd.select(f'inpdb and chain {chain}')
    nres_per_chain.append(nres)
    natoms_per_chain.append(natoms)
    print(f'chain {chain}')
    print(f'number or residues:\t{nres}')
    print(f'number or atoms:\t{natoms}')
    print(f'Sequence hash: {md5sum(seq)}')
ruler('#', length=80)
nres_per_chain = numpy.asarray(nres_per_chain)
natoms_per_chain = numpy.asarray(natoms_per_chain)
print(f'Total number of chains:\t\t{len(chains)}')
print(f'Total number of residues:\t{nres_per_chain.sum()}')
print(f'Total number of atoms:\t\t{natoms_per_chain.sum()}')
