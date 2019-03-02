n=int(input('give a number: '))
ls=[]
for i in range(1,n+1):
    ls.append(i)
    if i%15==0:
        f=i-1
        ls[f]='FizzBuzz'
    elif i%5==0:
        f=i-1
        ls[f]='Buzz'
    elif i%3==0:
        f=i-1
        ls[f]='Fizz'
print(ls)


#n=int(input('give a number: '))
#for i in range(1,n+1):
    #if i%15==0:
        #print('FizzBuzz')
    #elif i%5==0:
        #print('Buzz')
    #elif i%3==0:
        #print('Fizz')
    #else:
        #print(i)
