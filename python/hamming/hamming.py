# calculate Hamming distance
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        hamming_distance = 0
        for dna_a, dna_b in zip(strand_a, strand_b):
            if dna_a != dna_b:
                hamming_distance += 1
        return hamming_distance
