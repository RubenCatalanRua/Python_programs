while True:
    print('Select your operation: Add (1), Subtract (2), ', end='')
    print('Multiply (3), Divide (4).')

    while True:
        Operator = input()
        if Operator in ('1', '2', '3', '4'):
            break
        else:
            print('Write a valid number.')


    print('Write the first number you want to operate with:')

    while True:
         try:
            Number1 = int(input())
            break
         except ValueError:
            print('Write the first number you want to operate with:')
       


    print('Write the second number:')

    while True:
         try:
            Number2 = int(input())
            break
         except ValueError:
            print('Write the second number:')


    if Operator == '1':
        print('Result: ' + str(Number1 + Number2))
    elif Operator == '2':
        print('Result: ' + str(Number1 - Number2))
    elif Operator == '3':
        print('Result: ' + str(Number1 * Number2))
    elif Operator == '4':
        try:
            print('Result: ' + str(Number1 / Number2))
        except ZeroDivisionError:
            print('Cannot divide by zero.')
