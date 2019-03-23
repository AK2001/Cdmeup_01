res=input("do you want to play")
while res.lower()=="yes":
    print("what kind of shape do you want?")
    i=input("rectangle,square,triangle or circle?")
    if i.lower()=="rectangle":
        a=int(input("give the 2 sides"))
        b=int(input())
        while a<0 or b<0:
            a = int(input("give 2 positive sides"))
            b = int(input())
        print("the area is:",a*b)
        print("the perimeter is:",a*2+b*2)
    elif i.lower()=="square":
        c=int(input("give side"))
        while c<0:
            c = int(input("give a positive side"))
        print("the area is:",c**2)
        print("the perimeter is:",c*4)
    elif i.lower()=="triangle":
        d=int(input("give base and height"))
        e=int(input())
        while d<0 or e<0:
            d = int(input("give positive base and height"))
            e = int(input())
        print("the area is:",((d*e)/2))
    else:
        ray=int(input('give ray lenght'))
        while ray<0:
            ray = int(input('give a positive ray lenght'))
        print("the area is:",3,14*(ray**2))
        print("the perimeter is:",2*3.14*ray)
    res=input("do you want to still playing, YES OR NO?")
thanks
