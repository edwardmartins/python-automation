# Exceptions (exceptions are for user errors)
# --------------------------------------------------------
def boxPrint(symbol, width, height):
    # Raising different exceptions to stop the program in case the paremeters are wrong
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

boxPrint('*', 5, 5)

# Assertions (assertions are for programmer errors)
# --------------------------------------------------------
market_2nd = {'ns': 'green', 'ew': 'yellow'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # Always has to exist one light that is red in one direction
    assert 'red' in intersection.values(), 'Neither light is red' # if the assert fails the program crash

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)

# Priniting a Traceback
# --------------------------------------------------------
import traceback
try:
    raise Exception('This is the error message')
except: # we can write the traceback in a file
    error_File = open('error_log.txt', 'a')
    error_File.write(traceback.format_exc())
    error_File.close()
    print('The traceback info was written in error_log.txt')

# Logging
# --------------------------------------------------------
import logging

logging.basicConfig(filename = 'program_log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # disables all logging messages

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')