def operacion(a): 
  if a[2]=="+": 
    return int(a[0]) + int(a[1])
  elif a[2]=="-": 
    return int(a[0]) - int(a[1])
  elif a[2]=="*": 
    return int(a[0]) * int(a[1])
  elif a[2]=="/": 
    return int(a[0]) * int(a[1])
  else: 
    return "Datos ingresados no válidos"

x=input("Digite dos números y su operador cada uno separado por comas: ").split(",")
y=operacion(x)
print(y)
