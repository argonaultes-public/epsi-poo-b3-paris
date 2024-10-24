import time

pin = '431312'

def check_pin(user_pin):
    if len(pin) != len(user_pin):
        return False
    for i in range(len(pin)):
        time.sleep(1)
        if pin[i] != user_pin[i]:
            return False
    return True

user_pin = input('Your code: ')

print(check_pin(user_pin))
