direccion_ip = input("Inserte Aquí Su IP")

#Separa los números de la dirección

Octeto = direccion_ip.split(".")

#verifica la clase de su Dirección Ip

If int(Octeto[0]) >= 0 and int(Octeto[0]) <= 126:
 print("Su Dirección IP es de Clase A")

elif int(Octeto[0]) >= 127 and int(Octeto[0]) <= 191:
 print("Su Dirección IP es de Clase B")

elif int(Octeto[0]) >= 192 and int(Octeto[0]) <= 223:
 print("Su Dirección IP es de Clase C")

elif int(Octeto[0]) >= 224 and int(Octeto[0]) <= 239:
 print("Su Dirección IP es de Clase B")

elif int(Octeto[0]) >= 240 and int(Octeto[0]) <= 255:
print("Su Dirección IP es de Clase E")
 
else:
 print("Su IP no es Válida")
