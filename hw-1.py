from math import pi, pow

def print_type(variable):
    return(type(variable))


def do_action(variable):
    if(type(variable)==int):
        return(pow(variable, 2))
    elif(type(variable)==float):
        return(variable+pi)
    elif(type(variable)==bool):
        return(not variable)
    elif(type(variable)==list):
        print(*reversed(variable), sep = ' ')
    else:
        print("Task didn't defined for this type")


variables = [ 42, 45.0, True, False, [16, 9, 43, 65, 97, 0]]


if __name__ == '__main__':
    for i in variables:
        print(print_type(i))
        print(do_action(i))
