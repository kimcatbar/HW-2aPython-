def calculator(input):
    try:
        exec(input)
    except ZeroDivisionError:#if dividing by 0 error is detected
       return("You shall not pass!!!! Division by 0 not allowed")
    answer=eval(input)#evaluate as string
    make_int=float(answer)#turn string into float
    return str(make_int)#return as string
