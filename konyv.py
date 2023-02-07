f=open("regenyek.txt","r",encoding="UTF-8")
file_data=[]
#1.

for i in f:
    if(i[-1]=='\n'):
        file_data.append(i[:-1].split('\t'))
    else:
        file_data.append(i.split('\t'))

del file_data[0]

#2.
poirot=0
marple=0

for i in range(len(file_data)):
    if(file_data[i][0]=="Poirot"):
        poirot+=1
    elif(file_data[i][0]=="Marple"):
        marple+=1

print("Marple kategóriás könyvek száma:",marple,"Poirot kategóriás könyvek száma:",poirot)

#3.


#4.


#5.
