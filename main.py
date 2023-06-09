import os
import numpy as np
from nltk.stem.porter import*
import pandas as pd
import math


#Listing name of subdirectories in dataset
subdirec_List=os.listdir('/dataset')
print(subdirec_List)

#Listing files in each subdirectories(using jagged list)
textfile_List=[]
for i in range (len(subdirec_List)):
        textfile_List.append([])
        textfile_List[i]=os.listdir('/dataset/'+subdirec_List[i])

wd_alt =[]
wd_comp=[]
wd_rec =[]
wd_soc=[]
wd_talk=[]

#Open and read files in each subdirectories
for i in range (len(subdirec_List)):
        for j in textfile_List[i]:
                if(i==0):
                        f=open('/dataset/'+subdirec_List[i]+'/'+j,'r',encoding='Latin1')
                        r = f.read()
                        wd_alt.append(re.split('[^a-zA-Z]+', r))
                elif(i==1):
                        f = open('/dataset/' + subdirec_List[i] + '/' + j, 'r', encoding='Latin1')
                        r = f.read()
                        wd_comp.append(re.split('[^a-zA-Z]+', r))
                elif(i==2):
                        f = open('/dataset/' + subdirec_List[i] + '/' + j, 'r', encoding='Latin1')
                        r = f.read()
                        wd_rec.append(re.split('[^a-zA-Z]+', r))
                elif(i==3):
                        f = open('/dataset/' + subdirec_List[i] + '/' + j, 'r', encoding='Latin1')
                        r = f.read()
                        wd_soc.append(re.split('[^a-zA-Z]+', r))
                else:
                        f = open('/dataset/' + subdirec_List[i] + '/' + j, 'r', encoding='Latin1')
                        r = f.read()
                        wd_talk.append(re.split('[^a-zA-Z]+', r))

#save stopwords in the list
sw = open('/stopwords.txt','r',encoding='Latin1')
stopword=sw.read().splitlines()

#print(wd_alt[0])
#print(wd_soc[0])

#removing ''empty space if exist
#for alt.atheism
for i in range (len(wd_alt)):
    for j in wd_alt[i]:
        if (j==''):
            wd_alt[i].remove(j)
#for comp.graphics
for i in range (len(wd_comp)):
    for j in wd_comp[i]:
        if (j==''):
            wd_comp[i].remove(j)
#for rec.motorcycles
for i in range (len(wd_rec)):
    for j in wd_rec[i]:
        if (j==''):
            wd_rec[i].remove(j)
#for soc.religion.christian
for i in range (len(wd_soc)):
    for j in wd_soc[i]:
        if (j==''):
            wd_soc[i].remove(j)
#for talk.politics.misc
for i in range (len(wd_soc)):
    for j in wd_soc[i]:
        if (j==''):
            wd_soc[i].remove(j)
#removing stopwords
#for alt.atheism
for i in range (len(wd_alt)):
        for j in wd_alt[i]:
            for k in range (len(stopword)):
                    if(j == stopword[k]):
                        wd_alt[i].remove(j)
#for comp.graphics
for i in range (len(wd_comp)):
        for j in wd_comp[i]:
            for k in range (len(stopword)):
                    if(j == stopword[k]):
                        wd_comp[i].remove(j)
#for rec.motorcycles
for i in range (len(wd_rec)):
        for j in wd_rec[i]:
            for k in range (len(stopword)):
                    if(j == stopword[k]):
                        wd_rec[i].remove(j)
#for soc.religion.christian
for i in range (len(wd_soc)):
        for j in wd_soc[i]:
            for k in range (len(stopword)):
                    if(j == stopword[k]):
                        wd_soc[i].remove(j)
#for talk.politics.misc
for i in range (len(wd_talk)):
        for j in wd_talk[i]:
            for k in range (len(stopword)):
                    if(j == stopword[k]):
                        wd_talk[i].remove(j)

#removing non-alphabet letter and change all alphabets to lower case
#for alt.athesim
for i in range (len(wd_alt)):
    for j in range (len(wd_alt[i])):
            wd_alt[i][j]=re.sub(r'[^a-z]','',wd_alt[i][j].lower()).strip()
#for comp.graphics
for i in range (len(wd_comp)):
    for j in range (len(wd_comp[i])):
            wd_comp[i][j]=re.sub(r'[^a-z]','',wd_comp[i][j].lower()).strip()
#for rec.motorcycles
for i in range (len(wd_rec)):
    for j in range (len(wd_rec[i])):
            wd_rec[i][j]=re.sub(r'[^a-z]','',wd_rec[i][j].lower()).strip()
#for soc.religion.christian
for i in range (len(wd_soc)):
    for j in range (len(wd_soc[i])):
            wd_soc[i][j]=re.sub(r'[^a-z]','',wd_soc[i][j].lower()).strip()
#for talk.politics.misc
for i in range (len(wd_talk)):
    for j in range (len(wd_talk[i])):
            wd_talk[i][j]=re.sub(r'[^a-z]','',wd_talk[i][j].lower()).strip()

#stemming
stemmer=PorterStemmer()
alt=[]
comp=[]
rec=[]
soc=[]
talk=[]
#for alt.atheism
for i in range (len(wd_alt)):
        alt.append([stemmer.stem(plural) for plural in wd_alt[i]])
#for comp.graphics
for i in range (len(wd_comp)):
        comp.append([stemmer.stem(plural) for plural in wd_comp[i]])
#for rec.motorcycles
for i in range (len(wd_rec)):
        rec.append([stemmer.stem(plural) for plural in wd_rec[i]])
#for soc.religion.christian
for i in range (len(wd_soc)):
        soc.append([stemmer.stem(plural) for plural in wd_soc[i]])
#for talk.politics.misc
for i in range (len(wd_talk)):
        talk.append([stemmer.stem(plural) for plural in wd_talk[i]])


#creating set for unique word appear even once in one of files in dataset
# for alt.atheism
uniwd_alt=set()
for i in range (len(alt)):
    uniwd_alt.update(alt[i])
# for comp.graphics
uniwd_comp=set()
for i in range (len(comp)):
    uniwd_comp.update(comp[i])
# for rec.motorcycles
uniwd_rec=set()
for i in range (len(rec)):
    uniwd_rec.update(rec[i])
# for soc.religion.christian
uniwd_soc=set()
for i in range (len(soc)):
    uniwd_soc.update(soc[i])
# for talk.politics.misc
uniwd_talk=set()
for i in range (len(talk)):
    uniwd_talk.update(talk[i])
# final unique word
uniwd=set()
uniwd=uniwd_alt.union(uniwd_comp.union(uniwd_rec.union(uniwd_soc.union(uniwd_talk))))

#creating dictionary for storing the frequency of word k in document i
dict_f={}
for i in range (len(textfile_List)):
    for j in range (len(textfile_List[i])):
        dict_f[textfile_List[i][j]]=dict.fromkeys(uniwd,0)

# for files in alt.atheism
for i in range (len(textfile_List[0])):
    for word in alt[i]:
        dict_f[textfile_List[0][i]][word]+=1
#for files in comp.graphics
for i in range (len(textfile_List[1])):
    for word in comp[i]:
        dict_f[textfile_List[1][i]][word]+=1
#for files in rec.motorcycles
for i in range (len(textfile_List[2])):
    for word in rec[i]:
        dict_f[textfile_List[2][i]][word]+=1
#for files in soc.religion.christian
for i in range (len(textfile_List[3])):
    for word in soc[i]:
        dict_f[textfile_List[3][i]][word]+=1
#for files in talk.politics.misc
for i in range (len(textfile_List[4])):
    for word in talk[i]:
        dict_f[textfile_List[4][i]][word]+=1

#creating dictionary for storing the document frequency
dict_n=dict.fromkeys(uniwd,0)
for i in range (len(textfile_List)):
    for j in range (len(textfile_List[i])):
        for word in uniwd:
            if (dict_f[textfile_List[i][j]][word]!=0):
                dict_n[word]=dict_n[word]+1

# print(pd.DataFrame(dic_f))
# finding the number of documents(N) in the dataset
N=0
for i in range (len(textfile_List)):
    for j in range (len(textfile_List[i])):
        N=N+1
print(N)

#computing the weight of word k in document i : aik
array_weight=[]
for i in range (len(textfile_List)):
    for j in range (len(textfile_List[i])):
        array_weight.append(dict.fromkeys(uniwd,0))

index=-1
for i in range (len(textfile_List)):
    for j in range (len(textfile_List[i])):
        index=index+1
        for word in uniwd:
            array_weight[index][word]=dict_f[textfile_List[i][j]][word]*math.log10(N/dict_n[word])

#computing the document-by-word matrix
matrix=[]
for i in range (len(textfile_List)):
    for j in range (len(textfile_List[i])):
        matrix.append(dict.fromkeys(uniwd,0))

index2=-1
denominator=0
for i in range (len(textfile_List)):
    for j in range (len(textfile_List[i])):
        index2=index2+1
        for word in uniwd:
            denominator=math.sqrt(float(array_weight[index2][word]))+denominator
        for word in uniwd:
            matrix[index2][word]=array_weight[index2][word]/denominator
        denominator=0

print(pd.DataFrame(matrix))





