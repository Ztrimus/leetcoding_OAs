'''
-----------------------------------------------------------------------
File: q1_TFIDF.py
Creation Time: Nov 7th 2023 2:56 pm
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''
import numpy as np
import nltk
import math
from nltk.tokenize import word_tokenize

class TFIDF:

    def term_frequency(self, term, sentence):
        # please use nltk.word_tokenize
        words = word_tokenize(sentence.lower())
        term_count = words.count(term.lower())
        max_term_count = max(words, key=words.count)
        
        if term_count > 0:
            return 0.5 + 0.5 * (term_count / words.count(max_term_count))
        else:
            return 0


    def inverse_document_frequency(self, term, corpus):
        # please use nltk.word_tokenize
        term_appearances = sum(1 for sentence in corpus if term.lower() in word_tokenize(sentence.lower()))
        if term_appearances > 0:
            N = len(corpus)
            return math.log(N / term_appearances)
        else:
            return 0

    def tfidf(self, term, sentence, corpus):
        tf = self.term_frequency(term, sentence)
        idf = self.inverse_document_frequency(term, corpus)
        return tf * idf