import pytest

def parse_operation(operation):
    from controllers.lexer import PolyLexer
    from controllers.parser import PolyParser

    lexer = PolyLexer()
    parser = PolyParser()

    return parser.parse(lexer.tokenize(operation))

#===============================================================


#================= Basic operations ===========================

def test_one_number():
    result = parse_operation('5')

    assert result == {'X^0': 5}

def test_one_negative_number():
    result = parse_operation('-5')

    assert result == {'X^0': -5}

def test_simple_add_operation():
    result = parse_operation('5 + 4')

    assert result == {'X^0': 9}

def test_add_operation_with_negatives():
    result = parse_operation('-5 + -4')

    assert result == {'X^0': -9}

def test_simple_minus_operation():
    result = parse_operation('5 - 4')

    assert result == {'X^0': 1}

def test_minus_operation_with_negatives():
    result = parse_operation('-5 - -4')

    assert result == {'X^0': -1}

def test_simple_times_operation():
    result = parse_operation('5 * 4')

    assert result == {'X^0': 20}

def test_times_operation_with_negatives():
    result = parse_operation('-5 * -4')

    assert result == {'X^0': 20}

def test_simple_divide_operation():
    result = parse_operation('5 / 5')

    assert result == {'X^0': 1}

def test_divide_operation_with_negatives():
    result = parse_operation('-5 / -5')

    assert result == {'X^0': 1}

def test_parentheses_operation():
    result = parse_operation('(-5 + 2) *(((2+3)*4))')

    assert result == {'X^0': -60}


#=============== identifies elements of a polynomial ================

def test_only_one_X_raised_to_power():
    result = parse_operation('X^4')

    assert result == {'X^4': 1}

def test_negative_X_raised_to_power():
    result = parse_operation('-X^4')

    assert result == {'X^4': -1}

def test_add_Xs_raised_to_power():
    result = parse_operation('X^4 + X^2')

    assert result == {'X^4': 1, 'X^2': 1}

def test_simple_1_polynomial():
    result = parse_operation('X^0 * 5 + 4 * X^1')

    assert result == {'X^0': 5, 'X^1': 4}

def test_simple_2_polynomial():
    result = parse_operation('X^0 * 5 + 4 * X^1 + X^2 * 3.5')

    assert result == {'X^0': 5, 'X^1': 4, 'X^2': 3.5}

def test_complex_1_polynomial():
    result = parse_operation('-X^0 * (5 * 10 + 3) + 4 * -X^1 * (-1 - 1)')

    assert result == {'X^0': -53, 'X^1': 8}

def test_complex_1_polynomial_2():
    result = parse_operation('-X^0 * (5 * 10 + 3) - 4 * -X^1 * (-1 - 1)')

    assert result == {'X^0': -53, 'X^1': -8}

def test_complex_1_polynomial_3():
    result = parse_operation('-10 + -X^0 * (5 * 10 + 3) - (7 + 10) - 4 * -X^1 * (-1 - 1)')

    assert result == {'X^0': -80, 'X^1': -8}

def test_complex_1_polynomial_4():
    result = parse_operation('-1 - X^1 * (-1 - 1) * 8 / 2 + 3 * X^0 - 1')

    assert result == {'X^0': 1, 'X^1': 8}

def test_complex_2_polynomial():
    result = parse_operation('X^0 * 5 + (4 * X^1 + X^2 * 3.5)')

    assert result == {'X^0': 5, 'X^1': 4, 'X^2': 3.5}

def test_complex_2_polynomial_2():
    result = parse_operation('X^0 * 5 + (4 * X^1 + X^2 * 3.5) - 2 + (3 + 2) * X^2')

    assert result == {'X^0': 3, 'X^1': 4, 'X^2': 8.5}
