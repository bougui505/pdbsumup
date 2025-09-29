
# pdbsumup

`pdbsumup` is a command-line tool designed to summarize Protein Data Bank (PDB) structures. It provides detailed information on chains, sequences, residue IDs, symmetry, interfaces, and more, making it a useful utility for structural biologists and bioinformaticians.

## Features

*   **PDB/CIF File and ID Support**: Load structures from local files or directly fetch them using PDB IDs.
*   **Chain Information**: Get details on polypeptide and non-polypeptide chains.
*   **Sequence Analysis**: Extract and print amino acid sequences, unique sequences in FASTA format, and sequence identity matrices.
*   **Residue Information**: List residue IDs, identify missing residues or alternative locations, and output residue ID chunks.
*   **Symmetry Detection**: Identify symmetrical chains based on sequence and atom count, including RMSD and transformation details.
*   **Structural Metrics**: Calculate bounding box, center of coordinates, and recenter the structure based on principal axes.
*   **Interactions**: Generate chain-chain interface contact maps.
*   **Visualization**: Display images of PDB entries from rcsb.org for quick visual inspection.

## Installation

`pdbsumup` requires several Python packages. It is recommended to install it in a virtual environment.

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone https://github.com/your-repo/pdbsumup.git
    cd pdbsumup
    ```
    *(Note: Replace `https://github.com/your-repo/pdbsumup.git` with the actual repository URL)*

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: PyMOL (pymol-open-source) can be challenging to install. Ensure you have the necessary system dependencies or consider installing it separately if `pip` fails. For more detailed PyMOL installation instructions, refer to the official PyMOL documentation.*

## Usage

Run `pdbsumup.py` from the command line, providing a PDB file path or a PDB ID as an argument.

```bash
python pdbsumup.py --help
```

### Basic Example

To get a general summary of a PDB ID:

```bash
python pdbsumup.py 1kv1
```

Or for a local file:

```bash
python pdbsumup.py data/4ci0.pdb
```

### Common Options

*   **Print Sequence (`-s` or `--seq`):**
    ```bash
    python pdbsumup.py 1kv1 -s
    ```

*   **Print Residue IDs (`-r` or `--resids`):**
    ```bash
    python pdbsumup.py 1kv1 -r
    ```

*   **Output FASTA format (`-f` or `--fasta`):**
    ```bash
    python pdbsumup.py 1kv1 -f
    ```

*   **Display PDB image (`--img`):** (Requires a PDB ID, not a local file)
    ```bash
    python pdbsumup.py 1kv1 --img
    ```

*   **Show Symmetry information (`--sym`):**
    ```bash
    python pdbsumup.py 4ci0 --sym
    ```

*   **Display Chain-Chain Interfaces (`--inter`):**
    ```bash
    python pdbsumup.py 4ci0 --inter
    ```

*   **Align Sequences and get Identity Matrix (`--aln`):**
    ```bash
    python pdbsumup.py 4ci0 --aln
    ```

*   **Select specific parts of the structure (`--select`):**
    ```bash
    python pdbsumup.py 1kv1 --select "chain A" -s
    ```

## Full Options List

```
usage: pdbsumup.py [-h] [--img] [--select SELECT] [-s] [-r] [-sr] [-f] [-rc] [--sym] [--center] [--coords] [--inter] [--aln] PDB

Summarize Protein Data Bank (PDB) structures, providing details on chains, sequences, residue IDs, symmetry, interfaces, and more.

positional arguments:
  PDB                   Path to a PDB/CIF file or a PDB ID (e.g., '1kv1').

options:
  -h, --help            show this help message and exit
  --img                 Display an image of the PDB entry from rcsb.org. Only works if a valid PDB ID is provided.
  --select SELECT       Pymol selection string to filter parts of the structure (e.g., 'chain A').
  -s, --seq             Print the amino acid sequence for each polypeptide chain.
  -r, --resids          Print a semicolon-separated list of residue IDs for each polypeptide chain.
  -sr, --seqres         Print the amino acid sequence along with corresponding residue IDs for each polypeptide chain.
  -f, --fasta           Output unique polypeptide sequences in FASTA format.
  -rc, --resids-per-chain
                        Output unique residue ID lists per chain in a FASTA-like format.
  --sym                 Print symmetry information, including RMSD and transformation details for identical chains.
  --center              Recenter the structure coordinates based on its principal axes of inertia.
  --coords              Print the XYZ coordinates of all atoms in the structure.
  --inter               Display a contact map indicating interfaces between polypeptide chains.
  --aln                 Display a pairwise sequence identity matrix for all polypeptide chains.
```

## Author

Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
https://research.pasteur.fr/en/member/guillaume-bouvier/
