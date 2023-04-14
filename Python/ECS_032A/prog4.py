def ess(a,b):
    lengt=str(len(a))
    return lengt+' '+a+b

def dess(a,b):
    if b!=1 and b!=2:
        return "ERROR"
    divider=int(a[0])+2
    string1=a[2:divider]
    string2=a[divider:]
    if b==1:
        return string1
    else:
        return string2

def echo(a):
    echoed=""
    for x in a:
        echoed+=x*2
    return echoed

def find_last_mismatch(a,b):
    length=len(a)
    position=0
    for (x) in range(length):
        if a[x]!=b[x]:
            return x
    return -1

def max_length(a,b,c):
    alen=len(a)
    blen=len(b)
    clen=len(c)
    if alen>blen:
        if alen>clen:
            return alen
        else:
            return clen
    elif blen>clen:
        return blen
    else:
        return clen

def interleave(a,b,c):
    a=str(a)
    b=str(b)
    c=str(c)
    minlen=max_length(a,b,c)
    moda=a+" "*(minlen-len(a))
    modb=b+" "*(minlen-len(b))
    modc=c+" "*(minlen-len(c))
    imbored=""
    for x in range(minlen):
        imbored+=moda[x]+modb[x]+modc[x]
    return(imbored)

def get_longest_stretch(a,b):
    y=0 #counter
    z=0 #save
    for x in a:
        if x==b:
            y+=1
        elif x!=b:
            if y>z:
                z=y #saves y number
                y=0 #resets y to 0
            else:
                y=0
    return z

def compute_product_at(a,b):
    product=1
    for x in b:
        product=product*(a[x])
    return product

def insert_name_here(a):
    listy=[]
    #if a[0]>a[1]:
    #        listy.append(a[0])
    if len(a)==1:
        return []
    for x in range(len(a)-1):
        if a[x]>=a[x-1] and a[x]>=a[x+1]:
            listy.append(a[x])
    if a[-1]>a[-2]:
            listy.append(a[-1])
    return listy

def get_key_to_min(a):
    bb=[]
    aa=[]
    rang=len(a)
    for b in a:
        if a[b]>=10:
            aa.append(a[b])
    for b in a:
        if a[b]==min(aa):
            return b

##get_key_to_min ({'a':5,'b':8,'abc':13,'def':18,'xyz':9})