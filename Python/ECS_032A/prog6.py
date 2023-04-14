from  entity  import  Entity

def find_highest_in_file(a):
    a=str(a)
    file=open(a,"r")
    z=file.readlines()
    l=int(z[0])
    for x in z:
        g=x[:-1]
        g=g.split()
        if len(g)>1:
            return False
        g=int(g[0])
        if g > l:
            l = g

    return int(l)
    #return int(l[:-1])
    #find_highest_in_file("prob1case1.txt")

def find_matches(a,b,c,d):
    a=str(a)
    b=str(b)
    fileB=open(b,"w")
    z=0
    with open(a) as fileA:
        lines=fileA.readlines()
        if d==True:
            for x in lines:
                if c in x:
                    fileB.write(x)
                    z+=1
        if d==False:
            for x in lines:
                if c not in x:
                    fileB.write(x)
                    z+=1
    return z


def draw_entity(a,b):
    try:
        b[a.top_left_y+a.height][a.top_left_x+a.width]
    except:
        return False
    for s in range(a.top_left_y,a.top_left_y+a.height,1):
        for bleh in range(a.top_left_x,a.top_left_x+a.width,1):
            b[s][bleh]=a.icon
    return True

#b =    [['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']]
#e = Entity('T', 2, 1, 1, 2)
