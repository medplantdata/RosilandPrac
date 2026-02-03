aa_mass = {
    "A": 89.0,   # Alanine
    "R": 174.0,  # Arginine
    "N": 132.0,  # Asparagine
    "D": 133.0,  # Aspartic acid
    "C": 121.0,  # Cysteine
    "Q": 146.0,  # Glutamine
    "E": 147.0,  # Glutamic acid
    "G": 75.0,   # Glycine
    "H": 155.0,  # Histidine
    "I": 131.0,  # Isoleucine
    "L": 131.0,  # Leucine
    "K": 146.0,  # Lysine
    "M": 149.0,  # Methionine
    "F": 165.0,  # Phenylalanine
    "P": 115.0,  # Proline
    "S": 105.0,  # Serine
    "T": 119.0,  # Threonine
    "W": 204.0,  # Tryptophan
    "Y": 181.0,  # Tyrosine
    "V": 117.0,  # Valine
    "B": 133.0,  # Asx (Asn/Asp average)
    "Z": 147.0   # Glx (Gln/Glu average)
}

protSeq = 'SKADYEK' 
massTot = 0
for prot in protSeq:
    mass = aa_mass.get(prot)
    massTot += mass

print(massTot)