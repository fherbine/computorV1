from sly import Parser

from controllers.lexer import PolyLexer

class PolyParser(Parser):
    tokens = PolyLexer.tokens

    precedence = (
        ('left', ADD, MINUS),
        ('left', X),
        ('left', TIMES, DIVIDE),
        ('left', POWER),
        ('right', UMINUS),
        ('right', UMINX)
    )

    def __init__(self):
        self.degrees = {}

    def filter_results(self):
        output = {}
        degrees = self.degrees
        for degree, times in degrees.items():
            output[degree] = sum(times)

        self.degrees = {}

        return output

    @_('xexpr')
    def statement(self, parsed):
        return self.filter_results()

    @_('expr')
    def statement(self, parsed):
        self.degrees.setdefault('X^0', [])
        self.degrees['X^0'].append(parsed.expr)

        return self.filter_results()

    @_('X')
    def statement(self, parsed):
        return {parsed.X: 1}


    @_('xexpr MINUS expr')
    def expr(self, parsed):
        return -parsed.expr

    @_('expr MINUS xexpr')
    def expr(self, parsed):
        x, coef, degree_index = parsed.xexpr
        coef = -coef
        self.degrees[x][degree_index] = coef
        return parsed.expr

    @_('xexpr ADD X',
       'X ADD xexpr')
    def xexpr(self, parsed):
        self.degrees.setdefault(parsed.X, [])
        self.degrees[parsed.X].append(1)
        coef, degree_index = 1, len(self.degrees[parsed.X]) - 1

        return (parsed.X, coef, degree_index)

    @_('X MINUS xexpr')
    def xexpr(self, parsed):
        x, coef, degree_index = parsed.xexpr
        coef = -coef
        self.degrees[x][degree_index] = coef
        self.degrees.setdefault(parsed.X, [])
        self.degrees[parsed.X].append(1)
        return (x, coef, degree_index)

    @_('xexpr MINUS X')
    def xexpr(self, parsed):
        self.degrees.setdefault(parsed.X, [])
        self.degrees[parsed.X].append(-1)

        return (parsed.X, -1, len(self.degrees[parsed.X]) - 1)

    @_('xexpr ADD expr',
       'expr ADD xexpr')
    def expr(self, parsed):
        """ Used if an xexpr (made of an unknown raised to the power) collide a
        `+` or a `-`. In this case, we just have to return expr"""
        return parsed.expr

    @_('expr TIMES xexpr',
       'xexpr TIMES expr')
    def xexpr(self, parsed):
        x, coef, degree_index = parsed.xexpr
        coef *= parsed.expr
        self.degrees[x][degree_index] = coef
        return (x, coef, degree_index)

    #@_('expr DIVIDE xexpr')

    @_('xexpr DIVIDE expr')
    def xexpr(self, parsed):
        x, coef, degree_index = parsed.xexpr
        coef = coef / parsed.expr
        self.degrees[x][degree_index] = coef
        return (x, coef, degree_index)

    @_('xexpr ADD xexpr')
    def xexpr(self, parsed):
        return parsed.xexpr1

    @_('xexpr MINUS xexpr')
    def xexpr(self, parsed):
        x, coef, degree_index = parsed.xexpr1
        coef = -coef
        self.degrees[x][degree_index] = coef
        return (x, coef, degree_index)

    @_('expr TIMES X',
       'X TIMES expr')
    def xexpr(self, parsed):
        self.degrees.setdefault(parsed.X, [])
        self.degrees[parsed.X].append(parsed.expr)
        return (parsed.X, parsed.expr, len(self.degrees[parsed.X]) - 1)

    @_('expr DIVIDE X',
       'X DIVIDE expr')
    def xexpr(self, parsed):
        self.degrees.setdefault(parsed.X, [])
        self.degrees[parsed.X].append(1 / parsed.expr)
        return (parsed.X, 1 / parsed.expr, len(self.degrees[parsed.X]) - 1)

    @_('X ADD expr',
       'expr ADD X')
    def expr(self, parsed):
        self.degrees.setdefault(parsed.X, [])
        self.degrees[parsed.X].append(1)
        return parsed.expr

    @_('X MINUS expr',
       'expr MINUS X')
    def expr(self, parsed):
        self.degrees.setdefault(parsed.X, [])
        self.degrees[parsed.X].append(1)
        return -parsed.expr

    @_('X ADD X')
    def xexpr(self, parsed):
        x0, x1 = parsed.X0, parsed.X1
        self.degrees.setdefault(x0, [])
        self.degrees[x0].append(1)

        self.degrees.setdefault(x1, [])
        self.degrees[x1].append(1)
        coef1, degree_index1 = 1, len(self.degrees[x1]) - 1

        return (x1, coef1, degree_index1)

    @_('X MINUS X')
    def xexpr(self, parsed):
        x0, x1 = parsed.X0, parsed.X1
        self.degrees.setdefault(x0, [])
        self.degrees[x0].append(1)

        self.degrees.setdefault(x1, [])
        self.degrees[x1].append(-1)
        coef1, degree_index1 = -1, len(self.degrees[x1]) - 1

        return (x1, coef1, degree_index1)

    @_('MINUS X %prec UMINX')
    def xexpr(self, parsed):
        self.degrees.setdefault(parsed.X, [])
        self.degrees[parsed.X].append(-1)
        return (parsed.X, -1, len(self.degrees[parsed.X]) - 1)

    @_('expr TIMES expr')
    def expr(self, parsed):
        return parsed.expr0 * parsed.expr1

    @_('expr DIVIDE expr')
    def expr(self, parsed):
        return parsed.expr0 / parsed.expr1

    @_('expr POWER expr')
    def expr(self, parsed):
        return parsed.expr0 ** parsed.expr1

    @_('expr MINUS expr')
    def expr(self, parsed):
        return parsed.expr0 - parsed.expr1

    @_('expr ADD expr')
    def expr(self, parsed):
        return parsed.expr0 + parsed.expr1

    @_('MINUS expr %prec UMINUS')
    def expr(self, parsed):
        return -parsed.expr

    @_('LPAREN expr RPAREN')
    def expr(self, parsed):
        return parsed.expr

    @_('LPAREN xexpr RPAREN')
    def xexpr(self, parsed):
        return parsed.xexpr

    @_('NUMBER')
    def expr(self, parsed):
        return parsed.NUMBER

    def error(self, parsed):
        raise SyntaxError('An error occurs while parsing.')
