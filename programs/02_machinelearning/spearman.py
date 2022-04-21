#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:55:04 2020

@author: armandayuu
"""

import os
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import csv

#图像特征
image_feature = pd.read_csv("/Path of your feature.csv/", header=0, index_col=0)
#imgf = DataFrame(image_feature)
#image_feature.head()

#图像特征名称
featurename = list(image_feature.columns.values)
#print(featurename)

#gene信息
gene_exp = pd.read_csv("/Path of your gene.csv/", header=0, index_col=0)
#geneinfo = DataFrame(gene_exp) 
#gene_exp.head()
#partgene_exp = gene_exp[0:50]

#gene名称
genecase = list(gene_exp.index.values)
#print(genecase)

#新建表格
#result = pd.DataFrame(index=(genecase),columns=(featurename))
result = pd.DataFrame(columns=(featurename))
#result.to_csv("/Users/armandayuu/Desktop/result/result.csv")

#计算pearson，基因行对特征列
for gene_name in range(len(genecase)):
    geneseries = pd.Series(gene_exp.iloc[gene_name])
    geneinfo = geneseries.values
    #print(geneinfo)
    for fea_name in featurename:
        imgseries = pd.Series(image_feature[fea_name])
        imginfo = imgseries.values
        data1 = pd.Series(geneinfo)
        data2 = pd.Series(imginfo)
        ppp = data1.corr(data2,method="spearman")
        result.loc[gene_name,fea_name] = ppp
        
#修改表格index
print(result.index)
result.index = Series(genecase)
result.to_csv("/save spearman coefficients.csv/")
        #ppp = data1.corr(data2, method="pearson"), index=(genecase), columns=(featurename)
    #print(ppp)


#spearman>0.5
data = pd.read_csv("/read the path of spearman coefficients.csv/", header=0, index_col=0)
data1 = abs(data)
data1.head()

featurename = list(data1.columns.values)
genename = list(data1.index.values)
result = pd.DataFrame(columns=(featurename),index=(genename))


"""
for gena in genename:
    print(gena)
    for fena in featurename:
        ppp = data1.loc[gena,fena]
        if ppp > 0.5 :
            print(fena)
           # print(fename)
"""           
for fena in featurename:
    #print(fena)
    for gena in genename:
        ppp = data1.loc[gena,fena]
        if ppp >= 0.5:
            #print(gena)
            result.loc[gena,fena]=gena
            print(fena)
            
            
result.to_csv("/spearman>0.5.csv/")