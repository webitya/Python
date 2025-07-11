index =0
count=0
def FindIndex(name,data):
    global index
    global count
    length =len(data)
    if(index<length):
        if(name==(data[index]).lower()):
            index+=1
            count+=1
            return FindIndex(name,data) 
        else:
            index+=1
            return FindIndex(name,data)
    else:
        return f'{name} in data list appears {count} times' 