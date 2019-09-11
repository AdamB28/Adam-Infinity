import time

def calc():
    answer = input("\n~~~\nWelcome to the Simple Calculator!\nA calculator for people familiar with Python!\n\
Type \"q\" to quit.\n\n~~~\n\nPlease enter your sum:\n")
    if answer == "q":
        print("Goodbye!")
        time.sleep(1)
        quit()
    else:
        answer = eval(answer)
        return answer

def start():
    answer1 = calc()
    print(answer1, "\n")
    time.sleep(1)
    start()

start()
              
