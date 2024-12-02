def print_hello(msg, display_msg):
    display_msg(msg)

print_hello('hello', print)


my_function_display_l = lambda msg: print(f'Msg: {msg}')



def my_function_display(msg):
    print(f'Msg: {msg}')

print_hello('hello', lambda msg: print(f'Msg: {msg}'))