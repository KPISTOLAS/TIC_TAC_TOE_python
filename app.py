#tic tac toe

def ShowTable (A):
    for i in range(0,9,3):
        print(A[i]," | " , A[i+1]," | " , A[i+2])
        if i<6:
            print("--------------")

def FillTableCheck (A, key , choice):
    if A[key-1]==str(key):
        x=True
    else:
        print("You cant place here your symbol")  
        x = False  
    return x    

def FindWinner(A):
    x = False
    pos = -1
    for i in range(0, 9, 3):
        if A[i] == A[i + 1] and A[i] == A[i + 2] and A[i + 1] == A[i + 2]:
            x = True
            pos = i
    for j in range(0, 3):
        if A[j] == A[j + 3] and A[j] == A[j + 6] and A[j + 3] == A[j + 6]:
            x = True
            pos = j
    if A[0] == A[4] and A[0] == A[8] and A[4] == A[8]:
        x = True
        pos = 0
    if A[2] == A[4] and A[2] == A[6] and A[4] == A[6]:
        x = True
        pos = 2
    return x, pos       

#main

print("Whelcome to tic tac toe")
pl1 = input ("please enter player 1 name :")
pl2 = input ("please enter player 2 name :")


win=False
print(pl1," has 'x' symbol")
print(pl2," has 'o' symbol")

count=1
A = ["1","2","3","4","5","6","7","8","9"]
x = ShowTable (A)
while win==False:
    if count==1 :
        sym = "x"
    else:
        sym="o"

    flag=False
    while flag==False :
       s= int(input("please select your place :"))
       flag=FillTableCheck(A,s,sym)
           
    A[s-1]=sym
    if count==1 :
        count=2
    else:
        count=1
    temp =ShowTable(A)
    win , pos= FindWinner(A) 
    
    if pos==-1:
     print("Draw")       
    elif A[pos]=="x":
     print(pl1," is the winner")   
         
    else:
     print(pl2," is the winner")

print("thanks for playing")  
    