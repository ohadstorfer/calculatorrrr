from enum import Enum
import logging
logging.basicConfig(level=logging.DEBUG, filename="log.log",filemode="w", format= "%(asctime)s - %(levelname)s - %(message)s")

logging.info("info")

class Actions(Enum):

    KEFEL =1
    HILUK =2
    HIBUR=3
    HISUR=4
    EXIT=5


def menu():
    while(True):
       
        for act in Actions: 
            print(f'{act.value}:  {act.name}')
        print("")        
            
        user_input = int(input("Select action: "))
        if user_input < 0 or user_input > 5:
            print("")
            print("Only numbers from 0 to 5 are allowed.")
            logging.error(f'user entered an unvalid number: {user_input}')
            print("")
            return
        
        user_selection = Actions(user_input)

        if user_selection == Actions.KEFEL:
            score= x*y
            print("")
            print(score)
            print("")
            logging.debug(f'the score is: {score}')
            tocontinue = input("anything else? only yes or no answers: ")
            print("")
            if tocontinue =="no":return

        if user_selection == Actions.HILUK:
            score = x/y
            print("")
            print(score)
            print("")
            logging.debug(f'the score is: {score}')
            tocontinue = input("anything else? only yes or no answers: ")
            print("")
            if tocontinue =="no":return

        if user_selection == Actions.HIBUR:
            score= x+y
            print("")
            print(score)
            print("")
            logging.debug(f'the score is: {score}')
            tocontinue = input("anything else? only yes or no answers: ")
            print("")
            if tocontinue =="no":return

        if user_selection == Actions.HISUR:
            score=x-y
            print("")
            print(score)
            print("")
            logging.debug(f'the score is: {score}')
            tocontinue = input("anything else? only yes or no answers: ")
            print("")
            if tocontinue =="no":return
            

        if user_selection == Actions.EXIT:
            return    





if __name__ =="__main__":
    x= int(input("enter a number: "))
    y= int(input("enter another number: "))
    logging.debug(f'first number is: {x}, second number is: {y} ')
    print("")
    menu()