#Cows and Bulls
import random as r
def cal_cows(rand_num, user_input):
    cows = 0
    i = 0
    for i in range(0, len(str(rand_num))):
        if (list(str(user_input))[i] in list(str(rand_num))) and (list(str(rand_num))[i] != list(str(user_input))[i]):
            cows = cows+1
    return cows

def cal_bulls(rand_num, user_input):
    bulls = 0
    i = 0
    for i in range(0, len(str(user_input))):
        if list(str(rand_num))[i] == list(str(user_input))[i]:
            bulls = bulls+1
    return bulls
    
if __name__=="__main__":
    print("Welcome to the Game - Cows and Bulls")
    rand_num = r.randint(1000, 9999)
    print(rand_num)
    user_input = 0
    number_of_tries = 0
    while user_input != rand_num:
        user_input = int(input("Enter a 4 digit number: "))
        cows = cal_cows(rand_num, user_input)
        bulls = cal_bulls(rand_num, user_input)
        print(str(cows) + " Cows and " + str(bulls) + " Bulls. Try Again!!")
        number_of_tries = number_of_tries+1
    print("Bingo!! You guessed it right in " + str(number_of_tries) + " tries.")