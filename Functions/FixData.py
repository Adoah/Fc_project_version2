import glob
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

metaData = pd.DataFrame()
for file in glob.glob('Data\\*.txt'):
    newEntry = {}
    split = file.split('\\')[1].split('_')
    newEntry['file'] = file

    if 'C' in split[0]:
        newEntry['Ending'] = 'C'
    else:
        newEntry['Ending'] = ''

    if split[1] == 'Negative':
        newEntry['Votlage Range'] = 'N'
    if split[1] == 'Positive':
        newEntry['Votlage Range'] = 'Y'
    
    data = pd.read_csv(file, sep = '\t', header = None)
    
    if 'C' in newEntry['Ending']:
        data.columns = ['V1', 'OPE1C', 'V2', 'OPE2C', 'V3', 'OPE3C']
        
        OPE1 = data[['V1','OPE1C']]
        OPE2 = data[['V2','OPE2C']]
        OPE3 = data[['V3','OPE3C']]

    else:
        data.columns = ['V', 'OPE1', 'OPE2', 'OPE3']
        
        OPE1 = data[['V','OPE1']]
        OPE2 = data[['V','OPE2']]
        OPE3 = data[['V','OPE3']]

    OPE1.columns = ['V', 'Ea']
    OPE2.columns = ['V', 'Ea']
    OPE3.columns = ['V', 'Ea']
    
    OPE1 = OPE1.dropna()
    OPE2 = OPE2.dropna()
    OPE3 = OPE3.dropna()

    fileName1 = "Data\\Fixed\\OPE%s_%s_1.txt"%(newEntry['Ending'],newEntry['Votlage Range'])
    newEntry['n'] = 1
    newEntry['file'] = fileName1
    metaData = metaData.append(pd.DataFrame(newEntry,index=[0]))
    
    fileName2 = "Data\\Fixed\\OPE%s_%s_2.txt"%(newEntry['Ending'],newEntry['Votlage Range'])
    newEntry['n'] = 2
    newEntry['file'] = fileName2
    metaData = metaData.append(pd.DataFrame(newEntry,index=[0]))
    
    fileName3 = "Data\\Fixed\\OPE%s_%s_3.txt"%(newEntry['Ending'],newEntry['Votlage Range'])
    newEntry['n'] = 3
    newEntry['file'] = fileName3
    metaData = metaData.append(pd.DataFrame(newEntry,index=[0]))
    
    OPE1.to_csv(fileName1, sep = '\t', index = False)
    OPE2.to_csv(fileName2, sep = '\t', index = False)
    OPE3.to_csv(fileName3, sep = '\t', index = False)