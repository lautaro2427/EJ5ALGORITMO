cp=int(input("ingrese la cantidad de pagina"))

precio=500+cp*20.20

if cp >600:
    precio+=536
    
else:
    if cp>300:
        precio+=200
print("el precio a pagar es",precio)        
        
