def palindromo(a):  
  if a==a[::-1]: 
    return True 
  else: 
    return False 

x=input("Digite la palabra a evaluar: ").split(",")    
y=palindromo(x) 
print(y)        
