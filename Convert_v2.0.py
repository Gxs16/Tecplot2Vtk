#!/usr/bin/env python
# coding: utf-8

# In[138]:


import pandas as pd 
import numpy as np 
import os
from pyevtk.hl import unstructuredGridToVTK
from pyevtk.vtk import VtkHexahedron
import re


# In[139]:


#Open file in read mode 
file = open('./Data/tec_test_0.3g.dat','r')
lines = file.readlines()
file.close()


# In[140]:


#Delete the '\n' at the end of each line
for i in range(len(lines)):
    lines[i] = lines[i][:-1]


# In[141]:


data = []#The data of each ZONE
position = []#The position of 'VARIABLES' and 'ZONE'
#split VARIABLES
position.extend([lines.index('VARIABLES=')])


# In[142]:


#split ZONE
key_word = re.compile(r'ZONE T=')
line_match = list(filter(key_word.search, lines))#Get the serial number of lines which include ZONE
for key in line_match:
    position.extend([lines.index(key)])
position.append(len(lines))
#Split the file into several parts:Variables, Zone 1 ~ Zone n, 
for i in range(len(position)-1):
    data.append(lines[position[i]:position[i+1]])


# In[143]:


for zone in data[1:]:
    #Get the position of key words in the ZONE
    key_words = ['^N=', 'DATAPACKING=', 'SOLUTIONTIME=', 'VARLOCATION=', 'DT=']
    position_key = dict.fromkeys(key_words,[])
    serial = []#the list of serial number of all key word in order to determine the start of value
    for key in key_words:
        target = re.compile(key)
        position = []
        for x in filter(target.search, zone):
            position.append(zone.index(x))
        position_key[key] = position
        serial.extend(position)
        
    #Get the informations about nodes and elements
    string = zone[position_key['^N='][0]]
    a = string.split(', ')
    number_of_nodes = int(a[0][2:])
    number_of_elements = int(a[1][2:])
    
    #Get the informations about solutiontime
    string = zone[position_key['SOLUTIONTIME='][0]]
    SOLUTIONTIME = int(string[string.index('=')+1:])
    
    #Get the information about variable location
    string = zone[position_key['VARLOCATION='][0]]
    location = 'CELLCENTERED'
    serial_number = string[string.index('[')+1 : string.index(']')-1]
    loc = serial_number.split(' ')#Transfer a string to a list
    
    a = np.array(serial)
    flag = a.max()+1 #Attention!
    #Prepare three empty dictionary 
    cordinate=dict()
    cellData=dict()
    pointData=dict()
    for i in data[0][1:]:
        value_list = []
        if str(data[0].index(i)) in loc:
            rows = number_of_elements//100 +1
            value = zone[flag:flag+rows]
            for line in value:
                value_list.extend(line.split())
            cellData[i] = np.array(list(map(float, value_list)))
        else:
            rows = number_of_nodes//100 + 1
            value = zone[flag:flag+rows]
            for line in value:
                value_list.extend(line.split())
            if i not in ['X','Y','Z']:
                pointData[i] = np.array(list(map(float, value_list)))
            else:
                cordinate[i] = np.array(list(map(float, value_list)))
        flag += rows

    connect = ''
    for line in zone[flag:]:
        connect+=line#Extract data from corresponding rows
    connect_list = connect.split()#Transfer a string to a list
    connect_temp = list(map(int, connect_list))#Transfer string elements in list into float numbers
    Connect = np.array(connect_temp)-1#Transfer a list to an array. In the vtk file, the sequence number begin with 0, but in the .dat file, the sequence number begin with 1.

    ctype = np.zeros(number_of_elements)
    ctype[:] = VtkHexahedron.tid#Define the cell type. In this file the type is Hexahedron
    offset = np.arange(8,number_of_elements*8+1,8)

    #Write all the data to a vtk file
    unstructuredGridToVTK('./Output/Ver_3.0_'+zone[0][-9:-1], cordinate['X'], cordinate['Y'], cordinate['Z'],                          connectivity = Connect, offsets = offset, cell_types = ctype, cellData = cellData,                          pointData = pointData)

