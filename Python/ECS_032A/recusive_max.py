def find_highest_number_in_file(a):
    file=open(str(a),"r")
    z=file.readlines()
    l=z[1]
    print(type(l))
    for x in z:
        x=x[:-1]
        x=x.split()
        if len(x)>1:
            return False
        if x[0] > l[0]:
            l = x
    print(type(l[:-1]))
    return int(l[:-1]), find_highest_in_file("prob1case1.txt")