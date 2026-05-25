# 1) Hollow Pyramid
#         *
#        * *
#       *   *
#      *     *
#     *********
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
   
    for j in range(1,2*i):
        if i==1 or j==1 or i==n or j == i*2-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
   
    






















































