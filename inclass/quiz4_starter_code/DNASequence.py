class DNASequence(object):
    """ Represents a sequence of DNA """
    def __init__(self, nucleotides):
        """ constructs a DNASequence with the specified nucleotides.
             nucleotides: the nucleotides represented as a string of
                          capital letters consisting of A's, C's, G's, and T's """
        self.seq = nucleotides
 
    def __str__(self):
        """ Returns a string containing the nucleotides in the DNASequence
        >>> seq = DNASequence("TTTGCC")
        >>> print seq
        TTTGCC
        """
        return str(self.seq)

    def get_reverse_complement(self):
        """ Returns the reverse complement DNA sequence represented
            as an object of type DNASequence

            >>> seq = DNASequence("ATGC")
            >>> rev = seq.get_reverse_complement()
            >>> print rev
            GCAT
            >>> print type(rev)
            <class '__main__.DNASequence'>
        """
        x = 0
        rev = ''

        for x in range (0,len(self.seq)):
            if self.seq[x] == 'A':
                rev = 'T' + rev
            if self.seq[x] == 'C':
                rev = 'G' + rev
            if self.seq[x] == 'G':
                rev = 'C' + rev
            if self.seq[x] == 'T':
                rev =  'A' + rev

        return DNASequence(rev)

    def get_proportion_ACGT(self):
        """ Computes the proportion of nucleotides in the DNA sequence
            that are 'A', 'C', 'G', and 'T'
            returns: a dictionary where each key is a nucleotide and the
                corresponding value is the proportion of nucleotides in the
            DNA sequence that are that nucleotide.
            (NOTE: this doctest will not necessarily always pass due to key
                    re-ordering don't worry about matching the order)
        >>> seq = DNASequence("AAGAGCGCTA")
        >>> d = seq.get_proportion_ACGT()
        >>> print (d['A'], d['C'], d['G'], d['T'])
        (0.4, 0.2, 0.3, 0.1)
        """
        x = 0
        props = {'A':0,'C':0,'G':0,'T':0}

        for x in range(0,len(self.seq)):
            if self.seq[x] == 'A':
                props['A'] += 1
            if self.seq[x] == 'C':
                props['C'] += 1
            if self.seq[x] == 'G':
                props['G'] += 1
            if self.seq[x] == 'T':
                props['T'] += 1

        for nucleo in props:
            props[nucleo] = props[nucleo]/float(len(self.seq))

        return props


if __name__ == '__main__':
    import doctest
    doctest.testmod()
