def myreduce(func,seq):
    while len(seq)>1:
        res=func(seq[0],seq[1])
        seq=seq[2:]
        seq.insert(0,res)
    return seq[0]
seq=[1,2,3,4,5,6,7,8]
print(myreduce(max,seq))
print(int(myreduce(lambda x,y:str(x)+str(y),seq))) #idr what this is supposed to do lol but till here it works