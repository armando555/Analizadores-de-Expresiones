from enum import Enum


class TokenType(Enum):
    add = 1
    sub = 2
    times = 3
    divide = 4
    lparen = 5
    rparen = 6
    module = 7
    potencia = 8
    log = 9
    sen = 10
    cos = 11
    sqrt = 12
    eof = 13
    keyword = 14
    number = 15
    identifier = 16
    unrecognized = 17
    lower = 18
    higher = 19
    lowerEqual = 20
    higherEqual = 21
    equals = 22
    different = 23
    sumCondition = 24
    separate = 25
    loopCondition = 26


class Token(object):
    def __init__(self, typ: TokenType, line: int, col: int):
        self.typ: TokenType = typ
        self.line: int = line
        self.col: int = col

    def getType(self):
        return self.typ

    def getCol(self):
        return self.col

    def getLine(self):
        return self.line

    def getLex(self):
        return ""


class LexicalToken(Token):
    def __init__(self, typ: TokenType, lex: str, line: int, col: int):
        Token.__init__(self, typ, line, col)
        self.lexeme: str = lex

    def getLex(self):
        return self.lexeme
