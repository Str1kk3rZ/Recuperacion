from functools import reduce
"""
Primero
"""

a=[[1,2,3],[4,5,6],[7,8,9],[11,12,13],[14,15,16]]

m=list(map(lambda x:[x[0]]+[x[len(x)-1]],a))

print ("primero",a)

"""
Segundo
"""
i=[12,26,38,20,84,21,55]
b=list(map(lambda x:str(x),i))
perfecto=list(filter(lambda x:reduce(lambda a,b :int(a)%2==0 and int(b)%2==0,x),b))
                     
perfecto=list(map(lambda a:reduce(lambda c,b:c+b,a),perfecto))
perfecto=list(map(lambda a:int(a),perfecto))
print ("segundo",perfecto)
"""
Tercero
"""
p=list(map(lambda y:reduce(lambda a,b:a if a>b else b,y),a))
print("tercero",p)
"""
Quinto
"""
y=[2,40,16,25,31]
e=list(filter(lambda x: x<y[0]**5 ,y))
print("Quinto",e)

"""
Sexto
"""
z=[(21,6),(6,3),(20,7)]

lista=map(lambda x:x[0] if x[0] == (x[1]*(x[1]+1)/2) else 0,z)
suma=reduce(lambda a,b:a+b,lista)
print ("sexto",suma)
