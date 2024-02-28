def caracteres_iguales(a):
    q=[]
    for i in range(len(a)):
        p=set(a[i])
        for j in range(i+1, len(a)):
            p_2=set(a[j])
            if p_2==p and a[j] not in q:
                q.append(a[i])
                q.append(a[j])
    return q

x=[y.strip() for (y) in input("Ingrese las palabras separadas por coma cada una: ").split(",")]
print(caracteres_iguales(x)) 
