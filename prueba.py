

lista=["angelo" , "pendiente" , "siexiste" , "algo"  , "igual"]



tupla=[("angelo" , "pendiente" , "siexiste" , "algo" , "igual")]



print(lista [0])
print(tupla[0][0])
print(lista [1])
print(tupla[0][1])
print(lista [2])
print(tupla[0][2])
print(lista [3])
print(tupla[0][3])
print(lista [4])
print(tupla[0][4])




contador=0
for x in range(len(lista)):

	

	if lista[x] == tupla[0][x]:
		contador+=1
		print(lista[x] , tupla[0][x])


print(contador)

if lista[0]== tupla[0][0] and  lista[1]== tupla[0][1] and  lista[2]== tupla[0][2] and  lista[3]== tupla[0][3] and lista[4]== tupla[0][4] :

	print("son iguales" )

else:
	print("son diferentes")	
