# -*- coding: utf-8 -*-
from __future__ import division
import argparse, math
import logging

class Solidation:
    def __init__(self):
        self.logger = logging.getLogger('Init')
        
    '''Solication of candidate words
        @param: freq: candidate freq list
        @param: freq_limit: min freq to be selected, default = 1 
        @return: result list of solidation
    '''
    def compute(self, freq, freq_limit=1):
        self.result_soli = {}
        
        for word in freq:
            w_freq = freq.get(word, freq_limit)
            length = len(word)
            ninggudu = 0
            if length == 2:
                word1, word2 = word
                ninggudu = w_freq / (freq.get(word1, freq_limit)*freq.get(word2, freq_limit))
            elif length == 3:
                word1, word2 = word[:2], word[2:3]
                ninggudu1 = w_freq / (freq.get(word1, freq_limit)*freq.get(word2, freq_limit))
                word1, word2 = word[:1], word[1:3]
                ninggudu2 = w_freq / (freq.get(word1, freq_limit)*freq.get(word2, freq_limit))
                ninggudu = min(ninggudu1, ninggudu2)
            elif length == 4:
                word1, word2 = word[:1], word[1:4]
                ninggudu1 = w_freq / (freq.get(word1, freq_limit)*freq.get(word2, freq_limit))
                word1, word2 = word[:2], word[2:4]
                ninggudu2 = w_freq / (freq.get(word1, freq_limit)*freq.get(word2, freq_limit))
                word1, word2 = word[:3], word[3:4]
                ninggudu3 = w_freq / (freq.get(word1, freq_limit)*freq.get(word2, freq_limit))
                ninggudu = min(ninggudu1, ninggudu2, ninggudu3)
            self.result_soli.update({word: ninggudu})
            
        self.logger.info('Result solication: ' + str(self.result_soli))
        return self.result_soli
