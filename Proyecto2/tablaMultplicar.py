n = int(input("Ingresa n: "))
for i in range(1,n+1):
    print(f"tabla del {i}: ")
    for j in range(1,n+1):
        print (f"{i} x {j} = {i*j}")
    print("\n\n")