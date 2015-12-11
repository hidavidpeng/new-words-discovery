# -*- coding: utf-8 -*-
import argparse, re
from collections import Counter
import logging
from logging import NullHandler

class CandidateFreq:
    def __init__(self):
        logging.basicConfig()
        self.logger = logging.getLogger('CandidateFreq')
        self.logger.setLevel(logging.INFO)
    
    ''' Compute frequency of candidate words.
        @param: src_file: path to the file
        @param: reverse: default set as false
        @return: Dictionary with key of words and value of frequency
    '''
    def compute(self, src_file, reverse=False):
        with open(src_file, 'r') as fs:
            freq = Counter()
            freq_update = freq.update
            self.logger.info('Success reading file: ' + src_file)
        
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
            result_dict.update({key: value})
            
        self.logger.info('Result candidate frequency: ' + str(result_dict))
        return result_dict


    ''' Filter frequency of candidate words.
        @param: freq_limit: min freq
        @param: minLen: min word length, default=2
        @param: maxLen: max word length, default=4 
        @return: Dictionary with key of words and value of frequency
    '''
    def filter(self, result_dict, freq_limit, minLen=2, maxLen=4):
        if not result_dict:
            self.logger.error('No result dictionary initialized')
            return
        
        tmp_dict = {}
        for key, value in result_dict.iteritems():
            if len(key)>=minLen and len(key)<=maxLen and value>=freq_limit:
                tmp_dict.update({key: value})
        result_dict = tmp_dict
        self.logger.info('Filtered candidates: ' + str(result_dict))
        return result_dict