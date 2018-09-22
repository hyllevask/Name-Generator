#INDEX BoRJAR Pa NOLL

#Open and read file
import numpy as np
file_object = open(r"C:\Users\Johan\Desktop\MarkovProjekt\Namn.txt","r")
A = file_object.read()
#Split file
B = A.split()
B[83] = 'marta'
print(B[1])
#Close file
file_object.close()

alpha = np.zeros((31,31))
mu = np.zeros((31,1))
for ii in range(0,100):
    #Parse each name and add to the statistical 
    #print ii
    namn = B[ii]
    namn = namn.lower()
    namn_list = list(namn)
    #print ii
    prev_nummer = 0
    for jj in range(0,len(namn_list)):
        nummer = ord(namn_list[jj])
        #print nummer
        nummer = nummer - 96
        print nummer
        #print jj
        if jj == 0:     #First character, insert in the initialisation vector
            mu[nummer] = mu[nummer] + 1
        else:
            alpha[prev_nummer,nummer] = alpha[prev_nummer,nummer] + 1
    
        prev_nummer = nummer




alpha = alpha/100
mu = mu/100
print alpha
print mu
print namn_list


np.savetxt('P.txt', alpha,  fmt='%.4e')
np.savetxt('mu.txt', mu, fmt='%.4e')


