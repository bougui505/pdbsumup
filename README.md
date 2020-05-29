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
Sequence hash: be1ab48bbe59179699d6bebe9223b4a92c729bf5e79860ea3594bfc9
--------------------------------
chain B
number or residues:	228
number or atoms:	1762
Sequence hash: cf1d57745304f8e1454ca70575cfb9bb597638c1fd751e04c4e8e414
--------------------------------
chain C
number or residues:	280
number or atoms:	2206
Sequence hash: d11457e2bcc622c0142d32f4b8a389788e77c9a37d842b42508688f9
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
Sequence hash: be1ab48bbe59179699d6bebe9223b4a92c729bf5e79860ea3594bfc9
--------------------------------
chain B
number or residues:	228
number or atoms:	1762
Sequence hash: cf1d57745304f8e1454ca70575cfb9bb597638c1fd751e04c4e8e414
################################################################################
Total number of chains:		2
Total number of residues:	613
Total number of atoms:		4750
```
