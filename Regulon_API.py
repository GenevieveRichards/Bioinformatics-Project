
# coding: utf-8

# In[13]:


import requests

from bs4 import BeautifulSoup
from graphviz import Graph


f = open('testfile1.txt','w')
f.write('digraph graph {' )

#URLs
regulonID = "http://regprecise.lbl.gov/Services/rest/regulons?genomeId=601"
response = requests.get(regulonID)
file = response.json()


dot = Graph('G', filename='398_3.gv', engine='sfdp')

effector = []
pathway = []
regulationType = []
regulatorName = []
regulogID = []
regulonID = []
for regulon in range(len(file['regulon'])):
    effector.append(file['regulon'][regulon]['effector']);
    pathway.append(file['regulon'][regulon]['pathway'])
    regulationType.append(file['regulon'][regulon]['regulationType'])
    regulatorName.append(file['regulon'][regulon]['regulatorName'])
    regulogID.append( file['regulon'][regulon]['regulogId'])
    regulonID.append(file['regulon'][regulon]['regulonId'])

lists = []
counts = 0
for regulog in range(len(regulogID)):
    url = "http://regprecise.lbl.gov/Services/rest/sites?regulogId=" + str(regulogID[regulog])
    response = requests.get(url)
    file = response.json()

    #url = 'http://regprecise.lbl.gov/Services/rest/sites?regulogId=701'
    #response = requests.get(url)
    #file = response.json()
    for r in range(len(file['site'])):
        list1 = []
        try:
            counts += 1
            sites = file['site'][r]['geneLocusTag']
            regulon = file['site'][r]['regulonId']
            dot.edge(regulon, sites)
            list1 = [regulog, regulon]
            #print(list1)
            lists.append(list1)
            #print(lists)
        except KeyError:
            continue

#print(counts)
#print('Of the FORMAT: (Regulog, Regulon)')
#print(lists)
    #for i in range(len(lists)):
#    file.write("/n" + str(lists[i][0]) + " -- " + str(lists[i][1]))

f.write('}' )



    

    

