import logging

logging.basicConfig(filename='mylog.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(funcName)s : %(message)s')


def count_the_numbers():

    num1 = input('Input first number: ')
    char = input('Input operation (+, -, * or /): ')
    num2 = input('Input second number: ')
    logging.info(f'First number: {num1}, Second number: {num2}, Operator: {char}')

    if not num1.isdigit() or not num2.isdigit():
        error = f'ValueError: could not convert string to int/float: First number - {num1}, Second number - {num2}'
        logging.error(error)
        return error
    elif num1.isdigit() and num2.isdigit():
        num1, num2 = int(num1), int(num2)
        if char == '+':
            result = num1 + num2
            logging.info(f'result: {result}')
            return result
        elif char == '-':
            result = num1 - num2
            logging.info(f'result: {result}')
            return result
        elif char == '*':
            result = num1 * num2
            logging.info(f'result: {result}')
            return result
        elif char == '/':
            if not num2 == 0:
                result = num1 / num2
                logging.info(f'result: {result}')
                return result
            else:
                error = 'Cannot divide by zero'
                logging.error('Division by zero')
                return error
        else:
            error = f'Your operation input is "{char}", pleas input (+, -, * or /)'
            logging.error(f'Invalid operator: {char}')
            return error


res = count_the_numbers()
print(res)
