# -*- coding: utf-8 -*-
'''
Created on Dec 11, 2015

@author: v-shayi
'''
class FilterCandidate:
    def filter_all(self, elements, freq=1, solidation=0, right_entro=0, left_entro=0):
        result_elements = []
        for element in elements:
            if element['freq']>freq and element['solidation']>solidation and element['right_entro']>right_entro and element['left_entro']>left_entro:
                result_elements.append(element)
            
        return result_elements
