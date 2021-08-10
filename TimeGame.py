import time
import random
import string

Answer = ""



while True:
    start = time.time()
    Keyword = "".join(random.sample(string.ascii_letters + string.digits, k = random.randint(10,13)))
    print("Write this:" , Keyword)

    while Answer != Keyword:
        Answer = input()
        
    end = time.time()
    print("it took you" , + end - start , "seconds")
    
