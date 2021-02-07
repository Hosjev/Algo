def printAllPathsUtil(mat, i, j, r, c, path, pi): 
    # mat, 0, 0, 3, 3, [0...(6)], 0
    # go R 0,1,2 before hitting condition 
    if (i == r - 1): # i = 2 j = 0 c = 3 pi = 2
        for k in range(j, c): # 0-3 (2)
            path[pi + k - j] = mat[i][k]
            # path[0] = 1
            # path[1] = 4
            # path[2 + 0 - 0]2 = 2/0 = 7
            # path[2 + 1 - 0]3 = 2/1 = 8
            # path[2 + 2 - 0]4 = 2/2 = 9
  
        
        for l in range(pi + c - j): # for l in range currentIndex+columnTot-currentCol
            print(path[l], end = " ") 
        print() 
        return
  
    # go D 0,1,2 before hitting condition 
    if (j == c - 1): 
        for k in range(i, r): 
            path[pi + k - i] = mat[k][j] 
  
        for l in range(pi + r - i): 
            print(path[l], end = " ") 
        print() 
        return
  
    path[pi] = mat[i][j] # [0] set to 1 (value)
    printAllPathsUtil(mat, i + 1, j, r, c, path, pi + 1) 
    printAllPathsUtil(mat, i, j + 1, r, c, path, pi + 1) 
  

def printAllPaths(mat, r, c): 
  
    path = [0 for i in range(r + c)] # on 3x3 = 6 [0,0,0,0,0]
    printAllPathsUtil(mat, 0, 0, r, c, path, 0) 



mat = [[1, 2, 3],  
       [4, 5, 6], 
       [7, 8, 9]] 
  
printAllPaths(mat, 3, 3)
