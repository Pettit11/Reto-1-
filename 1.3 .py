def esprimo(n):
  b=True
  for i in range(2, int(n**0.5)+1):
    b=b and (n%i!=0)
  return b and n>1

def muestraprimos(a): 
  q=[]
  for i in range(len(a)): 
    if esprimo(a[i]): 
      q.append(a[i])
  return q

x=[int(y) for (y) in input("Digite los números separados por comas: ").split(",")]   
z=muestraprimos(x)
print(z)
