def count_in_other(list1, list2):
    numsame=0
    for x in list1:
        for y in list2:
            if y==x:
                numsame+=1
    return numsame


def buy_items(stock, request, prices):
    #price= request*prices
    for l in (stock):
        if stock[l]<=0:
            return -1
    for l in (request):
        if request[l]<=0:
            return -1
    for l in (prices):
        if prices[l]<=0:
            return -1
##Know that I hate this###
    try:
        for l in stock:
            prices[l]
    except:
        return -2
    try:
        for m in request:
            request[m]>stock[m]
    except:
        return -3

    pay=0
    for m in request:
        if request[m]>stock[m]:
            return -3
        else:
            pay+=request[m]*prices[m]
    return pay

def count_less_than(vals, k):
    bummer=0
    for x in vals:
        for s in x:
            if s==0:
                return -1
            elif s < k:
                bummer+=1
    return bummer



def count_absences(seating_chart, attendance):
    brats=0
    for x in range(len(attendance)):
        for y in range(len(attendance[x])):
            if seating_chart[x][y]!=attendance[x][y]:
                brats+=1
    return brats


def find_in_other(list1, list2):
    ammo=[]
    z=[]
    for l in range(len(list1)):
        for x in range(len(list2)):
            if list1[l]==list2[x]:
                z+=[x]
        ammo.append(z)
        z=[]
    return ammo



def count_has_k_even_divisors(n, k):
    bored=0
    for x in range(1,n):
        count=0
        for y in range(1,n):
            if (x % y)==0:
                count+=1
        if count==k:
            bored+=1
    return bored


seating_chart = [["Carly","Sam","Freddy","Drake","Josh"],["Homer","Bart","Marge","Lisa","Maggie"],["Robin","Starfire","Raven","Cyborg","Beast  Boy"]]
attendance = [["Carly","","Freddy","","Josh"],["Homer","","Marge","Lisa","Maggie"],["Starfire","Robin","Raven","Beast  Boy","Cyborg"]]
#format()/split()/append()/extend()/items()/values()/setdefault()
#Game of Thrones is an anology for america. Started great, got better,
#promising sci fi future,
#now terrible, awful final season that undoes
#all its previous greatness.
#Did I just have an hour long break to watch memes? Yes
#Am i ready to grind? Also yes
#Are notes in python programming twitter? Hell no
#so... return to work.