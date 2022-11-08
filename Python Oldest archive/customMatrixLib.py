a=[[1,2,3,4],
[5,5,5,5],
[6,6,6,6],
[8,9,10,11]]

b=[[4,3,2,1],
[5,5,5,5],
[6,6,6,6],
[8,9,10,11]]




class matrix:
    def __init__(self):
        pass

    def divider():
        print('_______________\n')

    def slice(arr):
        for i in range(0,len(arr)):
            print(arr[i])
            matrix.divider()    

    def trace(arr):
        store,x=0,0
        for i in range (0,len(arr)):
            store=a[i][i]
            x=x+store
            print('trace till',str(i+1) + 'x' + str(i+1),x)
    def sumof(matrix1,matrix2):
        matrix1

            
matrix.slice(a)
matrix.trace(a)
