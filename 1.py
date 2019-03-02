print("what kind of shape do you want?")
i=input("rectangle,square,triangle or circle?")
if i=="rectangle":
    a=int(input("give the 2 sides"))
    b=int(input())
    print("the area is:",a*b)
    print("the perimeter is:",a*2+b*2)
elif i=="square":
    c=int(input("give side"))
    print("the area is:",c**2)
    print("the perimeter is:",c*4)
elif i=="triangle":
    d=int(input("give base and height"))
    e=int(input())
    print("the area is:",((d*e)/2))
else:
    ray=int(input('give ray lenght'))
    print("the area is:",3,14*(ray**2))
    print("the perimeter is:",2*3.14*ray)