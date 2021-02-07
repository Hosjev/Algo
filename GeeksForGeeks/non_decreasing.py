# Honestly, I have no idea what this is

import numpy as np 
  
# Returns count of non- decreasing  
# numbers with n digits.  
def nonDecNums(n) : 
          
    # a[i][j] = count of all possible number  
    # with i digits having leading digit as j  
    a = np.zeros((n + 1, 10))  
  
    # Initialization of all 0-digit number  
    for i in range(10) : 
        a[0][i] = 1
  
    # Initialization of all i-digit  
    # non-decreasing number leading with 9 
    for i in range(1, n + 1) :  
        a[i][9] = 1
  
    # for all digits we should calculate  
    # number of ways depending upon  
    # leading digits 
    for i in range(1, n + 1) : 
        for j in range(8, -1, -1) :  
            a[i][j] = a[i - 1][j] + a[i][j + 1] 
  
    return int(a[n][0])  
  
# Driver Code  
if __name__ == "__main__" :  
  
    n = 2
    print("Non-decreasing digits = ",  
                       nonDecNums(n)) 
