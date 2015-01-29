# -*- coding: utf-8 -*-
"""
Created on 1/27/15

@author: Emily Mamula

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    # TODO: implement this
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'
    if nucleotide == 'T':
        return 'A'


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # TODO: implement this
    x = 0
    n = len(dna)

    complement = ''
    reverse_complement = ''
    
    for x in range(0,n):
        complement = get_complement(dna[x])
        reverse_complement = complement + reverse_complement

    return reverse_complement
    


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """
    # TODO: implement this
    x = 0
    n = len(dna)

    rest_of_ORF = ''

    '''if dna[3] == 'T':
        return rest_of_ORF'''

    for x in range(0,n):
        if (x%3) == 0 and ((dna[x:x+3] == 'TGA') or (dna[x:x+3] == 'TAA') or (dna[x:x+3] == 'TAG')):
            break
        rest_of_ORF = rest_of_ORF + dna[x]
        x = x + 1

    return rest_of_ORF


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    # TODO: implement this
    x = 0
    y = 0
    n = len(dna)

    find_all_ORFs_oneframe = []

    for x in range(0,n):
        if (x%3) == 0 and dna[x:x+3] == 'ATG':
            find_all_ORFs_oneframe.append(rest_of_ORF(dna[x:n]))

    return find_all_ORFs_oneframe
            

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    # TODO: implement this
    x = 0
    y = 0
    n = len(dna)

    find_all_ORFs = []

    for x in range(0,n):
        if dna[x:x+3] == 'ATG':
            find_all_ORFs.append(rest_of_ORF(dna[x:n]))

    return find_all_ORFs


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT', 'ATG']
    """
    # TODO: implement this
    find_all_ORFs_both_strands = []
    x = 0
    n = len(dna)
    dna_complement = get_reverse_complement(dna)

    for x in range(0,n):
        if dna[x:x+3] == 'ATG':
            find_all_ORFs_both_strands.append(rest_of_ORF(dna[x:n]))
        if dna_complement[x:x+3] == 'ATG':
            find_all_ORFs_both_strands.append(rest_of_ORF(dna_complement[x:n]))

    return find_all_ORFs_both_strands


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    all_ORFs = find_all_ORFs_both_strands(dna)

    x = 0
    n = len(all_ORFs)
    longest_ORF = [all_ORFs[0]]

    for x in range(1,n):
        if len(longest_ORF[0]) == len(all_ORFs[x]):
            longest_ORF.append(all_ORFs[x])
        if len(longest_ORF[0]) < len(all_ORFs[x]):
            longest_ORF = [all_ORFs[x]]

    if len(longest_ORF) == 1:
        return longest_ORF[0]
    else:
        return longest_ORF

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    pass

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # TODO: implement this
    pass
    gene_finder = []
    x = 0

    all_ORFs = find_all_ORFs(dna)
    n = len(all_ORFs)

    for x in range(0,n):
        if len(all_ORFs[x]) > threshold:
            #DO AMINO ACIDS
            gene_finder.append('Amino acids')

    print gene_finder

if __name__ == "__main__":
    import doctest
    doctest.testmod()