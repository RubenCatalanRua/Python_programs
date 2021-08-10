# Password maker thingy
import random
import string


# Functions

def Random_Pass(N = random.randint(12,17)):

        PassType = random.randint(1,3)
        if PassType == 1:
            RandPass = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, k = N))
            print(RandPass)
        else:
            RandPass = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = N))
            print(RandPass)


def Random_Pers_Pass():
    Letters = ''.join(random.choices(string.ascii_letters, k = random.randint(8, 10)))
    Nums = ''.join(random.choices(string.digits, k = random.randint(3, 5)))
    Punct = ''.join(random.choices(string.punctuation, k = random.randint(1, 3)))

    ListString = []

    print("¿Quiéres letras, números o símbolos especiales en tu contraseña? Responde únicamente LETRAS, NÚMEROS o SÍMBOLOS. escribe STOP para recibir tu contraseña.")

    while True:         
        Preg = input()
        if Preg == "LETRAS":
            if Letters in ListString:
                print("Ya están en la contraaseña")
            else:
                ListString.append(Letters)
        elif Preg == "NÚMEROS":
            if Nums in ListString:
                print("Ya están en la contraaseña")
            else:
                ListString.append(Nums)
        elif Preg == "SÍMBOLOS":
            if Punct in ListString:
                print("Ya están en la contraaseña")
            else:
                ListString.append(Punct)
        elif Preg == "STOP":
            break
        else:
            print("No")

    PersPass = ''.join(ListString)
    
    print(PersPass)
        

# Interface stuff 

while True:
         
    while True:
        print("¿Contraseña rápida (1) o personalizada (2)?")

        try:

            Answer = int((input()))

            if Answer == 1:
                
                Random_Pass()

                break

            elif Answer == 2:
                Random_Pers_Pass()
                

            else:
                print("No")

        except ValueError:
            print("No")
