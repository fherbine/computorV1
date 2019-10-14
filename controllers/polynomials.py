AUTHORIZED_POLYNOMS = ['X^0', 'X^1', 'X^2']

class Solver:
    pass

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

        self._check_operation_conformity(self.reduced_form)

        self._degree = value

    def dispatch_reduced_form(self):
        output = ''

        for degree, value in self.reduced_form.items():
            formula = '' if not output else ' '

            if not value:
                continue

            if degree == 'X^0':
                formula = f'{value}'
            else:
                if value < 0:
                    formula += '- '
                else:
                    formula += '+ '
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
