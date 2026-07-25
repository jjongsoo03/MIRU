import random
import time
a=1
while True:
    print('let\'s start game! game start!')
    input_number=int(input('choose number from 1 to 30: '))
    bomb=random.randint(1,30)
    time.sleep(2)
    while True:
        if input_number==bomb:
            print('You find the bomb %d시도 만에!'%a)
            break
        else:
            print('miss')
            if bomb>input_number:
                print('up')
            else:
                print('down')
            input_number=int(input('다시 입력하시오: '))
            a=a+1




    if input('To be continued?(y/n): ')=='n':
        print('Game is over')
        break


