AUTHORIZED_POLYNOMS = ['X^0', 'X^1', 'X^2']

# Avoid result like `-0.0`
sanitize_result = lambda n: n if n else 0

class Solver:
    def solve(self, null_result_polynom, degree):
        solution = getattr(self, '_solve_degree_%s' % degree)(
            null_result_polynom
        )
        n, scope = solution[:2]
        print(f'There is {n} solution(s) in {scope}.')
        print(*map(sanitize_result, solution[2:]), sep='\n')

    def _solve_degree_0(self, null_result_polynom):
        null_result = null_result_polynom.get('X^0', 0)

        if not null_result:
            return ('unique', 'real', null_result)
        return ('no', 'real')

    def _solve_degree_1(self, null_result_polynom):
        """Solve one degree polynomial equation w/null result.

            xa + b = 0
        <=> x = -b / a
        """
        a = null_result_polynom.get('X^1', 0)
        b = null_result_polynom.get('X^0', 0)

        return ('unique', 'real', -b / a)

    def _solve_degree_2(self, null_result_polynom):
        """Solve second degree polynomial equation w/null result.

        ð = b² - 4ac

        if ð == 0:
            one solution on real:
            x1 = x2 = -b / (2a)
        elif ð > 0:
            two solution on real:
            x1 = (-b - sqrt(ð)) / (2a) and x2 = (-b + sqrt(ð)) / (2a)
        else:
            two solution on complex:
            x1 = (-b - i*sqrt(|ð|)) / (2a) and x2 = (-b + i*sqrt(|ð|)) / (2a)
        """
        a = null_result_polynom.get('X^2', 0)
        b = null_result_polynom.get('X^1', 0)
        c = null_result_polynom.get('X^0', 0)

        discriminant = b**2 - 4 * a * c
        # Note: I'm not using math.sqrt because it's prohibited so I raised to
        # .5 power.
        discriminant_sqrt = discriminant**.5

        if not discriminant:
            return ('one', 'real', -b / (2*a))
        elif discriminant > 0:
            return (
                'two',
                'real',
                (-b - discriminant_sqrt) / (2*a),
                (-b + discriminant_sqrt) / (2*a),
            )
        else:
            # Complex solutions
            return (
                'two',
                'complex',
                complex(-b, -abs(discriminant_sqrt)) / (2*a),
                complex(-b, abs(discriminant_sqrt)) / (2*a),
            )


class PolyCalc:
    def __init__(self):
        self._degree = 0
        self.reduced_form = {}

    def simplify(self, left_operation, right_operation):
        null_result_polynom = {}

        for polynom in AUTHORIZED_POLYNOMS:
            null_result_polynom[polynom] = (
                left_operation.get(polynom, 0)
                - right_operation.get(polynom, 0)
            )

        self.reduced_form = null_result_polynom
        self._check_operation_authorized_degree(left_operation)
        self._check_operation_authorized_degree(right_operation)

    def solve(self):
        Solver().solve(self.reduced_form, self.degree)

    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        try:
            value = int(value)
        except:
            raise ValueError('Polynomial degree must be integer')

        if value < 0 or value > 2:
            raise ValueError('Polynomial degree must be in range [0;2].')

        self._degree = value
        self._check_operation_conformity(self.reduced_form)

    def dispatch_reduced_form(self):
        output = ''
        reduced_form = self.reduced_form

        for degree, value in reduced_form.items():
            formula = '' if not output else ' '

            if not value and (any(reduced_form.values()) or degree != 'X^0'):
                continue

            if degree == 'X^0':
                formula = f'{value}'
            else:
                if value < 0:
                    formula += '- ' if formula else '-'
                else:
                    formula += '+ ' if formula else ''
                formula += str(abs(value))

                if degree == 'X^1':
                    formula += f' * X'
                elif degree == 'X^2':
                    formula += f' * X^2'

            output += formula

        print(f'Reduced form: {output} = 0')

    def _check_operation_conformity(self, operation):
        for degree, times in operation.items():
            int_degree = int(degree.split('^')[-1])

            if times == 0:
                continue

            if int_degree > self.degree:
                raise Exception('Operaion is not conform with typed degree.')

    def _check_operation_authorized_degree(self, operation):
        for degree, times in operation.items():
            if times == 0:
                continue

            if degree not in AUTHORIZED_POLYNOMS:
                raise Exception('Operaion is strictly greater than 2.')
