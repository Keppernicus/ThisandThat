"""
Simple RNA translation function.
not crazy about the auto-formatting, so I left it as a too-long list comp
"""

def to_rna(dna_strand):
    rna = ''.join(['C' if char == 'G' else 'G' if char == 'C' else 'A' if char == 'T' else 'U' if char == 'A' else char for char in dna_strand])
    return rna
        
print(to_rna("ACGTGGTCTTAA"))
