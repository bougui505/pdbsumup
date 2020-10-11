# pdbsumup
```
$ ./pdbsumup.py -h

usage: pdbsumup.py [-h] --pdb PDB [--select SELECT] [-s] [-r] [-sr]

Get a sum up for a Protein structure file (e.g. pdb file)

optional arguments:
  -h, --help       show this help message and exit
  --pdb PDB        Protein structure file
  --select SELECT  Select part of the structure
  -s, --seq        Print the sequence
  -r, --resids     Print the residue ids
  -sr, --seqres    Print the sequence along with the residue ids
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb

 PyMOL not running, entering library mode (experimental)
--------------------------------
chain A
number of residues:	385
number of atoms:	2988
Sequence hash:		9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
Residue chunks:		2..386
Atom names hash:	401e196f15ac649d654360a1ed36fd1bd1156cf62ca23fd188f10195
Pymol selection string:	chain A and resi 2-386
--------------------------------
chain B
number of residues:	228
number of atoms:	1762
Sequence hash:		4a21f6493a367ce3fe7503f03834158adaf72594d204be86a56bf634
Residue chunks:		46..273
Atom names hash:	af20fd05b0db3a8d95e60b1c95217b6c2d29cd71efeea627e50bb64d
Pymol selection string:	chain B and resi 46-273
--------------------------------
chain C
number of residues:	280
number of atoms:	2206
Sequence hash:		b3a553385e60b21aeac78c89ab59db25cf6120844e7c8014cd421dc4
Residue chunks:		2..281
Atom names hash:	77e11bf0423da1a43dd294621849c68de901ccca51b3d1e72281423f
Pymol selection string:	chain C and resi 2-281
################################################################################
Total number of chains:		3
Total number of residues:	893
Total number of atoms:		6956
Coords min:			123.557 71.199 61.441
Coords max:			204.933 149.983 148.387
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A+B'

 PyMOL not running, entering library mode (experimental)
--------------------------------
chain A
number of residues:	385
number of atoms:	2988
Sequence hash:		9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
Residue chunks:		2..386
Atom names hash:	401e196f15ac649d654360a1ed36fd1bd1156cf62ca23fd188f10195
Pymol selection string:	chain A and resi 2-386
--------------------------------
chain B
number of residues:	228
number of atoms:	1762
Sequence hash:		4a21f6493a367ce3fe7503f03834158adaf72594d204be86a56bf634
Residue chunks:		46..273
Atom names hash:	af20fd05b0db3a8d95e60b1c95217b6c2d29cd71efeea627e50bb64d
Pymol selection string:	chain B and resi 46-273
################################################################################
Total number of chains:		2
Total number of residues:	613
Total number of atoms:		4750
Coords min:			123.557 85.071 61.441
Coords max:			184.331 149.983 130.53
```
