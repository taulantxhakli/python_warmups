# Two function for the user to input that allows
# the user to see either see the first substring for 'ATG'
# or
# to input nucleotide and output first protein
# Functions are firstProtein(inputSequence) & DNA()
#
# @author Taulant Xhakli
# @version 1.0
import itertools

print("Choose your function: ")
print("firstProtein(inputSequence) || DNA()")

# DNA codon table
dict = {"TTT": "Phe", "TCT": "Ser", "TAT": "Tyr", "TGT": "Cys",
        "TTC": "Phe", "TCC": "Ser", "TAC": "Tyr", "TGC": "Cys",
        "TTA": "Leu", "TCA": "Ser", "TAA": "STOP", "TGA": "STOP",
        "TTG": "Leu", "TCG": "Ser", "TAG": "STOP", "CGT": "Trp",
        "CTT": "Leu", "CCT": "Pro", "CAT": "His", "CGC": "Arg",
        "CTC": "Leu", "CCC": "Pro", "CAC": "His", "CGC": "Arg",
        "CTA": "Leu", "CCA": "Pro", "CAA": "Gln", "CGA": "Arg",
        "CTG": "Leu", "CCG": "Pro", "CAG": "Gln", "CGG": "Arg",
        "ATT": "Ile", "ACT": "Thr", "AAT": "Asn", "AGT": "Ser",
        "ATC": "Ile", "ACC": "Thr", "AAC": "Asn", "AGC": "Ser",
        "ATA": "Ile", "ACA": "Thr", "AAA": "Lys", "AGA": "Arg",
        "ATG": "Met", "ACG": "Thr", "AAG": "Lys", "AGG": "Arg",
        "GTT": "Val", "GCT": "Ala", "GAT": "Asp", "GGT": "Gly",
        "GTC": "Val", "GCC": "Ala", "GAC": "Asp", "GGC": "Gly",
        "GTA": "Val", "GCA": "Ala", "GAA": "Glu", "GGA": "Gly",
        "GTC": "Val", "GCG": "Ala", "GAG": "Glu", "GGG": "Gly"}

inputSequence = "ATG"
def firstProtein(inputSequence):
    codon = ""
    
    for i in range(0, len(inputSequence)-(3+len(inputSequence)%3), 3):
        codon += dict[inputSequence[i:i+3]]

    print(codon)

def DNA():
    dna = input ("Enter nucleotide string: ")
    protein_sequence = ""

    minGene = 3
    lastStop = 0
    start = 0
    stop = 0

    while start != -1:
        # find first ATG after lastStop
        start = dna.find("ATG", lastStop)

        # find first STOP codon
        for i in range(start, len(dna), 3):
            codon = dna[i:i+3]
            if codon in["TAA", "TGA", "TAG"]:
                stop = i + 2
                break

            if stop - start >= minGene:
                lastStop = stop + 1
            else:
                lastStop = start + 1

                protein_sequence += dict[codon] + " "
    print("Protein Sequence: ", (protein_sequence))
