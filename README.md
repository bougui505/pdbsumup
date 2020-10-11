# pdbsumup
```
$ ./pdbsumup.py -h

usage: pdbsumup.py [-h] --pdb PDB [--select SELECT] [-s] [-r] [-sr] [--sym]

Get a sum up for a Protein structure file (e.g. pdb file)

optional arguments:
  -h, --help       show this help message and exit
  --pdb PDB        Protein structure file
  --select SELECT  Select part of the structure
  -s, --seq        Print the sequence
  -r, --resids     Print the residue ids
  -sr, --seqres    Print the sequence along with the residue ids
  --sym            Print symmetry informations
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
Total number of chains:		3 (ABC)
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
Total number of chains:		2 (AB)
Total number of residues:	613
Total number of atoms:		4750
Coords min:			123.557 85.071 61.441
Coords max:			184.331 149.983 130.53
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A' -s

 PyMOL not running, entering library mode (experimental)
--------------------------------
chain A
number of residues:	385
number of atoms:	2988
Sequence:		SERIVISPTSRQEGHAELVMEVDDEGIVTKGRYFSITPVRGLEKMVTGKAPETAPVMVQRICGVCPIPHTLASVEAIDDSLDIEVPKAGRLLRELTLAAHHVNSHAIHHFLIAPDFVPENLMADAINSVSEIRKNAQYVVDMVAGEGIHPSDVRIGGMADNITELARKRLYARLKQLKPKVNEHVELMIGLIEDKGLPEGLGVHNQPTLASHQIYGDRTKFDLDRFTEIMPESWYDDPEIAKRACSTIPLYDGRNVEVGPRARMVEFQGFKERGVVAQHVARALEMKTALSRAIEILDELDTSAPVRADFDERGTGKLGIGAIEAPRGLDVHMAKVENGKIQFYSALVPTTWNIPTMGPATEGFHHEYGPHVIRAYDPCLSCATH/
Sequence hash:		9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
Residue chunks:		2..386
Atom names hash:	401e196f15ac649d654360a1ed36fd1bd1156cf62ca23fd188f10195
Pymol selection string:	chain A and resi 2-386
################################################################################
Total number of chains:		1 (A)
Total number of residues:	385
Total number of atoms:		2988
Coords min:			123.557 109.164 61.441
Coords max:			180.739 149.983 130.53
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A' -r

 PyMOL not running, entering library mode (experimental)
--------------------------------
chain A
number of residues:	385
number of atoms:	2988
Sequence hash:		9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
Resids:			2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 
Residue chunks:		2..386
Atom names hash:	401e196f15ac649d654360a1ed36fd1bd1156cf62ca23fd188f10195
Pymol selection string:	chain A and resi 2-386
################################################################################
Total number of chains:		1 (A)
Total number of residues:	385
Total number of atoms:		2988
Coords min:			123.557 109.164 61.441
Coords max:			180.739 149.983 130.53
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A' -sr

 PyMOL not running, entering library mode (experimental)
--------------------------------
chain A
number of residues:	385
number of atoms:	2988
Sequence hash:		9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
Residue chunks:		2..386
Atom names hash:	401e196f15ac649d654360a1ed36fd1bd1156cf62ca23fd188f10195
Pymol selection string:	chain A and resi 2-386
Sequence:
| 2....7....12...17...22...27...32...37...42...47...52...57...62...67...72...77...
| SERIVISPTSRQEGHAELVMEVDDEGIVTKGRYFSITPVRGLEKMVTGKAPETAPVMVQRICGVCPIPHTLASVEAIDDS
| 82...87...92...97...102..107..112..117..122..127..132..137..142..147..152..157..
| LDIEVPKAGRLLRELTLAAHHVNSHAIHHFLIAPDFVPENLMADAINSVSEIRKNAQYVVDMVAGEGIHPSDVRIGGMAD
| 162..167..172..177..182..187..192..197..202..207..212..217..222..227..232..237..
| NITELARKRLYARLKQLKPKVNEHVELMIGLIEDKGLPEGLGVHNQPTLASHQIYGDRTKFDLDRFTEIMPESWYDDPEI
| 242..247..252..257..262..267..272..277..282..287..292..297..302..307..312..317..
| AKRACSTIPLYDGRNVEVGPRARMVEFQGFKERGVVAQHVARALEMKTALSRAIEILDELDTSAPVRADFDERGTGKLGI
| 322..327..332..337..342..347..352..357..362..367..372..377..382..
| GAIEAPRGLDVHMAKVENGKIQFYSALVPTTWNIPTMGPATEGFHHEYGPHVIRAYDPCLSCATH

################################################################################
Total number of chains:		1 (A)
Total number of residues:	385
Total number of atoms:		2988
Coords min:			123.557 109.164 61.441
Coords max:			180.739 149.983 130.53
```
```
$ ./pdbsumup.py --pdb data/5lcw.pdb --select 'chain E+F+H+G+W' --sym

 PyMOL not running, entering library mode (experimental)
--------------------------------
chain E
number of residues:	56
number of atoms:	450
Sequence hash:		6ef38111b84d9e87e58a4da334dae8693a66f7ca4b8148c3295728c0
Residue chunks:		52..107
Atom names hash:	51e1d213788916943e4e9a4ea6ed38aab298f0cb7450918703ea984b
Pymol selection string:	chain E and resi 52-107
--------------------------------
chain F
number of residues:	483
number of atoms:	3849
Sequence hash:		819531b3770d7fcc82e39645448e9d8621d3eda62ae44927c4024f65
Residue chunks:		5..170/451..767
Atom names hash:	abe8c808a518f7095dfd9a297293dfbbe09f56fba0c2a75420c9d2e9
Pymol selection string:	chain F and resi 5-170+451-767
--------------------------------
chain G
number of residues:	25
number of atoms:	213
Sequence hash:		5bb6443300b079605ab05233e8dc4bdae7cb8eda6283e6b31eb71b29
Residue chunks:		1..25
Atom names hash:	9f45fbbf797dc8ec13b67f7b1e3298fb091ee9281a2d3183b298c7c2
Pymol selection string:	chain G and resi 1-25
--------------------------------
chain H
number of residues:	483
number of atoms:	3853
Sequence hash:		819531b3770d7fcc82e39645448e9d8621d3eda62ae44927c4024f65
Residue chunks:		5..170/451..767
Atom names hash:	3dc465a98d9ee7254717491b7922df92df8d8f5e05eaaaed4a0b826c
Pymol selection string:	chain H and resi 5-170+451-767
--------------------------------
chain W
number of residues:	25
number of atoms:	213
Sequence hash:		5bb6443300b079605ab05233e8dc4bdae7cb8eda6283e6b31eb71b29
Residue chunks:		1..25
Atom names hash:	9f45fbbf797dc8ec13b67f7b1e3298fb091ee9281a2d3183b298c7c2
Pymol selection string:	chain W and resi 1-25
################################################################################
Total number of chains:		5 (EFGHW)
Symmetry:			F=H (RMSD=1.69Å, θx=173.85°, θy=-0.20°, θz=-86.78°, tx=357.94Å, ty=319.33Å, tz=363.43Å) 
				G=W (RMSD=0.95Å, θx=-131.46°, θy=-41.19°, θz=-97.49°, tx=315.93Å, ty=422.42Å, tz=243.46Å) 
				
Total number of residues:	1072
Total number of atoms:		8578
Coords min:			81.228 134.165 110.565
Coords max:			170.09 249.44 253.405
```
