# -*- coding: utf-8 -*-
'''
Created on Dec 16, 2015

@author: v-shayi
'''
import re

class prefilter(object):

    def filter(self, src_file):
        with open(src_file, 'r') as fs:
            data = fs.read().decode('utf-8')
        
            data = re.sub('[a-zA-Z.<>\[\]]+', '', data)
            data = re.sub(u'[0-9：；‘’”“，。？（）、·=_:;,\'\"\-\(\)]+', '\n', data)
        
        with open(src_file, 'w') as fw:
            fw.write(data.encode('utf-8'))
            