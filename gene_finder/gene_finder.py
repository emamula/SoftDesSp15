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

    result = ''
    
    for x in range(0,n):
        result = get_complement(dna[x]) + result

    return result
    


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

    result = ''

    for x in range(0,n):
        if (x%3) == 0 and dna[x:x+3] in ['TGA', 'TAA', 'TAG']:
            break
        result = result + dna[x]

    return result


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
    n = len(dna)

    result = []

    while x < n:
        if (x%3) == 0 and dna[x:x+3] == 'ATG':
            result.append(rest_of_ORF(dna[x:n]))
            x += len(rest_of_ORF(dna[x:n]))
        else:
            x += 1

    return result
            

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
    n = len(dna) #3
    x = 0
    y = 0
    z = 0

    result = []
    frame1 = find_all_ORFs_oneframe(dna[0:n])
    n1 = len(frame1)
    frame2 = find_all_ORFs_oneframe(dna[1:n])
    n2 = len(frame2)
    frame3 = find_all_ORFs_oneframe(dna[2:n])
    n3 = len(frame3)

    for x in range(0,n1):
        if (frame1[x]) != '':
            result.append(frame1[x])
    
    for y in range(0,n2):
        if (frame2[y]) != '':
            result.append(frame2[y])
    
    for z in range(0,n3):
        if (frame3) != '':
            result.append(frame3[z])

    return result


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this
    result = []
    x = 0
    y = 0
    n = len(dna)
    dna_complement = get_reverse_complement(dna[0:n])
    #print(dna_complement)
    
    dna_ORFs = find_all_ORFs(dna[0:n])
    #print(dna_ORFs) 

    dna_complement_ORFs = find_all_ORFs(dna_complement[0:n])
    #print(dna_complement_ORFs)

    n1 = len(dna_ORFs)
    n2 = len(dna_complement_ORFs)

    for x in range(0,n1):
        result.append(dna_ORFs[x])

    for y in range(0,n2):
        result.append(dna_complement_ORFs[y])

    '''for x in range(0,n):
        if dna[x:x+3] == 'ATG':
            result.append(rest_of_ORF(dna[x:n]))
        if dna_complement[x:x+3] == 'ATG':
            result.append(rest_of_ORF(dna_complement[x:n]))'''

    return result


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
    result = [all_ORFs[0]]

    for x in range(1,n):
        if len(result[0]) == len(all_ORFs[x]):
            result.append(all_ORFs[x])
        if len(result[0]) < len(all_ORFs[x]):
            result = [all_ORFs[x]]

    if len(result) == 1:
        return result[0]
    else:
        return result

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    x = 0
    shuff = ''
    l = list(dna)
    longest_round = 0
    result = 0

    for x in range (0,num_trials):
        random.shuffle(l)
        shuff = ''.join(l)
        longest_round = len(longest_ORF(shuff))
        if longest_round > result:
            result = longest_round

    return result
    

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
    n = len(dna)
    x = 0
    amino_acids = ''
    extras = len(dna)%3

    for x in range(0,(n-extras),3):
        amino_acids += aa_table[dna[x:x+3]]

    return amino_acids


def gene_finder(dna,threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # TODO: implement this
    threshold = longest_ORF_noncoding(dna,1500)
    result = []
    x = 0

    all_ORFs = find_all_ORFs_both_strands(dna)
    n = len(all_ORFs)

    for x in range(0,n):
        if len(all_ORFs[x]) > threshold:
            result.append(coding_strand_to_AA(all_ORFs[x]))

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()