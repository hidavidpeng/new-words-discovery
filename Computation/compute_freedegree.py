# -*- coding: utf-8 -*-
from __future__ import division
import argparse, math

class Entropy:
    def compute_entropy(self, neighbours):
        if neighbours:
            right_sum = sum(neighbours)
            right_prob = map(lambda x:x/right_sum, neighbours)
            right_entropy = sum(map(lambda x:-(x)*math.log(x), right_prob))
            return right_entropy
        else:
            return 0
        
    ''' Compute entropy of words
        @param: freq: input dictionary of freq list
        @param: direction: right/left entropy, default as right
        @return: entropy dictionary
    '''
    def compute(self, freq, freq_limit=1, minLen=2, maxLen=4, reverse=False):
        words = {word for word, count in freq.iteritems() if 2<=len(word)<=4 and count>=freq_limit}
        right_distribution = {}
        for key, count in freq.iteritems():
            length = len(key)
            if length >= 3 and key[:length-1] in words:
                right_distribution.setdefault(key[:length-1], []).append(count)
            
        entropys = map(lambda x:self.compute_entropy(right_distribution.get(x, None)), words)
        
        result_entro = {}
        if not reverse:
            for (word, entropy) in zip(words, entropys):
                result_entro.update({word: entropy})
            return result_entro
        elif reverse:
            for (word, entropy) in zip(words, entropys):
                result_entro.update({word[::-1]: entropy})
            return result_entro