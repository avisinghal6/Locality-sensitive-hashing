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
from sympy import Min;
import heapq


J=np.linspace(0,1,1000);
L=50;
K=[1,2,3,4,5,6,7];
color=['r','b','g','y','m','c','pink'];
count=0;
plt.figure();
plt.xlabel("Jaccard Similarity");
plt.ylabel("Probability of Retrieval");
for k in K:
    P=[]
    for j in J:
        p=1-(1-j**k)**L;
        P.append(p);

    plt.scatter(J,P,c=color[count],label=K[count]);
    count=count+1;
plt.legend(loc="lower right")

L=[5,10,20,50,100,150,200];
K=4;
count=0;
plt.figure();
for l in L:
    P=[]
    for j in J:
        p=1-(1-j**K)**l;
        P.append(p);

    plt.scatter(J,P,c=color[count],label=L[count]);
    count=count+1;

plt.legend(loc="lower right")
plt.show();
