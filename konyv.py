f=open("regenyek.txt","r",encoding="UTF-8")
file_data=[]
#1.

for i in f:
    if(i[-1]=='\n'):
        file_data.append(i[:-1].split('\t'))
    else:
        file_data.append(i.split('\t'))

del file_data[0]

print("Regények száma: ",len(file_data))

#2.
poirot=0
marple=0

for i in range(len(file_data)):
    if(file_data[i][0]=="Poirot"):
        poirot+=1
    elif(file_data[i][0]=="Marple"):
        marple+=1

print("Marple kategóriás könyvek száma:",marple,"Poirot kategóriás könyvek száma:",poirot)

#3. Átlag számolósdi

osszeg=0

for i in range(len(file_data)):
    osszeg+=int(file_data[i][3])

print("Az árak átlagösszege: ",round(osszeg/len(file_data)),"ft")    

#4.


#5.

f2=open("ujra.txt","w",encoding="UTF-8")
csere=''

for i in range(len(file_data)):
    csere=round(int(file_data[i][3])*1.1)
    uj=file_data[i][3].replace(file_data[i][3],str(csere))
    f2.write(file_data[i][0]+"\t"+file_data[i][1]+"\t"+file_data[i][2]+"\t"+uj+"\n")