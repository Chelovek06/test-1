import random
 
 
def get_coin():
    coin = random.randint(1,2)
 
    if coin == 1:
        return "Орёл, ты выиграл"
    else:
        return"Решка, ты проиграл"
