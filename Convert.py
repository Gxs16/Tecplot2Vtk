import pandas as pd 
import numpy as np 
import os
from pyevtk.hl import unstructuredGridToVTK
from pyevtk.vtk import VtkHexahedron
file = open('./Data/tec_test_0.3g.dat','r')#Open file in read mode 
lines = file.readlines()

#The point data
x = ''#Generate an empty string
y = ''
z = ''

for line in lines[26:432]:
    x+=line[0:-1]#Extract data from corresponding rows
x_list = x.split()#Transfer a string to a list 
X_temp = list(map(float ,x_list))#Transfer string elements in list into float numbers
X = np.array(X_temp)#Transfer a list to an array

for line in lines[432:838]:
    y+=line[0:-1]#Extract data from corresponding rows
y_list = y.split()#Transfer a string to a list 
Y_temp = list(map(float ,y_list))#Transfer string elements in list into float numbers
Y = np.array(Y_temp)#Transfer a list to an array

for line in lines[838:1244]:
    z+=line[0:-1]#Extract data from corresponding rows
z_list = z.split()#Transfer a string to a list 
Z_temp = list(map(float ,z_list))#Transfer string elements in list into float numbers
Z = np.array(Z_temp)#Transfer a list to an array

#The element data
connect = ''

for line in lines[7380:44280]:
    connect+=line[0:-1]#Extract data from corresponding rows
connect_list = connect.split()#Transfer a string to a list
connect_temp = list(map(int, connect_list))#Transfer string elements in list into float numbers
Connect = np.array(connect_temp)-1#Transfer a list to an array. In the vtk file, the sequence number begin with 0, but in the .dat file, the sequence number begin with 1.

ctype = np.zeros(36900)
ctype[:] = VtkHexahedron.tid#Define the cell type. In this file the type is Hexahedron
offset = np.arange(8,36900*8+1,8)

#The displacement data
disp_1=''
disp_2=''
disp_3=''

for line in lines[45504:45910]:
    disp_1+=line[0:-1]#Extract data from corresponding rows
disp_1_list = disp_1.split()#Transfer a string to a list 
Disp_1_temp = list(map(float ,disp_1_list))#Transfer string elements in list into float numbers
Disp_1 = np.array(Disp_1_temp)#Transfer a list to an array

for line in lines[45910:46316]:
    disp_2+=line[0:-1]#Extract data from corresponding rows
disp_2_list = disp_2.split()#Transfer a string to a list 
Disp_2_temp = list(map(float ,disp_2_list))#Transfer string elements in list into float numbers
Disp_2 = np.array(Disp_2_temp)#Transfer a list to an array

for line in lines[46316:46722]:
    disp_3+=line[0:-1]#Extract data from corresponding rows
disp_3_list = disp_3.split()#Transfer a string to a list 
Disp_3_temp = list(map(float ,disp_3_list))#Transfer string elements in list into float numbers
Disp_3 = np.array(Disp_3_temp)#Transfer a list to an array

#The residual data
residual_1=''
residual_2=''
residual_3=''

for line in lines[46722:47128]:
    residual_1+=line[0:-1]#Extract data from corresponding rows
residual_1_list = residual_1.split()#Transfer a string to a list 
Residual_1_temp = list(map(float ,residual_1_list))#Transfer string elements in list into float numbers
Residual_1 = np.array(Residual_1_temp)#Transfer a list to an array

for line in lines[47128:47534]:
    residual_2+=line[0:-1]#Extract data from corresponding rows
residual_2_list = residual_2.split()#Transfer a string to a list 
Residual_2_temp = list(map(float ,residual_2_list))#Transfer string elements in list into float numbers
Residual_2 = np.array(Residual_2_temp)#Transfer a list to an array

for line in lines[47534:47940]:
    residual_3+=line[0:-1]#Extract data from corresponding rows
residual_3_list = residual_3.split()#Transfer a string to a list 
Residual_3_temp = list(map(float ,residual_3_list))#Transfer string elements in list into float numbers
Residual_3 = np.array(Residual_3_temp)#Transfer a list to an array

#The equivalent inelastic data
equi = ''

for line in lines[47940:48310]:
    equi+=line[0:-1]#Extract data from corresponding rows
euqi_list = equi.split()#Transfer a string to a list 
Equi_temp = list(map(float ,euqi_list))#Transfer string elements in list into float numbers
Equi = np.array(Equi_temp)#Transfer a list to an array

#The principle stress
prin_1=''
prin_2=''
prin_3=''

for line in lines[48310:48680]:
    prin_1+=line[0:-1]#Extract data from corresponding rows
prin_1_list = prin_1.split()#Transfer a string to a list 
Prin_1_temp = list(map(float ,prin_1_list))#Transfer string elements in list into float numbers
Prin_1 = np.array(Prin_1_temp)#Transfer a list to an array

for line in lines[48680:49050]:
    prin_2+=line[0:-1]#Extract data from corresponding rows
prin_2_list = prin_2.split()#Transfer a string to a list 
Prin_2_temp = list(map(float ,prin_2_list))#Transfer string elements in list into float numbers
Prin_2 = np.array(Prin_2_temp)#Transfer a list to an array

for line in lines[49050:49420]:
    prin_3+=line[0:-1]#Extract data from corresponding rows
prin_3_list = prin_3.split()#Transfer a string to a list 
Prin_3_temp = list(map(float ,prin_3_list))#Transfer string elements in list into float numbers
Prin_3 = np.array(Prin_3_temp)#Transfer a list to an array

#The stress data
stress_1=''
stress_2=''
stress_3=''
stress_4=''
stress_5=''
stress_6=''

for line in lines[49420:49790]:
    stress_1+=line[0:-1]#Extract data from corresponding rows
stress_1_list = stress_1.split()#Transfer a string to a list 
Stress_1_temp = list(map(float ,stress_1_list))#Transfer string elements in list into float numbers
Stress_1 = np.array(Stress_1_temp)#Transfer a list to an array

for line in lines[49790:50160]:
    stress_2+=line[0:-1]#Extract data from corresponding rows
stress_2_list = stress_2.split()#Transfer a string to a list 
Stress_2_temp = list(map(float ,stress_2_list))#Transfer string elements in list into float numbers
Stress_2 = np.array(Stress_2_temp)#Transfer a list to an array

for line in lines[50160:50530]:
    stress_3+=line[0:-1]#Extract data from corresponding rows
stress_3_list = stress_3.split()#Transfer a string to a list 
Stress_3_temp = list(map(float ,stress_3_list))#Transfer string elements in list into float numbers
Stress_3 = np.array(Stress_3_temp)#Transfer a list to an array

for line in lines[50530:50900]:
    stress_4+=line[0:-1]#Extract data from corresponding rows
stress_4_list = stress_4.split()#Transfer a string to a list 
Stress_4_temp = list(map(float ,stress_4_list))#Transfer string elements in list into float numbers
Stress_4 = np.array(Stress_4_temp)#Transfer a list to an array

for line in lines[50900:51270]:
    stress_5+=line[0:-1]#Extract data from corresponding rows
stress_5_list = stress_5.split()#Transfer a string to a list 
Stress_5_temp = list(map(float ,stress_5_list))#Transfer string elements in list into float numbers
Stress_5 = np.array(Stress_5_temp)#Transfer a list to an array

for line in lines[51270:51640]:
    stress_6+=line[0:-1]#Extract data from corresponding rows
stress_6_list = stress_6.split()#Transfer a string to a list 
Stress_6_temp = list(map(float ,stress_6_list))#Transfer string elements in list into float numbers
Stress_6 = np.array(Stress_6_temp)#Transfer a list to an array

#Write all the data to a vtk file
unstructuredGridToVTK("./Output/Ver_1.0", X, Y, Z, connectivity = Connect, offsets = offset, cell_types = ctype, cellData = {'equivalent_inelastic':Equi,'Principal_1':Prin_1,'Principal_2':Prin_2,'Principal_3':Prin_3,'Stress_1':Stress_1,'Stress_2':Stress_2,'Stress_3':Stress_3,'Stress_4':Stress_4,'Stress_5':Stress_5,'Stress_6':Stress_6}, pointData = {'Disp_1':Disp_1,'Disp_2':Disp_2,'Disp_3':Disp_3,'Residual_1':Residual_1,'Residual_2':Residual_2,'Residual_3':Residual_3})