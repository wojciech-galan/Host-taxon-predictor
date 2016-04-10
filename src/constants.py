#! /usr/bin/python
# -*- coding: utf-8 -*-

import os.path
__author__="wojtek"
__date__ ="$2012-08-20 09:26:10$"

import os

searchURL  = 'http://www.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
fetchURL  = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'

parser_classes_dir = './parser_classes/'
temp_dir='../temp_fetched_data/'
res_dir='../fetched_data/'
seq_dir = '../sequences/'
tax_dir='../taxonomy/'
pars_err_dir='../errors'
bad_hosts_path = '../bad_host'
database_path='..%sdatabases%s' %( os.sep, os.sep )
containers_path='..%scontainers%s' %( os.sep, os.sep )

strange_orgname='dziwna budowa orgname w tym pliku'

acid_to_number = {'dna':1.0, 'rna':0.0}
strands_to_number = {'ss':1.0, 'ds':2.0, 'mixed':1.5}

NA_IUPAC = {'A':('A',), 'C':('C',), 'G':('G',), 'T':('T',),
            'R':('A','G'), 'Y':('C','T'), 'M':('A','C'), 'K':('G','T'),
            'S':('C','G'), 'W':('A','T'), 'B':('C','G','T'), 'D':('A','G','T'),
            'H':('A','C','T'), 'V':('A','C','G'), 'N':('A','C','G','T')}

AA_IUPAC = {'A':('A',), 'C':('C',), 'D':('D',), 'E':('E',), 'F':('F',),
            'G':('G',), 'H':('H',), 'I':('I',), 'K':('K',), 'L':('L',),
            'M':('M',), 'N':('N',), 'P':('P',), 'Q':('Q',), 'R':('R',),
            'S':('S',), 'T':('T',), 'V':('V',), 'W':('W',), 'Y':('Y',),
            '_':('_',), 'B':('D','N'), 'Z':('E','Q'),
            'X':('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')}

transcription_dict={'A':'T', 'C':'G', 'G':'C', 'T':'A', 'U':'A', 'R':'Y',
                    'Y':'R', 'N':'N', 'M':'K', 'K':'M', 'S':'W', 'W':'S',
                    'B':'V', 'V':'B', 'D':'H', 'H':'D'}

stop_code = '_'
any_codon_code = 'x'

#zdefiniowane w razie potrzeby dzielenia przez zero - co zwrócić
RSCU_ZERO = 0
CAI_ZERO = 0