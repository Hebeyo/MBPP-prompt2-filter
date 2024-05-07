def encode_list(list1):
    encoded_list=[]
    i=0
    while i<len(list1):
        count=1
        while i+1<len(list1) and list1[i]==list1[i+1]:
            i+=1
            count+=1
        encoded_list.append([count,list1[i]])
        i+=1
    return encoded_list
