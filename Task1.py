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
import heapq;
import time;


Seed=random.seed(2315); 
path=os.path.abspath(os.getcwd())+"/user-ct-test-collection-01.txt";
data = pd.read_csv(path, sep="\t");
urllist = data.ClickURL.dropna().unique()
print(len(urllist))
# print(type(urllist));
def MinHash(x,m,R,SEED):
    Set=set();
    for i in range(len(x)-2):
        Set.add(x[i:i+3]);
        
    minHash=[];
    for i in range(m):
        min=sys.maxsize;
        for val in Set:
            temp=murmurhash3_32(val,200+i+SEED) % R;
            if temp<min:
                min=temp;

        minHash.append(min);
        
    return minHash;

def threeGram(x):
    Set=set();
    for i in range(len(x)-2):
        Set.add(x[i:i+3]);

    return Set;

class HashTable():
    def __init__(self,K,L,B,R):
        self.K=K;
        self.L=L;
        self.B=B;
        self.R=R;
        self.UniHash=[];
        self.Table=[];
        self.c=[];
        for i in range(L):
            temp=[];
            for j in range(K):
                temp.append(random.randint(1,10000));
            self.UniHash.append(temp);
            self.c.append(random.randint(1,10000));

        for i in range(L):
            self.Table.append([]);
            for j in range(self.B):
                self.Table[i].append([]);

    def insert(self,hashcodes,id):
        for i in range(self.L):
            idx=(np.sum(np.array(hashcodes[i])*np.array(self.UniHash[i]))+self.c[i]) % self.B;
            self.Table[i][idx].append(id);
    
    def lookup(self,hashcodes):
        ansSet=set();
        for i in range(self.L):
            idx=(np.sum(np.array(hashcodes[i])*np.array(self.UniHash[i]))+self.c[i]) % self.B;
            retList=self.Table[i][idx];
            for s in retList:
                ansSet.add(s);
        return ansSet;

minHashobj=HashTable(2,50,64,1048576);
# randseed=random.randint(1,10000);
randseed=range(40,10000,100)
for s in urllist:
    mincodes=[];
    for i in range(50):
        mincodes.append(MinHash(s,2,1048576,randseed[i]));
    minHashobj.insert(mincodes,s);


sample=[];
for i in range(200):
    sample.append(random.choice(urllist));

# print(sample);
start=time.time();
# AverageJaccard=[];
for s in sample:
    mincodes=[];
    for i in range(50):
        mincodes.append(MinHash(s,2,1048576,randseed[i]));
    lookupResults=minHashobj.lookup(mincodes);
    retrievedUrls=set();
    queryUrl=threeGram(s);
    sum=0;
    heap=[];
    heapq.heapify(heap);
    for l in lookupResults:
        retrievedUrl=threeGram(l);
        Jac=len(retrievedUrl.intersection(queryUrl))/len(retrievedUrl.union(queryUrl));
        sum=sum+Jac;
        if(len(heap)<10):
            heapq.heappush(heap,(Jac,l));
        elif(Jac>heap[0][0]):
            heapq.heappop(heap);
            heapq.heappush(heap,(Jac,l));
        # print(heap);
    all_mean=(sum/len(lookupResults));
    Top10=0;
    n=len(heap);
    Top10_Query=[];
    for i in range(len(heap)):
        jac,s=heapq.heappop(heap);
        Top10_Query.append(s);
        Top10=Top10+jac;

    
    Top10=Top10/n;
    print("Mean Value of Top10=",Top10,"Mean Value of all elements=",all_mean);

end=time.time();
print(end-start);


    