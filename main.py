#-- ecoding:utf-8 --
'''
Created on Dec 10, 2015

@author: v-shayi
'''
from os import listdir
from os.path import isfile, join, basename

from Computation.compute_candidate_freq import CandidateFreq
from Computation.compute_solidation import Solidation
from Computation.compute_freedegree import Entropy
from Operation.filter import FilterCandidate
from Operation.PreFilter import prefilter

def discover(path):
    prefilter().filter(path)
    
    rFreq = CandidateFreq().compute(path)
    rFreqRev = CandidateFreq().compute(path, reverse=True)
    rFreqFil = CandidateFreq().filter(rFreq, 1)
    
    rSol = Solidation().compute(rFreqFil, 2)
    
    rEntroRight = Entropy().compute(rFreq)
    rEntroLeft = Entropy().compute(rFreqRev, reverse=True)
    
    elements = []
    for k in rFreq:
        if any(char.isdigit() for char in k):
            continue
        element = {'word': k, 'freq': rFreq.get(k), 'solidation': rSol.get(k), 'right_entro': rEntroRight.get(k), 'left_entro': rEntroLeft.get(k)}
        elements.append(element)
    print elements
    elements = FilterCandidate().filter_all(elements)
    
    file_name = basename(path)
    with open('//spg-share/root/Users/v-shayi/Pig_Raising/Dataset/TestSet/Test20151217/result/%s' % file_name, 'w') as fd:
        for element in elements:
            try:
                fd.writelines('%s\t%d\t%.9f\t%.9f\t%.9f\n' % (element['word'].encode('utf-8'), element['freq'], element['solidation'], 
                                                              element['right_entro'], element['left_entro']))
            except Exception as e:
                print 'Drop item: ' + str(element)

if __name__ == '__main__':
    pathDir = '//spg-share/root/Users/v-shayi/Pig_Raising/Dataset/TestSet/Test20151217/'
    fileList = [f for f in listdir(pathDir) if isfile(join(pathDir, f))]
    for file in fileList:
        discover(pathDir + file)