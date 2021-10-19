import Bio.PDB.PDBParser as PDBParser
import urllib.request
import io
import numpy as np

pdbId = input("Įverskite PDB failo id: (1zaa) ")

# Default to 1zaa
if len(pdbId) == 0:
    pdbId = "1zaa"

url = "https://files.rcsb.org/download/{}.pdb".format(
    pdbId
)

# Attempt to fetch pdb with provided id from rcsb
with urllib.request.urlopen(url) as response:
    if response.code != 200:
        print("Toks PDB id neegzistuoja")
        exit(1)

    # Parse pdb file ATOM records
    pdbInMemoryFile = io.BytesIO(response.read())

    # atoms = np.array()
    while True:
        line = pdbInMemoryFile.readline().decode("utf-8")
        if line.startswith("ATOM"):

            # https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html#:~:text=X%20orthogonal%20%C3%85%20coordinate
            x, y, z = float(line[30:38]), float(line[38:46]), float(line[46:54])

        # Break loop once all lines are read
        if line == "":
            pdbInMemoryFile.close()
            break

    # Calculate distances of atoms

    # Output the histogram image


class Atom:
    x, y, z = 0, 0, 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


