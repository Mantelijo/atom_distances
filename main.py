import Bio.PDB.PDBParser as PDBParser
import urllib.request

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
    pdbInMemoryFile = response.read()
    # print(type(pdbInMemoryFile))

    # Parse pdb file
    # parser = PDBParser()
    # struct = parser.get_structure(id=pdbId, file=pdbInMemoryFile)
    # print(type(struct))
    # print("test")
    # Calculate distances of atoms

    # Output the histogram image
