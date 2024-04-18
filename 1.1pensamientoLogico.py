def unknownInEquilateral (a,b,c,d,e,f,g,h):
    side1 = a+b+c+d
    side2 = d+e+f+g
    side3 = g+h+a
    while True:
        if side1 == side2 :
            i = side1 - side3 
            print (f"La incognita del triangulo es{i}")
        else: 
            print ("error vuelva a colocar los datos")
unknownInEquilateral(int(input),int(input),int(input),int(input),int(input),int(input),int(input),int(input))