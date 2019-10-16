import sys

from controllers.lexer import PolyLexer
from controllers.parser import PolyParser
from controllers.polynomials import PolyCalc


def usage():
    print('====== USAGE ======\n')
    print('`python3 main.py <polynomial_equation>`\n')
    print('NB: empty string is not allowed for the equation.')

def check_sysargs():
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)

def invalid_equation():
    print('The polynomial equation is invalid ! Exiting.')
    sys.exit(0)


if __name__ == '__main__':
    lexer = PolyLexer()
    parser = PolyParser()
    calculator = PolyCalc()

    check_sysargs()
    splitted_equation = sys.argv[-1].split('=')

    if len(splitted_equation) != 2:
        invalid_equation()

    left_operation, result = splitted_equation

    if not left_operation or not result:
        invalid_equation()

    try:
        left_operation = parser.parse(lexer.tokenize(left_operation))
        result = parser.parse(lexer.tokenize(result))

        calculator.simplify(left_operation, result)
        print(calculator.dispatch_reduced_form())

        while True:
            degree = input('Polynomial degree: ')
            try:
                calculator.degree = degree
                break
            except Exception as e:
                print(e)

        print(*calculator.solve(), sep='\n')

    except Exception as e:
        print(e)
        invalid_equation()
