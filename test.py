for line in lines[48310:48679]:
    stress_6+=line[0:-1]#Extract X data in first 2 rows
stress_6_list = stress_6.split()#Transfer a string to a list 
Stress_6_temp = list(map(float ,stress_6_list))#Transfer string elements in list into float numbers
Stress_6 = np.array(Stress_6_temp)#Transfer a list to an array