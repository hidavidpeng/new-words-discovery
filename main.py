#-- ecoding:utf-8 --
'''
Created on Dec 10, 2015

@author: v-shayi
'''
from Computation.compute_candidate_freq import CandidateFreq
from Computation.compute_solidation import Solidation

if __name__ == '__main__':
    path = '//spg-share/root/Users/v-shayi/Pig_Raising/Dataset/TestSet/_hangqing_zoushi_3.html.txt'
    
    candidate = CandidateFreq()
    r1 = candidate.compute(path)
    print r1.encode()
    r2 = candidate.filter(2)
    print r2
    sol = Solidation()
    r3 = sol.compute(r2, 2)
    print r3
    
    