from sly import Lexer

class PolyLexer(Lexer):
    tokens = { NUMBER, ADD, MINUS, TIMES, DIVIDE, LPAREN,
               RPAREN, X, POWER }


    ignore = ' \t'

    NUMBER = '\d*\.?\d+'
    ADD = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    LPAREN = r'[\(\[]'
    RPAREN = r'[\)\]]'
    X = r'X\^[0-9]+'
    POWER = r'\^'

    def NUMBER(self, token):
        if '.' in token.value:
            token.value = float(token.value)
        else:
            token.value = int(token.value)
        return token

    def error(self, token):
        print('Illegal character: `%s`' % token.value[0])
        self.index += 1
