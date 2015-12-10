# -*- coding: utf-8 -*-
import argparse, re
from collections import Counter

class CandidateFreq:
    ''' Compute frequency of candidate words.
        @param: src_file: path to the file, reverse default set as false
        @return: Dictionary with key of words and value of frequency
    '''
    def compute(self, src_file, reverse=False):
        with open(src_file, 'r') as fs:
            freq = Counter()
            freq_update = freq.update
        if not fs:
            self.logger.info('Error reading file: ' + src_file)
            return
        
        re_chinese = re.compile(u'[^a-zA-Z0-9\u4e00-\u9fa5]+')
        for line in fs:
            sentence = re_chinese.sub('', line.decode('utf-8').rstrip())
            sentence = sentence if not reverse else sentence[::-1]
            sen_len = len(sentence)
            freq_update(sentence[i:i+1] for i in xrange(sen_len-1, -1, -1))
            freq_update(sentence[i:i+2] for i in xrange(sen_len-2, -1, -1))
            freq_update(sentence[i:i+3] for i in xrange(sen_len-3, -1, -1))
            freq_update(sentence[i:i+4] for i in xrange(sen_len-4, -1, -1))
            freq_update(sentence[i:i+5] for i in xrange(sen_len-5, -1, -1))

        result_dict = {}
        for key, value in freq.iteritems():
            result_dict.update(key, value)
            
        self.logger.info('Result candidate frequency: ' + str(result_dict))
