#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-05-29 14:37:24 (UTC+0200)

import os
import sys
sys.stdout.write('message: ')
import textwrap
import argparse
import hashlib
import numpy
from pymol import cmd


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


def clean_resids(chain):
    myspace = {'resids': []}
    cmd.iterate(f'inpdb and chain {chain} polymer.protein',
                'resids.append(resi)', space=myspace)
    resids = myspace['resids']
    altresids = []
    for r in resids:
        try:
            int(r)
        except ValueError:
            altresids.append(r)
            cmd.remove(f'resid {r} and chain {chain}')
    altresids = numpy.unique(altresids)
    return altresids


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


def print_sequence(sequence, chunks):
    seq_string = ''
    chunk_ids = list(chunks.keys())
    chunk_ids.sort()
    start = 0
    for chunk_id in chunk_ids:
        chunk = chunks[chunk_id]
        chunk_len = chunk[1] - chunk[0] + 1
        seq_string += sequence[start:start + chunk_len]
        start = chunk_len
        seq_string += '/'
    return seq_string


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


def get_unique_resids(resids):
    resids_unique = []
    rp = None
    for r in resids:
        if r != rp:
            resids_unique.append(r)
        rp = r
    return resids_unique


def print_resids(resids):
    outstr = ''
    resids = get_unique_resids(resids)
    outstr = ';'.join(['%d' % r for r in resids])
    return outstr


def print_resid_seq(sequence, resids, linewidth=80):
    """
    Print the sequence along with residue id markers
    """
    resids = get_unique_resids(resids)
    outseq = ''
    outres = ''
    for i, (s, r) in enumerate(zip(sequence, resids)):
        outseq += s
        if i % 5 == 0:
            outres += '{:5s}'.format('%d' % r)
            outres = outres.replace(' ', '.')
    rp = None
    for i, r in enumerate(resids):
        if rp is not None:
            if r - rp > 1:
                outres = outres[:i] + '/' + outres[i + 1:]
        rp = r
    outseq = textwrap.wrap(outseq, linewidth)
    outres = textwrap.wrap(outres, linewidth)
    outstr = ''
    for lineres, lineseq in zip(outres, outseq):
        outstr += '+ '
        outstr += lineres
        outstr += '\n'
        outstr += '+ '
        outstr += lineseq
        outstr += '\n'
    return outstr


def find_rigid_alignment(A, B):
    """
    See: https://en.wikipedia.org/wiki/Kabsch_algorithm
    2-D or 3-D registration with known correspondences.
    Registration occurs in the zero centered coordinate system, and then
    must be transported back.
        Args:
        -    A: Numpy array of shape (N,D) -- Point Cloud to Align (source)
        -    B: Numpy array of shape (N,D) -- Reference Point Cloud (target)
        Returns:
        -    R: optimal rotation
        -    t: optimal translation
    Test on rotation + translation and on rotation + translation + reflection
        >>> A = np.asarray([[1., 1.], [2., 2.], [1.5, 3.]])
        >>> R0 = np.asarray([[np.cos(60), -np.sin(60)], [np.sin(60), np.cos(60)]])
        >>> B = (R0.dot(A.T)).T
        >>> t0 = np.array([3., 3.])
        >>> B += t0
        >>> B.shape
        (3, 2)
        >>> R, t = find_rigid_alignment(A, B)
        >>> A_aligned = (R.dot(A.T)).T + t
        >>> rmsd = np.sqrt(((A_aligned - B)**2).sum(axis=1).mean())
        >>> rmsd
        2.5639502485114184e-16
        >>> B *= np.array([-1., 1.])
        >>> R, t = find_rigid_alignment(A, B)
        >>> A_aligned = (R.dot(A.T)).T + t
        >>> rmsd = np.sqrt(((A_aligned - B)**2).sum(axis=1).mean())
        >>> rmsd
        2.5639502485114184e-16
    """
    a_mean = A.mean(axis=0)
    b_mean = B.mean(axis=0)
    A_c = A - a_mean
    B_c = B - b_mean
    # Covariance matrix
    H = A_c.T.dot(B_c)
    U, S, Vt = numpy.linalg.svd(H)
    V = Vt.T
    # Rotation matrix
    R = V.dot(U.T)
    # Translation vector
    t = b_mean - R.dot(a_mean)
    # rmsd
    A_aligned = (R.dot(A.T)).T + t
    rmsd = numpy.sqrt(((A_aligned - B)**2).sum(axis=1).mean())
    # Get angles:
    theta_x = numpy.rad2deg(numpy.arctan2(R[2, 1], R[2, 2]))
    theta_y = numpy.rad2deg(numpy.arctan2(-R[2, 0], numpy.sqrt(R[2, 1]**2 + R[2, 2]**2)))
    theta_z = numpy.rad2deg(numpy.arctan2(R[1, 0], R[1, 1]))
    return R, t, rmsd, theta_x, theta_y, theta_z


def get_chain_seqmatch(seqhashes, natoms_per_chain, chains):
    """
    Return exact sequence match for chains
    """
    seqmatch = {(h, n): [] for (h, n) in zip(seqhashes, natoms_per_chain)}
    for h, n, c in zip(seqhashes, natoms_per_chain, chains):
        seqmatch[(h, n)].append(c)
    outstr = ''
    chains_uniq = []
    for hn in seqmatch:
        chains = seqmatch[hn]
        if len(chains) > 1:
            outstr += '\n+ '
            outstr += chains[0]
            chains_uniq.append(chains[0])
            B = cmd.get_coords(f'inpdb and chain {chains[0]} and name CA')
            for c in chains[1:]:
                outstr += '\n+ '
                A = cmd.get_coords(f'inpdb and chain {c} and name CA')
                R, t, rmsd, theta_x, theta_y, theta_z = find_rigid_alignment(A, B)
                outstr += f'={c} (RMSD={rmsd:.2f}Å, θx={theta_x:.2f}°, θy={theta_y:.2f}°, θz={theta_z:.2f}°, tx={t[0]:.2f}Å, ty={t[1]:.2f}Å, tz={t[2]:.2f}Å) '
        else:
            chains_uniq.append(chains[0])
    if outstr == '':
        outstr = 'Symmetry: No symmetry'
    outstr += f'\nunique_chains: {",".join(chains_uniq)}'
    return outstr


def get_unique_chains(seqhashes, seqs, chains, label='+ ', linewidth=80):
    """
    Return unique sequences from the pdb
    """
    seqchains = {h: [] for h in seqhashes}
    sequniq = {}
    for h, s, c in zip(seqhashes, seqs, chains):
        seqchains[h].append(c)
        sequniq[h] = s
    outfasta = ''
    for h in sequniq:
        chains = seqchains[h]
        if len(chains) > 1:
            outfasta += f"{label}>Chains "
        else:
            outfasta += f"{label}>Chain "
        outfasta += ' '.join(chains)
        outfasta += f'\n{label}'
        seqstring = sequniq[h]
        seqwrap = textwrap.wrap(seqstring, linewidth)
        outfasta += f'\n{label}'.join(seqwrap)
        outfasta += '\n'
    return outfasta


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get a sum up for a Protein structure file (e.g. pdb file)')
    parser.add_argument('--pdb', type=str, help='Protein structure file',
                        required=True)
    parser.add_argument('--select', type=str, help='Select part of the structure',
                        required=False, default='all')
    parser.add_argument('-s', '--seq', help='Print the sequence',
                        action='store_true', default=False)
    parser.add_argument('-r', '--resids', help='Print the residue ids for each chain',
                        action='store_true', default=False)
    parser.add_argument('-sr', '--seqres', help='Print the sequence along with the residue ids',
                        action='store_true', default=False)
    parser.add_argument('-f', '--fasta', help='Return a fasta file with the unique sequences',
                        action='store_true', default=False)
    parser.add_argument('-rc', '--resids_per_chain', help='Return a fasta-like output containing the residue ids',
                        action='store_true', default=False)
    parser.add_argument('--sym', help='Print symmetry informations',
                        action='store_true', default=False)
    args = parser.parse_args()

    PDBFILENAME = args.pdb

    cmd.load(PDBFILENAME, 'inpdb')
    cmd.remove(f'not (inpdb and {args.select})')
    chains = cmd.get_chains('inpdb')
    seqs = []
    resids_per_chain = []
    nres_per_chain = []
    natoms_per_chain = []
    seqhashes = []
    chains_prot = []
    chains_not_prot = []
    name = os.path.basename(os.path.splitext(PDBFILENAME)[0])
    for chain in chains:
        print()
        print(f'name: {name}')
        print(f'filename: {PDBFILENAME}')
        print(f'chain: {chain}')
        altresids = clean_resids(chain)
        if len(altresids) > 0:
            print(f'Alternate_resids: {",".join(altresids)}')
        nres = cmd.select(f'inpdb and polymer.protein and name CA and chain {chain}')
        if nres > 0:
            chains_prot.append(chain)
            seq = get_sequence(chain)
            seqs.append(seq)
            resids = get_resids(chain)
            resids_per_chain.append(resids)
            resid_chunks = get_resid_chunks(resids)
            atomnames = get_atomnames(chain)
            natoms = cmd.select(f'inpdb and chain {chain}')
            nres_per_chain.append(nres)
            natoms_per_chain.append(natoms)
            print(f'nres: {nres}')
            print(f'natoms: {natoms}')
            if args.seq:
                print(f'sequence: {seq}')
            seqhash = md5sum(seq)
            print(f'seq_hash: {seqhash}')
            seqhashes.append(seqhash)
            if args.resids:
                print(f'resids: {print_resids(resids)}')
            print(f'resids_chunks: {print_chunks(resid_chunks)}')
            print(f'atom_names_hash: {md5sum(atomnames)}')
            print(f'selection_string: {print_pymol_selection(chain, resid_chunks)}')
            if args.seqres:
                print(f'sequence:\n{print_resid_seq(seq, resids)}')
        else:
            print("comment: not a polypeptide chain")
            chains_not_prot.append(chain)
    chains = chains_prot
    print()
    print(f"name: {name}")
    print(f'filename: {PDBFILENAME}')
    nres_per_chain = numpy.asarray(nres_per_chain)
    natoms_per_chain = numpy.asarray(natoms_per_chain)
    print(f'n_polypeptidic_chains: {len(chains)}')
    print(f'polypeptidic_chain_names: {",".join(chains)}')
    print(f'n_non_polypeptidic_chains: {len(chains_not_prot)}')
    print(f'non_polypeptidic_chain_names: {",".join(chains_not_prot)}')
    if args.sym:
        print(f'Symmetry: {get_chain_seqmatch(seqhashes, natoms_per_chain, chains)}')
    if args.fasta:
        print(f'fasta:\n{get_unique_chains(seqhashes, seqs, chains)}')
    if args.resids_per_chain:
        rc = [get_unique_resids(rlist) for rlist in resids_per_chain]
        rc = [",".join([str(e) for e in rlist]) for rlist in rc]
        print(f'resids:\n{get_unique_chains(seqhashes, rc, chains, label="+ ")}')
    print(f'nres: {nres_per_chain.sum()}')
    print(f'natoms: {natoms_per_chain.sum()}')
    coords = cmd.get_coords('inpdb')
    print(f"coords_min: {' '.join([str(e) for e in coords.min(axis=0)])}")
    print(f"coords_max: {' '.join([str(e) for e in coords.max(axis=0)])}")
    boxsize = coords.max(axis=0) - coords.min(axis=0)
    print(f"box_size: {' '.join([str(e) for e in boxsize])}")
