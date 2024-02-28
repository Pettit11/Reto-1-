def mayor(k):
  n=len(k)
  m=k[0]
  for i in range (n):
    if m<k[i]:
      m=k[i]
  return m

def mayorsuma(a): 
  q=[]
  for i in range(len(a)-1): 
    n=a[i]+a[i+1]
    q.append(n)
  return mayor(q)

x=[int(y) for (y) in input("Digite los números separados por comas: ").split(",")]
print(mayorsuma(x))
