from time import *
import random

def mistake(para, user):
    error = 0
    for x in range(len(para)):
        try:
            if para[x] != user[x]:
                error += 1
        except:
            error += 1
    return error
    
    
def speed_time(start_time, end_time, user_input, ):
    time_delay = end_time - start_time
    time_round = round(time_delay, 2)
    speed = len(user_input)/time_round
    return round(speed)
    


text = ['this is a dummy paragraph to test your typing speed and calculate with word per second',
        "this story is very interesting and i can pay for your movie because its simply awesome",
        "my name is adil shabab and i am from malappuram padikkal and i am 17 years old and i completed my higher study in 2021",
        'now i am studying python full stack web developing from techolas technologies calicut']


selected_text = random.choice(text)
while True:
    ready = input("are you ready to test: yes / no :  ")
    if ready.lower() == 'yes':
        print()
        print('******************************** typing speed ***********************************')
        print()
        print(selected_text)
        print()
        print()


        start_time = time()
        user_input = input('Enter this paragraph:   ')
        end_time = time()


        print('Speed : ',speed_time(start_time,end_time,user_input), "  w/sec")
        print('Error : ', mistake(selected_text,user_input))
    elif ready.lower() == 'no':
        print(" Thank You ")
    else:
        print(' Wrong input ')
