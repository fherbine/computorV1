def _calculator_init(equation):
    from controllers.lexer import PolyLexer
    from controllers.parser import PolyParser
    from controllers.polynomials import PolyCalc

    calculator = PolyCalc()
    lexer = PolyLexer()
    parser = PolyParser()

    splitted_equation = equation.split('=')
    left_operation, result = splitted_equation

    left_operation = parser.parse(lexer.tokenize(left_operation))
    result = parser.parse(lexer.tokenize(result))
    calculator.simplify(left_operation, result)
    return calculator

def get_reduced_form(equation):
    calculator = _calculator_init(equation)

    reduced_form = calculator.dispatch_reduced_form()

    return reduced_form

def get_result(equation, degree):
    calculator = _calculator_init(equation)

    calculator.degree = degree
    solution = calculator.solve()

    return solution[1:]

#===============================================================


#===================== getting reduced form ===================

def test_reduced_simple_0_degree_eq():
    equation = '0=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 0 = 0'

def test_reduced_simple_0_degree_eq2():
    equation = '42=42'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 0 = 0'

def test_reduced_simple_1_degree_eq():
    equation = 'X^1=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 1 * X = 0'

def test_reduced_simple_1_degree_eq2():
    equation = 'X^1 * 2=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 2 * X = 0'

def test_reduced_simple_1_degree_eq3():
    equation = 'X^1 + 1=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 1 + 1 * X = 0'

def test_reduced_simple_1_degree_eq4():
    equation = 'X^1 * 2 + 1=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 1 + 2 * X = 0'

def test_reduced_1_degree_eq_with_negatives():
    equation = '-X^1=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: -1 * X = 0'

def test_reduced_1_degree_eq_with_negatives2():
    equation = '-1 * X^1=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: -1 * X = 0'

def test_reduced_1_degree_eq_with_negatives3():
    equation = '-1 * -X^1=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 1 * X = 0'

def test_reduced_1_degree_eq_with_negatives4():
    equation = '-1 * -X^1=2'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: -2 + 1 * X = 0'

def test_reduced_1_degree_eq_with_negatives5():
    equation = '-1 * -X^1 + 2=2'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 1 * X = 0'

def test_reduced_1_degree_eq_with_negatives6():
    equation = '-1 * -X^1 + -2=-2'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 1 * X = 0'

def test_reduced_simple_2_degree_eq():
    equation = 'X^2=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 1 * X^2 = 0'

def test_reduced_simple_2_degree_eq2():
    equation = '2 * X^2  * 4=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 8 * X^2 = 0'

def test_reduced_simple_2_degree_eq2():
    equation = '2 * X^2  * 4 + X^1 + X^2=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 1 * X + 9 * X^2 = 0'

def test_reduced_2_degree_eq2_with_negatives():
    equation = '-X^2=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: -1 * X^2 = 0'

def test_reduced_2_degree_eq2_with_negatives2():
    equation = '-X^2 + X^1=42'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: -42 + 1 * X - 1 * X^2 = 0'

def test_reduced_2_degree_eq2_with_negatives3():
    equation = 'X^2 - X^1=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: -1 * X + 1 * X^2 = 0'

def test_reduced_2_degree_eq2_with_negatives4():
    equation = 'X^2 + -X^1=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: -1 * X + 1 * X^2 = 0'

def test_reduced_2_degree_eq2_with_negatives5():
    equation = 'X^2 - -X^1=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: 1 * X + 1 * X^2 = 0'

def test_reduced_2_degree_eq2_with_negatives6():
    equation = '-X^2 - X^1=0'

    reduced_form = get_reduced_form(equation)

    assert reduced_form == 'Reduced form: -1 * X - 1 * X^2 = 0'


#===================== Solve equation ===================

def test_solve_0_degrees_eq():
    equation = '0=0'

    result = get_result(equation, 0)

    assert result == (0,)

def test_solve_0_degrees_eq2():
    equation = '42=42'

    result = get_result(equation, 0)

    assert result == (0,)

def test_solve_0_degrees_eq3():
    equation = '42=0'

    result = get_result(equation, 0)

    assert result == tuple()

def test_solve_1_degrees_eq():
    equation = 'X^1=0'

    result = get_result(equation, 1)

    assert result == (0,)

def test_solve_1_degrees_eq2():
    equation = 'X^1 * 3 =0'

    result = get_result(equation, 1)

    assert result == (0,)

def test_solve_1_degrees_eq3():
    equation = 'X^1 = -42'

    result = get_result(equation, 1)

    assert result == (-42,)

def test_solve_1_degrees_eq4():
    equation = 'X^1 -42 = -42'

    result = get_result(equation, 1)

    assert result == (0,)

def test_solve_1_degrees_eq5():
    equation = 'X^1 + 21 + X^1 = 42'

    result = get_result(equation, 1)

    assert result == (10.5,)

def test_solve_1_degrees_eq6():
    equation = 'X^1 + 20 * 2 + X^1 = 42'

    result = get_result(equation, 1)

    assert result == (1,)

def test_solve_1_degrees_eq7():
    equation = '1.5 * X^1 * 2 + 20 * 2 + X^1 = 42'

    result = get_result(equation, 1)

    assert result == (0.5,)

def test_solve_2_degrees_eq():
    equation = 'X^2=0'

    result = get_result(equation, 2)

    assert result == (0,)

def test_solve_2_degrees_eq2():
    equation = 'X^2 - 4 =0'

    result = get_result(equation, 2)

    assert result == (-2, 2)

def test_solve_2_degrees_eq3():
    equation = 'X^2 + X^1 =2'

    result = get_result(equation, 2)

    assert result == (-2, 1)

def test_solve_2_degrees_eq4():
    equation = 'X^2 + 1.5 * 2 * X^1 =-2'

    result = get_result(equation, 2)

    assert result == (-2, -1)

def test_solve_2_degrees_eq5():
    equation = '4 * X^2 + X^1 + X^1 + X^1 * 2 + 1 = 0'

    result = get_result(equation, 2)

    assert result == (-0.5,)

def test_solve_2_degrees_eq_complex_result():
    equation = 'X^2 = -49'

    result = get_result(equation, 2)

    assert result == ('-7i', '7i')

def test_solve_2_degrees_eq_complex_result2():
    equation = 'X^2 + X^1 * 4 + 20 = 0'

    result = get_result(equation, 2)

    assert result == ('(-2 - 4i)', '(-2 + 4i)')
