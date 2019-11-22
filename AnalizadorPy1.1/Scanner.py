from Ast import *
from Token import *
import time

class Scanner:
    def __init__(self, entrada: str):
        self.entrada = entrada
        self.needToken: bool = True
        self.lastToken: Token = None
        self.lineaCount: int = 1
        self.colCount: int = -1

    def putBackToken(self):
        print("PUTBACKTOKEN IN SCANNER")
        time.sleep(3)
        self.needToken = False

    def isDigit(self, c: str) -> bool:
        try:
            float(c)
            valor: bool = True
            return valor
        except ValueError:
            valor: bool = False
            return valor

    def isLetter(self, c: str) -> bool:
        return c in "abcdefghijklmnopqrstuvxywzñABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    def getToken(self) -> Token:
        if self.entrada != "":
            self.needToken = True
        if not self.needToken:
            print("ENTRE AL NOT NEED TOKEN")
            self.needToken = True
            return self.lastToken
        token: Token
        state: int = 0
        tType: TokenType
        column: int
        line: int
        found: bool = False
        print("Entrada SIN CORTAR= ", self.entrada)
        if len(self.entrada) > 1:
            c: str = self.entrada[0]
            num: str = ""
            if self.isDigit(c):
                while self.isDigit(c):
                    num += c
                    self.entrada = self.entrada[1:]
                    c = self.entrada[0]
            elif (c == ">" and self.entrada[1] == "=") or (c == "<" and self.entrada[1] == "=") or (c == "=" and self.entrada[1] == "=") or (c == "!" and self.entrada[1] == "="):
                c += self.entrada[1]
                print("DOBLE SYMBOL")
                self.entrada = self.entrada[2:]
            else:
                self.entrada = self.entrada[1:]
            if num != "":
                c = num
        elif len(self.entrada) == 1:
            c: str = self.entrada[0]
            self.entrada = ""
        print(len(self.entrada))
        print("C= ", c)
        print("Entrada Cortada= ", self.entrada)
        while not found:
            self.colCount += 1
            column = self.colCount
            line = self.lineaCount
            if self.isLetter(c):
                state = 1
            elif self.isDigit(c):
                state = 2
            elif c == "+":
                state = 3
            elif c == "-":
                state = 4
            elif c == "*":
                state = 5
            elif c == "/":
                state = 6
            elif c == "(":
                state = 7
            elif c == ")":
                state = 8
            elif c == "%":
                state = 9
            elif c == "^":
                state = 10
            elif c == "<":
                print("SYMBOL MENOR")
                state = 11
            elif c == ">":
                print("SYMBOL MAYOR")
                state = 12
            elif c == "<=":
                state = 13
            elif c == ">=":
                state = 14
            elif c == "==":
                state = 15
            elif c == "!=":
                state = 16
            elif c == "?":
                state = 17
            elif c == ":":
                state = 18
            elif self.entrada == "":
                tType = None
                found = True
            else:
                print("Unrecognized Token ")
            if state == 1:
                if self.isLetter(c):
                    tType = 16
                    found = True
            elif state == 2:
                if self.isDigit(c):
                    tType = 15
                    found = True
            elif state == 3:
                tType = 1
                found = True
            elif state == 4:
                tType = 2
                found = True
            elif state == 5:
                tType = 3
                found = True
            elif state == 6:
                tType = 4
                found = True
            elif state == 7:
                tType = 5
                found = True
            elif state == 8:
                tType = 6
                found = True
            elif state == 9:
                tType = 7
                found = True
            elif state == 10:
                tType = 8
                found = True
            elif state == 11:
                tType = 18
                found = True
            elif state == 12:
                tType = 19
                found = True
            elif state == 13:
                found = True
                tType = 20
            elif state == 14:
                tType = 21
                found = True
            elif state == 15:
                tType = 22
                found = True
            elif state == 16:
                tType = 23
                found = True
            elif state == 17:
                tType = 24
                found = True
            elif state == 18:
                tType = 25
                found = True
            if not found:
                if len(self.entrada) > 1:
                    c: str = self.entrada[0]
                    self.entrada = self.entrada[1:]
                elif len(self.entrada) == 1:
                    c: str = self.entrada[0]
                else:
                    c: str = " "
        if c != " ":
            self.putBackToken()
        if tType != 15 and tType != 18 and tType != 19 and tType != 20 and tType != 21 and tType != 22 and tType != 23 and tType != 25:
            token = Token(tType, line, column)
        else:
            token = LexicalToken(tType, c, line, column)
        print("TOKEN TYPE", token.getType())
        self.lastToken = token
        return token