f=open("regenyek.txt","r")
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


#3. Átlag számolósdi

osszeg=0

for i in range(len(file_data)):
    osszeg+=int(file_data[i][3])

print("Az árak átlagösszege: ",round(osszeg/len(file_data)),"ft")    

#4.


#5.
