print ("Bienvenido al clasificador de edad")
user_name = input ("cual es su nombre?")
user_age = int(input ("cual es su edad?"))
if user_age < 18 :
    print(f"{user_name},segun tu edad {user_age}, eres menor de edad")
elif 18 <= user_age <= 59:
    print(f"{user_name}, segun tu edad {user_age}, eres adulto")
else:
    print (f"{user_name}, segun tu edad {user_age}, eres adulto mayor")