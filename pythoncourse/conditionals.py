x = int(input("ingresa tu edad"))

if(x>0 and x<18):
    print("eres menor")
elif(x>18 and x<60):
    print("eres mayor")
else:
    print("eres de la tercera edad")