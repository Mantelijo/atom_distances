import urllib.request
import io
import numpy as np
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt
from urllib.error import HTTPError

pdbId = input("Įveskite PDB failo id: (1zaa) ")

# Default to 1zaa
if len(pdbId) == 0:
    pdbId = "1zaa"

pdbId = pdbId.upper()
url = "https://files.rcsb.org/download/{}.pdb".format(
    pdbId
)

response = None
try:
    response = urllib.request.urlopen(url)
except HTTPError as err:
    print(f"Toks PDB id neegzistuoja: HTTP {err.code}")
    exit(1)

# Attempt to fetch pdb with provided id from rcsb
if response.code != 200:
    print("Toks PDB id neegzistuoja")
    exit(1)

# Parse pdb file ATOM records
pdbInMemoryFile = io.BytesIO(response.read())
atoms = []
while True:
    line = pdbInMemoryFile.readline().decode("utf-8")
    if line.startswith("ATOM") or line.startswith("HETATM"):
        # https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html#:~:text=X%20orthogonal%20%C3%85%20coordinate
        x, y, z = float(line[30:38]), float(line[38:46]), float(line[46:54])
        atoms.append([x, y, z])

    # Break loop once all lines are read
    if line == "":
        pdbInMemoryFile.close()
        break
all_atoms = np.array(atoms)
# Calculate distances between atoms
print("Skaičiuojami atstumai")
distances = distance_matrix(all_atoms, all_atoms)

# Remove duplicates and self distances: AA, AB, BA - will leave only BA
print("Šalinami dublikuoti ir nuliniai atstumai")
num_atoms = distances.shape[0]
distances = np.tril(distances)

# Drop zeros
distances = distances.flatten()
distances[distances == 0] = np.nan

print("Baigta!")
# Output the histogram image
plt.hist(distances, edgecolor="#444", linewidth=1.5, color="#aaaa44")
plt.xlabel("Atstumas, Å")
plt.ylabel("Dažnis")
plt.title(f"{pdbId} Atstumų tarp {num_atoms} atomų histograma")

# Save image and display it
plt.savefig(f"{pdbId}.png")
plt.show()

