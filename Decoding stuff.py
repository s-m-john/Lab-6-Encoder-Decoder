#dawson craft decoder

def decode(tbd):
    decode_dictionary= {'0':7, '1':8, '2':9, '3':0, '4':1, '5':2, '6':3, '7':4, '8':5, '9':6 } #dict that changes values to decode them
    decodedlist=[]
    tempnum=''
    for i in range(0,8):
        tempnum=tbd[i]
        decodedlist.append(decode_dictionary[tempnum])
    return decodedlist
decodedlist=decode(tbd)
print(str(decodedlist[0]) +str(decodedlist[1]) +str(decodedlist[2]) +str(decodedlist[3]) +str(decodedlist[4]) +str(decodedlist[5]) +str(decodedlist[6]) +str(decodedlist[7]) )