# pdbsumup
```
$ ./pdbsumup.py -h

usage: pdbsumup.py [-h] --pdb PDB [--select SELECT]

Get a sum up for a Protein structure file (e.g. pdb file)

optional arguments:
  -h, --help       show this help message and exit
  --pdb PDB        Protein structure file
  --select SELECT  Select part of the structure
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb

 PyMOL not running, entering library mode (experimental)
--------------------------------
chain A
number or residues:	385
number or atoms:	2988
Sequence hash: 9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
--------------------------------
chain B
number or residues:	228
number or atoms:	1762
Sequence hash: 4a21f6493a367ce3fe7503f03834158adaf72594d204be86a56bf634
--------------------------------
chain C
number or residues:	280
number or atoms:	2206
Sequence hash: b3a553385e60b21aeac78c89ab59db25cf6120844e7c8014cd421dc4
################################################################################
Total number of chains:		3
Total number of residues:	893
Total number of atoms:		6956
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A+B'

 PyMOL not running, entering library mode (experimental)
--------------------------------
chain A
number or residues:	385
number or atoms:	2988
Sequence hash: 9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
--------------------------------
chain B
number or residues:	228
number or atoms:	1762
Sequence hash: 4a21f6493a367ce3fe7503f03834158adaf72594d204be86a56bf634
################################################################################
Total number of chains:		2
Total number of residues:	613
Total number of atoms:		4750
```
