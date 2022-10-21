import csv
from tokenize import String
from typing import List
import pandas as pd
import random;
import os;
from sklearn.utils import murmurhash3_32;
# import mmh3;
import numpy as np;
from bitarray import bitarray
import math;
import string;
import matplotlib.pyplot as plt;
import sys
import statistics
from sympy import Min
from torch import positive;

Seed=random.seed(2315); 

def MinHash(x,m):
    Set=set();
    for i in range(len(x)-2):
        Set.add(x[i:i+3]);
    
    minHash=[];
    for i in range(m):
        min=sys.maxsize;
        for val in Set:
            temp=murmurhash3_32(val,200+i,positive=True);
            # print(temp)
            if temp<min:
                min=temp;

        minHash.append(min);
    
    return (minHash,Set);


S1 = "The mission statement of the WCSCC and area employers recognize the importance of good attendance on the job. Any student whose absences exceed 18 days is jeopardizing their opportunity for advanced placement as well as hindering his/her likelihood for successfully completing their program";
S2 = "The WCSCC’s mission statement and surrounding employers recognize the importance of great attendance. Any student who is absent more than 18 days will loose the opportunity for successfully completing their trade program";

minHash_S1,setS1=MinHash(S1,100);
minHash_S2,setS2=MinHash(S2,100);
# print(len(setS1))
Jaccard= len(setS1.intersection(setS2))/len(setS1.union(setS2));

count=[i for i, j in zip(minHash_S1, minHash_S2) if i == j]
# print(len(count));
minHash100=len(count)/100;

print("Similarity from MinHash= ",minHash100," Simililarity from Jaccard= ",Jaccard);