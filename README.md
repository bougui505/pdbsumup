# pdbsumup
```
$ ./pdbsumup.py -h

message: usage: pdbsumup.py [-h] --pdb PDB [--select SELECT] [-s] [-r] [-sr] [-f] [-rc]
                   [--sym] [--coords] [--inter] [--aln]

Get a sum up for a Protein structure file (e.g. pdb file)

optional arguments:
  -h, --help            show this help message and exit
  --pdb PDB             Protein structure file
  --select SELECT       Select part of the structure
  -s, --seq             Print the sequence
  -r, --resids          Print the residue ids for each chain
  -sr, --seqres         Print the sequence along with the residue ids
  -f, --fasta           Return a fasta file with the unique sequences
  -rc, --resids_per_chain
                        Return a fasta-like output containing the residue ids
  --sym                 Print symmetry informations
  --coords              Print coordinates
  --inter               Get chain chain interface map
  --aln                 Align pairwisely the sequence of the chains and return
                        the pairwise matrix of sequence identity
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb

message: 
name: 4ci0
filename: data/4ci0.pdb
chain: A
nres: 385
natoms: 2988
seq_hash: 9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
resids_chunks: 2..386
ligand_names: FE NI FE2
ligand_resids: 1387 1388 1389
ligand_selection_string: chain A and resi 1387-1389
atom_names_hash: 401e196f15ac649d654360a1ed36fd1bd1156cf62ca23fd188f10195
selection_string: chain A and resi 2-386

name: 4ci0
filename: data/4ci0.pdb
chain: B
nres: 228
natoms: 1762
seq_hash: 4a21f6493a367ce3fe7503f03834158adaf72594d204be86a56bf634
resids_chunks: 46..273
ligand_names: SF4 SF4 SF4 ZN
ligand_resids: 1274 1275 1276 1277
ligand_selection_string: chain B and resi 1274-1277
atom_names_hash: af20fd05b0db3a8d95e60b1c95217b6c2d29cd71efeea627e50bb64d
selection_string: chain B and resi 46-273

name: 4ci0
filename: data/4ci0.pdb
chain: C
nres: 280
natoms: 2206
seq_hash: b3a553385e60b21aeac78c89ab59db25cf6120844e7c8014cd421dc4
resids_chunks: 2..281
ligand_names: SF4 FAD
ligand_resids: 1282 1283
ligand_selection_string: chain C and resi 1282-1283
atom_names_hash: 77e11bf0423da1a43dd294621849c68de901ccca51b3d1e72281423f
selection_string: chain C and resi 2-281

name: 4ci0
filename: data/4ci0.pdb
n_polypeptidic_chains: 3
polypeptidic_chain_names: A,B,C
n_non_polypeptidic_chains: 0
non_polypeptidic_chain_names: 
nres: 893
natoms: 6956
coords_min: 123.557 71.199 61.441
coords_max: 204.933 149.983 148.387
box_size: 81.376 78.784004 86.94599
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A+B'

message: 
name: 4ci0
filename: data/4ci0.pdb
chain: A
nres: 385
natoms: 2988
seq_hash: 9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
resids_chunks: 2..386
ligand_names: FE NI FE2
ligand_resids: 1387 1388 1389
ligand_selection_string: chain A and resi 1387-1389
atom_names_hash: 401e196f15ac649d654360a1ed36fd1bd1156cf62ca23fd188f10195
selection_string: chain A and resi 2-386

name: 4ci0
filename: data/4ci0.pdb
chain: B
nres: 228
natoms: 1762
seq_hash: 4a21f6493a367ce3fe7503f03834158adaf72594d204be86a56bf634
resids_chunks: 46..273
ligand_names: SF4 SF4 SF4 ZN
ligand_resids: 1274 1275 1276 1277
ligand_selection_string: chain B and resi 1274-1277
atom_names_hash: af20fd05b0db3a8d95e60b1c95217b6c2d29cd71efeea627e50bb64d
selection_string: chain B and resi 46-273

name: 4ci0
filename: data/4ci0.pdb
n_polypeptidic_chains: 2
polypeptidic_chain_names: A,B
n_non_polypeptidic_chains: 0
non_polypeptidic_chain_names: 
nres: 613
natoms: 4750
coords_min: 123.557 85.071 61.441
coords_max: 184.331 149.983 130.53
box_size: 60.773994 64.912 69.089
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A' -s

message: 
name: 4ci0
filename: data/4ci0.pdb
chain: A
nres: 385
natoms: 2988
sequence: SERIVISPTSRQEGHAELVMEVDDEGIVTKGRYFSITPVRGLEKMVTGKAPETAPVMVQRICGVCPIPHTLASVEAIDDSLDIEVPKAGRLLRELTLAAHHVNSHAIHHFLIAPDFVPENLMADAINSVSEIRKNAQYVVDMVAGEGIHPSDVRIGGMADNITELARKRLYARLKQLKPKVNEHVELMIGLIEDKGLPEGLGVHNQPTLASHQIYGDRTKFDLDRFTEIMPESWYDDPEIAKRACSTIPLYDGRNVEVGPRARMVEFQGFKERGVVAQHVARALEMKTALSRAIEILDELDTSAPVRADFDERGTGKLGIGAIEAPRGLDVHMAKVENGKIQFYSALVPTTWNIPTMGPATEGFHHEYGPHVIRAYDPCLSCATH
seq_hash: 9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
resids_chunks: 2..386
ligand_names: FE NI FE2
ligand_resids: 1387 1388 1389
ligand_selection_string: chain A and resi 1387-1389
atom_names_hash: 401e196f15ac649d654360a1ed36fd1bd1156cf62ca23fd188f10195
selection_string: chain A and resi 2-386

name: 4ci0
filename: data/4ci0.pdb
n_polypeptidic_chains: 1
polypeptidic_chain_names: A
n_non_polypeptidic_chains: 0
non_polypeptidic_chain_names: 
nres: 385
natoms: 2988
coords_min: 123.557 109.164 61.441
coords_max: 180.739 149.983 130.53
box_size: 57.182 40.819 69.089
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A' -r

message: 
name: 4ci0
filename: data/4ci0.pdb
chain: A
nres: 385
natoms: 2988
seq_hash: 9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
resids: 2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;51;52;53;54;55;56;57;58;59;60;61;62;63;64;65;66;67;68;69;70;71;72;73;74;75;76;77;78;79;80;81;82;83;84;85;86;87;88;89;90;91;92;93;94;95;96;97;98;99;100;101;102;103;104;105;106;107;108;109;110;111;112;113;114;115;116;117;118;119;120;121;122;123;124;125;126;127;128;129;130;131;132;133;134;135;136;137;138;139;140;141;142;143;144;145;146;147;148;149;150;151;152;153;154;155;156;157;158;159;160;161;162;163;164;165;166;167;168;169;170;171;172;173;174;175;176;177;178;179;180;181;182;183;184;185;186;187;188;189;190;191;192;193;194;195;196;197;198;199;200;201;202;203;204;205;206;207;208;209;210;211;212;213;214;215;216;217;218;219;220;221;222;223;224;225;226;227;228;229;230;231;232;233;234;235;236;237;238;239;240;241;242;243;244;245;246;247;248;249;250;251;252;253;254;255;256;257;258;259;260;261;262;263;264;265;266;267;268;269;270;271;272;273;274;275;276;277;278;279;280;281;282;283;284;285;286;287;288;289;290;291;292;293;294;295;296;297;298;299;300;301;302;303;304;305;306;307;308;309;310;311;312;313;314;315;316;317;318;319;320;321;322;323;324;325;326;327;328;329;330;331;332;333;334;335;336;337;338;339;340;341;342;343;344;345;346;347;348;349;350;351;352;353;354;355;356;357;358;359;360;361;362;363;364;365;366;367;368;369;370;371;372;373;374;375;376;377;378;379;380;381;382;383;384;385;386
resids_chunks: 2..386
ligand_names: FE NI FE2
ligand_resids: 1387 1388 1389
ligand_selection_string: chain A and resi 1387-1389
atom_names_hash: 401e196f15ac649d654360a1ed36fd1bd1156cf62ca23fd188f10195
selection_string: chain A and resi 2-386

name: 4ci0
filename: data/4ci0.pdb
n_polypeptidic_chains: 1
polypeptidic_chain_names: A
n_non_polypeptidic_chains: 0
non_polypeptidic_chain_names: 
nres: 385
natoms: 2988
coords_min: 123.557 109.164 61.441
coords_max: 180.739 149.983 130.53
box_size: 57.182 40.819 69.089
```
```
$ ./pdbsumup.py --pdb data/4ci0.pdb --select 'chain A' -sr

message: 
name: 4ci0
filename: data/4ci0.pdb
chain: A
nres: 385
natoms: 2988
seq_hash: 9627ab006ea654bdabf4bdd7b3a4c11eee47fe6f1164a55b1249cb95
resids_chunks: 2..386
ligand_names: FE NI FE2
ligand_resids: 1387 1388 1389
ligand_selection_string: chain A and resi 1387-1389
atom_names_hash: 401e196f15ac649d654360a1ed36fd1bd1156cf62ca23fd188f10195
selection_string: chain A and resi 2-386
sequence:
+ 2....7....12...17...22...27...32...37...42...47...52...57...62...67...72...77...
+ SERIVISPTSRQEGHAELVMEVDDEGIVTKGRYFSITPVRGLEKMVTGKAPETAPVMVQRICGVCPIPHTLASVEAIDDS
+ 82...87...92...97...102..107..112..117..122..127..132..137..142..147..152..157..
+ LDIEVPKAGRLLRELTLAAHHVNSHAIHHFLIAPDFVPENLMADAINSVSEIRKNAQYVVDMVAGEGIHPSDVRIGGMAD
+ 162..167..172..177..182..187..192..197..202..207..212..217..222..227..232..237..
+ NITELARKRLYARLKQLKPKVNEHVELMIGLIEDKGLPEGLGVHNQPTLASHQIYGDRTKFDLDRFTEIMPESWYDDPEI
+ 242..247..252..257..262..267..272..277..282..287..292..297..302..307..312..317..
+ AKRACSTIPLYDGRNVEVGPRARMVEFQGFKERGVVAQHVARALEMKTALSRAIEILDELDTSAPVRADFDERGTGKLGI
+ 322..327..332..337..342..347..352..357..362..367..372..377..382..
+ GAIEAPRGLDVHMAKVENGKIQFYSALVPTTWNIPTMGPATEGFHHEYGPHVIRAYDPCLSCATH


name: 4ci0
filename: data/4ci0.pdb
n_polypeptidic_chains: 1
polypeptidic_chain_names: A
n_non_polypeptidic_chains: 0
non_polypeptidic_chain_names: 
nres: 385
natoms: 2988
coords_min: 123.557 109.164 61.441
coords_max: 180.739 149.983 130.53
box_size: 57.182 40.819 69.089
```
```
$ ./pdbsumup.py --pdb data/5lcw.pdb --select 'chain E+F+H+G+W' --sym --fasta

message: 
name: 5lcw
filename: data/5lcw.pdb
chain: E
nres: 56
natoms: 450
seq_hash: 6ef38111b84d9e87e58a4da334dae8693a66f7ca4b8148c3295728c0
resids_chunks: 52..107
atom_names_hash: 51e1d213788916943e4e9a4ea6ed38aab298f0cb7450918703ea984b
selection_string: chain E and resi 52-107

name: 5lcw
filename: data/5lcw.pdb
chain: F
nres: 483
natoms: 3849
seq_hash: 819531b3770d7fcc82e39645448e9d8621d3eda62ae44927c4024f65
resids_chunks: 5..170/451..767
atom_names_hash: abe8c808a518f7095dfd9a297293dfbbe09f56fba0c2a75420c9d2e9
selection_string: chain F and resi 5-170+451-767

name: 5lcw
filename: data/5lcw.pdb
chain: G
nres: 25
natoms: 213
seq_hash: 5bb6443300b079605ab05233e8dc4bdae7cb8eda6283e6b31eb71b29
resids_chunks: 1..25
atom_names_hash: 9f45fbbf797dc8ec13b67f7b1e3298fb091ee9281a2d3183b298c7c2
selection_string: chain G and resi 1-25

name: 5lcw
filename: data/5lcw.pdb
chain: H
nres: 483
natoms: 3853
seq_hash: 819531b3770d7fcc82e39645448e9d8621d3eda62ae44927c4024f65
resids_chunks: 5..170/451..767
atom_names_hash: 3dc465a98d9ee7254717491b7922df92df8d8f5e05eaaaed4a0b826c
selection_string: chain H and resi 5-170+451-767

name: 5lcw
filename: data/5lcw.pdb
chain: W
nres: 25
natoms: 213
seq_hash: 5bb6443300b079605ab05233e8dc4bdae7cb8eda6283e6b31eb71b29
resids_chunks: 1..25
atom_names_hash: 9f45fbbf797dc8ec13b67f7b1e3298fb091ee9281a2d3183b298c7c2
selection_string: chain W and resi 1-25

name: 5lcw
filename: data/5lcw.pdb
n_polypeptidic_chains: 5
polypeptidic_chain_names: E,F,G,H,W
n_non_polypeptidic_chains: 0
non_polypeptidic_chain_names: 
symmetry: 
+ G
+ =W (RMSD=0.95Å, θx=-131.46°, θy=-41.19°, θz=-97.49°, tx=315.93Å, ty=422.42Å, tz=243.46Å) 
unique_chains: E,F,G,H
fasta:
+ >Chain E
+ RFLCESVFSYQVASTLKQVKHDQQVARMEKLAGLVEELEADEWRFKPIEQLLGFTP
+ >Chains F H
+ QEPVQAAIWQALNHYAYRDAVFLAERLYAEVHSEEALFLLATCYYRSGKAYKAYRLLKGHSCTTPQCKYLLAKCCVDLSK
+ LAEGEQILSGGVFNKQKSHDDIVTEFGDSACFTLSLLGHVYCKTDRLAKGSECYQKSLSLNPFLWSPFESLCEIGEKPDP
+ DQTFKFAFNLQKAAAEGLMSLLREMGKGYLALCSYNCKEAINILSHLPSHHYNTGWVLCQIGRAYFELSEYMQAERIFSE
+ VRRIENYRVEGMEIYSTTLWHLQKDVALSVLSKDLTDMDKNSPEAWCAAGNCFSLQREHDIAIKFFQRAIQVDPNYAYAY
+ TLLGHEFVLTEELDKALACFRNAIRVNPRHYNAWYGLGMIYYKQEKFSLAEMHFQKALDINPQSSVLLCHIGVVQHALKK
+ SEKALDTLNKAIVIDPKNPLCKFHRASVLFANEKYKSALQELEELKQIVPKESLVYFLIGKVYKKLGQTHLALMNFSWAM
+ DLD
+ >Chains G W
+ MLRRKPTRLELKLDDIEEFENIRKD

nres: 1072
natoms: 8578
coords_min: 81.228 134.165 110.565
coords_max: 170.09 249.44 253.405
box_size: 88.862 115.27501 142.84
```
