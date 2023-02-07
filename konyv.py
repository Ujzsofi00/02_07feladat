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


#3.


#4.


#5.
