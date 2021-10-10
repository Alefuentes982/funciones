def saludo():
    print("Hola mundo 2")


saludo()


def suma(n1,n2):
    return  n1+n2
numero1=int(input("ingrese primer numero: \n"))
numero2=int(input("ingrese segundo numero: \n"))

print("la suma es: ", suma(numero1, numero2))



def saludos_mensaje(nombre, apellido):
    print("Bienvenido ",nombre," ",apellido)


nombre1=input("ingrese su nombre: \n")
apellido1=input("ingrese su apellido: \n")

saludos_mensaje(nombre1, apellido1)

