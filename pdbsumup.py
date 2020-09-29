#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-05-29 14:37:24 (UTC+0200)

import argparse
import hashlib
import numpy
from pymol import cmd

parser = argparse.ArgumentParser(description='Get a sum up for a Protein structure file (e.g. pdb file)')
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


def get_sequence(chain):
    seq = cmd.get_fastastr(f'inpdb and chain {chain} and polymer.protein')
    seq = seq.split()[1:]
    seq = ''.join(seq)
    return seq


def get_resids(chain):
    myspace = {'resids': []}
    cmd.iterate(f'inpdb and chain {chain} and polymer.protein',
                'resids.append(resi)', space=myspace)
    resids = numpy.int_(myspace['resids'])
    return resids


def get_atomnames(chain):
    myspace = {'atomnames': []}
    cmd.iterate(f'inpdb and chain {chain} and polymer.protein',
                'atomnames.append(name)', space=myspace)
    atomnames = myspace['atomnames']
    return atomnames


def get_resid_chunks(resids):
    chunks = {0: [resids[0], ]}
    inds = numpy.where(numpy.diff(resids) > 1)[0]
    for i, ind in enumerate(inds):
        chunks[i].append(resids[ind])
        chunks[i + 1] = [resids[ind + 1]]
    keys = list(chunks.keys())
    keys.sort()
    chunks[keys[-1]].append(resids[-1])
    return chunks


def print_chunks(chunks):
    keys = list(chunks.keys())
    keys.sort()
    out = ''
    nchunks = len(keys)
    for i, k in enumerate(keys):
        out += f'{chunks[k][0]}..{chunks[k][1]}'
        if i < nchunks - 1:
            out += '/'
    return out


def print_pymol_selection(chain, chunks):
    keys = list(chunks.keys())
    keys.sort()
    out = f'chain {chain} and resi '
    nchunks = len(keys)
    for i, k in enumerate(keys):
        out += f'{chunks[k][0]}-{chunks[k][1]}'
        if i < nchunks - 1:
            out += '+'
    return out


cmd.load(PDBFILENAME, 'inpdb')
cmd.remove(f'not (inpdb and {args.select})')
chains = cmd.get_chains('inpdb')
seqs = []
nres_per_chain = []
natoms_per_chain = []
for chain in chains:
    ruler()
    seq = get_sequence(chain)
    seqs.append(seq)
    resids = get_resids(chain)
    resid_chunks = get_resid_chunks(resids)
    atomnames = get_atomnames(chain)
    nres = cmd.select(f'inpdb and polymer.protein and name CA and chain {chain}')
    natoms = cmd.select(f'inpdb and chain {chain}')
    nres_per_chain.append(nres)
    natoms_per_chain.append(natoms)
    print(f'chain {chain}')
    print(f'number of residues:\t{nres}')
    print(f'number of atoms:\t{natoms}')
    print(f'Sequence hash:\t\t{md5sum(seq)}')
    print(f'Residue chunks:\t\t{print_chunks(resid_chunks)}')
    print(f'Atom names hash:\t{md5sum(atomnames)}')
    print(f'Pymol selection string:\t{print_pymol_selection(chain, resid_chunks)}')
ruler('#', length=80)
nres_per_chain = numpy.asarray(nres_per_chain)
natoms_per_chain = numpy.asarray(natoms_per_chain)
print(f'Total number of chains:\t\t{len(chains)}')
print(f'Total number of residues:\t{nres_per_chain.sum()}')
print(f'Total number of atoms:\t\t{natoms_per_chain.sum()}')
coords = cmd.get_coords('inpdb')
print(f"Coords min:\t\t\t{' '.join([str(e) for e in coords.min(axis=0)])}")
print(f"Coords max:\t\t\t{' '.join([str(e) for e in coords.max(axis=0)])}")
