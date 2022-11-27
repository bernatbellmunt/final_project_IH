
#my column will be the years -> function 1
def clean_centuries(column):
    nl0=[]
    nl=[]
    for y in column:
        if y[0]==" ":
            nl0.append(y[1:])
        else:
            nl0.append(y)

    for y in nl0:
               
        if y in centuries:
            new = centuries[y]
            nl.append(new)
        else:
            nl.append(y)
    return nl


#my column will be the year -> function 2
def clean_year(col):
    nl=[]
    a=[]
    out=[]

    for elem in col:
        if "-" in elem:
            nl.append(elem)
        else:
            nl.append(elem)

    for e in nl:
        a.append(e.split(" - ")[-1])
    
    for el in a:
        if len(el)>4:
            findnum= re.findall("\d{4}",el)
            if findnum!=[]:
                out.append(re.findall("\d{4}",el)[0])
            else:
                out.append(elem)
        else:
            out.append(el)
    
    return out


centuries = {"I":"10","II":"100","III":"200","IV":"300","V":"400","VI":"500","VII":"600","VIII":"700","IX":"800",
"X":"900","XI":"1000","XII":"1100","XIII":"1200","XIV":"1300","XV":"1400","XVI":"1500","XVII":"1600",
"XVIII":"1700","XIX":"1800","XX":"1900","XXI":"2000"}

#my column will be the year -> function 3
def last_year(col):
    a=[]
    for e in col:
        e=e.replace(" ","")
        if e in centuries:
            a.append(centuries[e])

        else:
            a.append(e)
    return a


def create_img_name_col (col):
    img_name=[]
    for elem in col:
        elem = elem.split("/")
        img_name.append(elem[-1])
    return img_name