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

#user_pin = input('Your code: ')


def break_the_code():
    pin_list = 6 * ['0']
    # pour chaque position
    for idx in range(len(pin_list)):
        # tourner la roue en position idx
        for digit in range(10):
            pin_list[idx] = str(digit)
            pin = ''.join(pin_list)
            start_time = time.time()
            result = check_pin(pin)
            end_time = time.time()
            time_elapsed = int(end_time - start_time)
            print(f'{time_elapsed} : {pin_list} : {result}')
            if time_elapsed > 1 + idx or result:
                break
    return pin

print(break_the_code())