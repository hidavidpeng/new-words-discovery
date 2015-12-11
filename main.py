#-- ecoding:utf-8 --
'''
Created on Dec 10, 2015

@author: v-shayi
'''
from Computation.compute_candidate_freq import CandidateFreq
from Computation.compute_solidation import Solidation
from Computation.compute_freedegree import Entropy

if __name__ == '__main__':
    path = '//spg-share/root/Users/v-shayi/Pig_Raising/Dataset/TestSet/_hangqing_zoushi_3.html.txt'
    
    candidate = CandidateFreq()
    rFreq = candidate.compute(path)
    rFreqRev = candidate.compute(path, reverse=True)
    rFreqFil = candidate.filter(rFreq, 1)
    
    sol = Solidation()
    rSol = sol.compute(rFreqFil, 2)
    
    en = Entropy()
    rEntroRight = en.compute(rFreq)
    rEntroLeft = en.compute(rFreqRev, reverse=True)

    
    elements = []
    for k in rFreq:
        element = {'word': k, 'freq': rFreq.get(k), 'solidation': rSol.get(k), 'right_entro': rEntroRight.get(k), 'left_entro': rEntroLeft.get(k)}
        elements.append(element)
    print elements
    
    with open('//spg-share/root/Users/v-shayi/Pig_Raising/Dataset/TestSet/result.txt', 'w') as fd:
        for element in elements:
            try:
                fd.writelines('%s\t%d\t%.9f\t%.9f\t%.9f\n' % (element['word'].encode('utf-8'), element['freq'], element['solidation'], 
                                                              element['right_entro'], element['left_entro']))
            except Exception as e:
                print 'Drop item: ' + str(element)
