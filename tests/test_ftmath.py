from controllers.ft_math import ft_abs, ft_power, ft_sqrt, Complex

from math import sqrt


#=========== abs func ============

def test_abs_positive_int():
    assert abs(128) == ft_abs(128)

def test_abs_negative_int():
    assert abs(-128) == ft_abs(-128)

def test_abs_positive_float():
    assert abs(128.256) == ft_abs(128.256)

def test_abs_negative_float():
    assert abs(-128.256) == ft_abs(-128.256)


#========== power func ===========

def test_n_power_0():
    assert 4**0 == ft_power(4, 0)

def test_n_power_1():
    assert 4**1 == ft_power(4, 1)

def test_n_power_n2():
    assert 4**16 == ft_power(4, 16)

#============= sqrt =============

def test_sqrt_int():
    assert sqrt(24025) == ft_sqrt(24025)

def test_sqrt_float():
    assert round(sqrt(24026), 4) == round(ft_sqrt(24026), 4)

#============ complex ============

def test_complex_instanciation():
    c1 = complex(4, 2)
    c2 = Complex(4, 2)

    c1_repr = c1.real, c1.imag
    c2_repr = c2.r, c2.i

    assert c1_repr == c2_repr

def test_complex_addition_real():
    c1 = complex(4, 2) + 3
    c2 = Complex(4, 2) + 3

    c1_repr = c1.real, c1.imag
    c2_repr = c2.r, c2.i

    assert c1_repr == c2_repr

def test_complex_addition_complex():
    c1 = complex(4, 2) + complex(2, 1)
    c2 = Complex(4, 2) + Complex(2, 1)

    c1_repr = c1.real, c1.imag
    c2_repr = c2.r, c2.i

    assert c1_repr == c2_repr

def test_complex_sub_real():
    c1 = complex(4, 2) - 3
    c2 = Complex(4, 2) - 3

    c1_repr = c1.real, c1.imag
    c2_repr = c2.r, c2.i

    assert c1_repr == c2_repr

def test_complex_sub_complex():
    c1 = complex(4, 2) - complex(2, 1)
    c2 = Complex(4, 2) - Complex(2, 1)

    c1_repr = c1.real, c1.imag
    c2_repr = c2.r, c2.i

    assert c1_repr == c2_repr

def test_complex_mul_real():
    c1 = complex(4, 2) * 21
    c2 = Complex(4, 2) * 21

    c1_repr = c1.real, c1.imag
    c2_repr = c2.r, c2.i

    assert c1_repr == c2_repr

def test_complex_div_real():
    c1 = complex(4, 2) / 2
    c2 = Complex(4, 2) / 2

    c1_repr = c1.real, c1.imag
    c2_repr = c2.r, c2.i

    assert c1_repr == c2_repr
