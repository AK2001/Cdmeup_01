i=int(input("give a number "))
k=1
while i%2!=1:
    print('give a number again')
    i=int(input())
if i%2==1:
    print("correct")
while k<=i:
    print(k)
    k=k+2