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
Chain sequence match:		A ; B ; C ; 
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
Chain sequence match:		A ; B ; 
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
Total number of chains:		1
Chain sequence match:		A ; 
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
Total number of chains:		1
Chain sequence match:		A ; 
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
Total number of chains:		1
Chain sequence match:		A ; 
Total number of residues:	385
Total number of atoms:		2988
Coords min:			123.557 109.164 61.441
Coords max:			180.739 149.983 130.53
```
```
$ ./pdbsumup.py --pdb data/5lcw.pdb

 PyMOL not running, entering library mode (experimental)
--------------------------------
chain A
number of residues:	1441
number of atoms:	10949
Sequence hash:		3bf262727d8a23a122b91e9ec240c37dedfab927c3d8eaa66430236b
Residue chunks:		11..58/71..134/146..192/206..226/236..280/346..360/402..414/424..460/464..513/582..670/757..814/839..882/924..986/1013..1333/1347..1437/1452..1680/1684..1711/1727..1734/1739..1827/1839..1873/1877..1897/1912..1936
Atom names hash:	bc2ad5ac1b82a23ef215c2c75eefb40c45bfc5f4cc4676d1dfa94e5e
Pymol selection string:	chain A and resi 11-58+71-134+146-192+206-226+236-280+346-360+402-414+424-460+464-513+582-670+757-814+839-882+924-986+1013-1333+1347-1437+1452-1680+1684-1711+1727-1734+1739-1827+1839-1873+1877-1897+1912-1936
--------------------------------
chain B
number of residues:	79
number of atoms:	643
Sequence hash:		88b2b6b8e7c20a3b150305fdbd8dde4f524dca5870bcf944ad9ebc70
Residue chunks:		1..17/23..84
Atom names hash:	c5eb3d944a48d7b4410f37985d0a4e22fee182abcfe6dbc3c3a700d4
Pymol selection string:	chain B and resi 1-17+23-84
--------------------------------
chain C
number of residues:	524
number of atoms:	4306
Sequence hash:		da4a11ef0b7876e5e69b11aa337e1b131d93cdeec667cb4b55827418
Residue chunks:		26..500/509..557
Atom names hash:	48c4de1beb98cd5ae87463e6bf9f68f0bbbb834a47880a47274f4e02
Pymol selection string:	chain C and resi 26-500+509-557
--------------------------------
chain D
number of residues:	18
number of atoms:	153
Sequence hash:		c28fc99b18a79e49e2144a849ed0dbd724b6ae5c540cc2f8fec8e9e5
Residue chunks:		2..19
Atom names hash:	f7ff4d2cb305a0c18752a52b73451c92c5270eb3d36f7f08fc162c47
Pymol selection string:	chain D and resi 2-19
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
chain I
number of residues:	733
number of atoms:	5716
Sequence hash:		09ba4cb7d6d18c2eb3a18589e97310c208dd5de950e89faaeef9fd97
Residue chunks:		6..129/132..456/474..757
Atom names hash:	1f489c864056fc8807cd76a39e2587eba850593dbbe5856b76c97e43
Pymol selection string:	chain I and resi 6-129+132-456+474-757
--------------------------------
chain J
number of residues:	504
number of atoms:	4047
Sequence hash:		7fbd7247683d4d881d56057a354429e75b3dc7f97ea0fdbcedf770f8
Residue chunks:		2..95/124..533
Atom names hash:	b1a25eb1112726e4ab5af016968dde430ca4c5bc3b35cb4921201f33
Pymol selection string:	chain J and resi 2-95+124-533
--------------------------------
chain K
number of residues:	493
number of atoms:	3988
Sequence hash:		1aa88973f6f0f87c6536a4f6c0bc66137f71ba1c8986f3aad3ab58c2
Residue chunks:		2..93/127..527
Atom names hash:	cfe8bb054db1ef82a1c3196a805e892a4ae7d24a10a4958af5811426
Pymol selection string:	chain K and resi 2-93+127-527
--------------------------------
chain L
number of residues:	182
number of atoms:	1435
Sequence hash:		ab5688b276e5fb95005656e5394ce493d13c8b305ae7a8695a50e926
Residue chunks:		3..184
Atom names hash:	054d6948c098a4cb909068e283576ca7b1390bd4e69338745109e5d1
Pymol selection string:	chain L and resi 3-184
--------------------------------
chain M
number of residues:	59
number of atoms:	493
Sequence hash:		d784d5cae4aea58fbd2913b17b5990ed19b02f9cc3052a4325c70ea5
Residue chunks:		1..39/48..67
Atom names hash:	881b2bb2b1a5ba1677af9938ece026bf84b962222aa66ed8607694ef
Pymol selection string:	chain M and resi 1-39+48-67
--------------------------------
chain N
number of residues:	703
number of atoms:	5403
Sequence hash:		35cb2b296ad5bd47d5269f7cd3e1fd90456118e8c714cd2b1c783f19
Residue chunks:		15..29/53..65/70..102/107..191/196..220/232..304/320..443/451..458/476..730/747..818
Atom names hash:	30108bd9990be298fd5b6f71a11c28aeac64b83e210a1ec2c4965065
Pymol selection string:	chain N and resi 15-29+53-65+70-102+107-191+196-220+232-304+320-443+451-458+476-730+747-818
--------------------------------
chain O
number of residues:	685
number of atoms:	5402
Sequence hash:		9981f11fa51690f1ec2341f14acbbf4b4f2fa7fde3b45903c8e624c5
Residue chunks:		27..169/206..452/459..746/749..755
Atom names hash:	bce30055455161546be8ecf828c33294673782507901ef59dc379c31
Pymol selection string:	chain O and resi 27-169+206-452+459-746+749-755
--------------------------------
chain P
number of residues:	491
number of atoms:	4043
Sequence hash:		9a366a46e42a8c55540bdbbd9a4b235e8cc494f61dd6a3a98b7e7e80
Residue chunks:		26..134/147..500/511..538
Atom names hash:	f573c917f8fbb98e53a6dabcdf4151b754d59ae4678411fdf19fb3aa
Pymol selection string:	chain P and resi 26-134+147-500+511-538
--------------------------------
chain Q
number of residues:	354
number of atoms:	2671
Sequence hash:		1d7f4101f22cd89f113b2a3d8c19268e051f9c5a7f7b2546cf231473
Residue chunks:		126..146/158..482/492..499
Atom names hash:	876f89964af8ea4a881d58fadd313b6c6298ed50248349237e7caaf1
Pymol selection string:	chain Q and resi 126-146+158-482+492-499
--------------------------------
chain R
number of residues:	383
number of atoms:	2953
Sequence hash:		aacd9b7694c78df5bfddcbb200cc4442de734a1acb7c5de08514ce1c
Residue chunks:		73..135/165..476/492..499
Atom names hash:	1ea031101724be1ec8f18b4f919bd29d940150871e6b989f8cf77aad
Pymol selection string:	chain R and resi 73-135+165-476+492-499
--------------------------------
chain S
number of residues:	277
number of atoms:	2077
Sequence hash:		9abaef5f34568c9584fdc5d53402c7a4ea55684de73da10139425482
Residue chunks:		19..207/221..239/255..310/529..533/553..560
Atom names hash:	2bc4a577669b05b2853db80ec3a94bbdd7f02d297727a112b9845ee9
Pymol selection string:	chain S and resi 19-207+221-239+255-310+529-533+553-560
--------------------------------
chain W
number of residues:	25
number of atoms:	213
Sequence hash:		5bb6443300b079605ab05233e8dc4bdae7cb8eda6283e6b31eb71b29
Residue chunks:		1..25
Atom names hash:	9f45fbbf797dc8ec13b67f7b1e3298fb091ee9281a2d3183b298c7c2
Pymol selection string:	chain W and resi 1-25
--------------------------------
chain X
number of residues:	484
number of atoms:	3773
Sequence hash:		23b77cb054f6c36ceba40e1bf26a0fce3be12e3aa013f0334b3e0e03
Residue chunks:		36..110/132..540
Atom names hash:	396d187b3708dd9ad0ad8c5684e28aa1fc7a4cb66e4ed437c6869f66
Pymol selection string:	chain X and resi 36-110+132-540
--------------------------------
chain Y
number of residues:	496
number of atoms:	3868
Sequence hash:		fbce4c09c5ea51b9162dbd4028d5f11396fcd49eff9dc3213058bda7
Residue chunks:		36..110/132..552
Atom names hash:	f5ee3fc3ba53c96bdef9e6a1163ac887c70adce79fc4cb95d3fa22f6
Pymol selection string:	chain Y and resi 36-110+132-552
--------------------------------
chain Z
number of residues:	195
number of atoms:	1577
Sequence hash:		6280979c6da782615a2dedf804082fcecea201925c2c2c7ec82dca63
Residue chunks:		8..202
Atom names hash:	a7006aae172178e9568364b1fdf8c901b2417ff6013e56b278e690fa
Pymol selection string:	chain Z and resi 8-202
################################################################################
Total number of chains:		23
Chain sequence match:		A ; B ; C ; D ; E ; F=H ; G=W ; I ; J ; K ; L ; M ; N ; O ; P ; Q ; R ; S ; X ; Y ; Z ; 
Total number of residues:	9173
Total number of atoms:		72075
Coords min:			72.86 86.77 69.615
Coords max:			291.912 273.047 283.79
```
