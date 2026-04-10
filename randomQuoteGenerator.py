import random
quote=['those who fly hard fall hard',
       'noticed a man is never late for his funeral',
       "glory comes to those who seek it",
       "those who seek will get"
       ]
print("WLCOME TO THIS RANDOM QUOTE GENERATOR!!!")
choice=input("click enter to generate a quote and click on q to quit: ")
if choice=="q":
    print("thanks for using!!!!!")
else:
    print(random.choice(quote))
    choice1=input("do you want to continue: ")
    while choice1!="q":
       print(random.choice(quote))
       choice1=input("do you want to continue: ")
    print("thanks for using!")