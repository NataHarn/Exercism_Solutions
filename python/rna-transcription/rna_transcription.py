def to_rna(dna_strand):
    pairs = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna_strand = [pairs[seq] for seq in dna_strand]
    return ''.join(rna_strand)