"""Own math module.

Contained functions are:
- ft_abs(n): return the absolute value of n.
- ft_power(n, p): return n raised to power p
- ft_sqrt(n): return the square root of n. Should be improved !

Contained objects are:
- Complex(r, i): Represents a coplex number.
"""

def ft_abs(n):
    return -n if n < 0 else n


def ft_power(n, p):
    total = 1

    for _ in range(p):
        total *= n

    return total


def ft_sqrt(n):
    if n < 0:
        raise ValueError('Square root function is not defined for negatives.')
    i = 0

    # Ugly way to calculate sqrt :/

    while (i+1) * (i+1) <= n:
        i += 1

    while (i+.1) * (i+.1) <= n:
        i+= .1

    while (i+.01) * (i+.01) <= n:
        i += .01

    while (i+.001) * (i+.001) <= n:
        i += .001

    while (i+.0001) * (i+.0001) <= n:
        i += .0001

    return i


class Complex:
    def __init__(self, r, i):
        self._r = r
        self._i = i

    @property
    def r(self):
        if not isinstance(self._r, int):
            return int(self._r) if self._r.is_integer() else self._r
        return self._r

    @r.setter
    def r(self, value):
        self._r = value

    @property
    def i(self):
        if not isinstance(self._i, int):
            return int(self._i) if self._i.is_integer() else self._i
        return self._i

    @i.setter
    def i(self, value):
        self._i = value

    def __repr__(self):
        return "'%s'" % self.__str__()

    def __str__(self):
        r, i = self.r, self.i
        separator = '+' if i >= 0 else '-'
        i = ft_abs(i)

        if not i:
            return f'{r}'

        if not r:
            if separator == '+':
                separator = ''

            return f'{separator}{i}i'

        return f'({r} {separator} {i}i)'

    def __add__(self, number):
        r = self.r
        i = self.i

        if isinstance(number, Complex):
            r = self.r + number.r
            i = self.i + number.i
            return Complex(r, i)
        return Complex(r + number, i)

    def __sub__(self, number):
        r = self.r
        i = self.i

        if isinstance(number, Complex):
            r = self.r - number.r
            i = self.i - number.i
            return Complex(r, i)
        return Complex(r - number, i)

    def __mul__(self, number):
        if isinstance(number, Complex):
            # Not implemented yet
            raise TypeError(
                'Cannot multiplie complex numbers between them.'
            )
        return Complex(self.r * number, self.i * number)

    def __truediv__(self, number):
        if isinstance(number, Complex):
            # Not implemented yet
            raise TypeError(
                'Cannot divide complex numbers between them.'
            )
        return Complex(self.r / number, self.i / number)
