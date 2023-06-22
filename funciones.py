# Funciones en Python
# def name_function(params):
#   Codigo
#   Return

# Funcion sin parametros y sin retornos
def saludos():
    print("Hola a Todos!")

saludos()

# Funciones con 1 parametro
def get_age_in_future(age):
    print(f" En 3 años tendras { age + 3} años")

get_age_in_future(19)

# funciones con 2 parametros sin retorno
def suma(num1, num2):
    print(f"{ num1 } + { num2 } = { num1 + num2 }")

suma(12, 35)

# Funciones con parametros opcionales
def  get_heroes( h1 = "Iroman", h2 = "Spiderman"):
    print([h1, h2])

get_heroes()
get_heroes("Batman")
get_heroes("Batman", "Superman")
get_heroes(h2="Batman", h1="Superman")

# Funciones con retorno 
def title(texto):
    return texto.title()

text_changed = title("hOlA a TodOs")
print(text_changed)