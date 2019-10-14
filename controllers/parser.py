from sly import Parser

from controllers.lexer import PolyLexer

class PolyParser(Parser):
    tokens = PolyLexer.tokens

    precedence = (
        ('left', ADD, MINUS),
        ('left', X),
        ('left', TIMES, DIVIDE),
        ('left', POWER),
    #    ('right', UMINUS)
    )

    def __init__(self):
        self.degrees = {}

    @_('xexpr')
    def statement(self, parsed):
        # DEBUG
        #print(parsed.expr)
        print(self.degrees)
        self.degrees = {}

    @_('expr')
    def statement(self, parsed):
        self.degrees.setdefault('X^0', [])
        self.degrees['X^0'].append(parsed.expr)
        print(self.degrees)

    @_('xexpr MINUS expr',
       'xexpr ADD expr',
       'expr MINUS xexpr',
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

    #@_('xexpr TIMES xexpr')
    #def

    @_('expr TIMES X',
       'X TIMES expr')
    def xexpr(self, parsed):
        self.degrees.setdefault(parsed.X, [])
        self.degrees[parsed.X].append(parsed.expr)
        print('X:', parsed.X, parsed.expr)
        return (parsed.X, parsed.expr, len(self.degrees[parsed.X]) - 1)

    @_('expr DIVIDE X',
       'X DIVIDE expr')
    def xexpr(self, parsed):
        self.degrees.setdefault(parsed.X, [])
        self.degrees[parsed.X].append(1 / parsed.expr)
        return (parsed.X, 1 / parsed.expr, len(self.degrees[parsed.X]) - 1)

    @_('expr TIMES expr')
    def expr(self, parsed):
        print('TIMES', parsed.expr0, parsed.expr1)
        return parsed.expr0 * parsed.expr1

    @_('expr DIVIDE expr')
    def expr(self, parsed):
        return parsed.expr0 / parsed.expr1

    @_('expr POWER expr')
    def expr(self, parsed):
        return parsed.expr0 ** parsed.expr1

    @_('expr MINUS expr')
    def expr(self, parsed):
        print('MINUS', parsed.expr0, parsed.expr1)
        return parsed.expr0 - parsed.expr1

    @_('expr ADD expr')
    def expr(self, parsed):
        print('ADD', parsed.expr0, parsed.expr1)
        return parsed.expr0 + parsed.expr1

    @_('NUMBER')
    def expr(self, parsed):
        return parsed.NUMBER

    def error(self, parsed):
        print('err')
