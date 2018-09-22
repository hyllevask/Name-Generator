#Todo: Kolumner  som alla ar noll gor att det fastnar pa 30
import numpy as np
letters = 5 #input('Number of letters: ')
X = np.random.random_sample(letters)
mu = np.loadtxt('mu.txt')
P = np.loadtxt('P.txt')
#print mu
#print P

name = np.zeros(letters)
for ii in range(0,letters):
    if ii == 0:
        t = (np.cumsum(mu) < X[ii])
        index = np.max([i for i, x in enumerate(t) if x]) #Hittade online & det funkar!
        name[ii] = index
        
    else:
        print 'Hej!'
        prev_index = int(name[ii-1])
        local_mu = P[prev_index,:]
        t = (np.cumsum(local_mu) < X[ii])
        print t
        index = np.max([i for i, x in enumerate(t) if x]) #Hittade online & det funkar!
        name[ii] = index

        
        
        
print name   


