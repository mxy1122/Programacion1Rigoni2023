def mutant(dna):
    sequences = []
    rows = len(dna)
    cols = len(dna[0])
    for i in range(rows):
        sequences.append("".join(dna[i])) 
        sequences.append("".join(dna[j][i] for j in range(cols))) 
    for i in range(rows - 3):
        for j in range(cols - 3):
            sequences.append("".join(dna[i + k][j + k] for k in range(4)))  
            sequences.append("".join(dna[i + 3 - k][j + k] for k in range(4)))  
    return any(sequence in {"AAAA", "TTTT", "CCCC", "GGGG"} for sequence in sequences)
def get_dna():
    while True:
        sequence = input("Ingrese la secuencia de ADN (solo puede tener las letras A, T, C y G y tener una longitud de 6): ").upper()
        if all(base in "ATCG" for base in sequence) and len(sequence) == 6:
            return sequence
        else:
            print("La secuencia de ADN ingresada no es válida. pruebe de nuevo.")
dna = [get_dna() for _ in range(6)]
if mutant(dna):
    print("Es mutante.")
else:
    print("No es mutante.")
