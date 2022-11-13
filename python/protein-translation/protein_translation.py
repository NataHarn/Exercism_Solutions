CA_Map = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 
          'UUC': 'Phenylalanine', 'UUA': 'Leucine',
          'UUG': 'Leucine', 'UCU': 'Serine',
          'UCC': 'Serine', 'UCA': 'Serine',
          'UCG': 'Serine', 'UAU': 'Tyrosine',
          'UAC': 'Tyrosine', 'UGU': 'Cysteine',
          'UGC': 'Cysteine', 'UGG': 'Tryptophan',
          'UAA': 'STOP', 'UAG': 'STOP',
          'UGA': 'STOP'}
          
def proteins(strand):
    codons = [strand[idx:idx+3] for idx in range(0,len(strand), 3)]
    proteins = []
    for codon in codons:
        protein = CA_Map[codon]
        if protein != 'STOP':
            proteins.append(protein)
        else:
            break
    return proteins
