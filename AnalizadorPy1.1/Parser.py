from Scanner import *
from Ast import *


class Parser(object):
    def __init__(self, entrada: str):
        self.scan: Scanner = Scanner(entrada)

    def parse(self) -> AST:
        print("PARSE PARSER RETURN PROG")
        return self.Prog()

    def Prog(self) -> AST:
        print("JOIN TO FUNCTION PROG IN PARSE")
        result: AST = self.Expr()
        print("GET TOKEN DE PROG")
        token: Token = self.scan.getToken()
        print("SALI DE GETTOKEN DE PROG")
        if token == 13:
            print("Syntax Error: Expected EOF, found token at column ", token.getCol())
        print("tipo de arbol", type(result))
        return result

    def Expr(self) -> AST:
        print("JOIN TO FUNCTION EXPR IN PARSER")
        arbol: AST = self.Term()
        return self.RestExpre(arbol)

    def Term(self) -> AST:
        print("FUNCTION TERM IN PARSER GET TOKEN")
        token: Token = self.scan.getToken()
        print("FUNCTION TERM IN PARSER GET TOKEN SALÍ VIVO")
        if token.getType() == 15:
            val: float = float(token.getLex())
            print("NUM NODE IN TERM")
            return NumNode(val)
        print("COMPRUEBO QUE PASÓ EL IF DE TERM")

    def RestExpre(self, tree: AST) -> AST:
        print(" RESTEXPRE IN PARSE GET TOKEN")
        token: Token = self.scan.getToken()
        if token.getType() == 1:
            return self.RestExpre(AddNode(tree, self.Term()))
        if token.getType() == 2:
            return self.RestExpre(SubNode(tree, self.Term()))
        if token.getType() == 3:
            return self.RestExpre(TimesNode(tree, self.Term()))
        if token.getType() == 4:
            return self.RestExpre(DivideNode(tree, self.Term()))
        if token.getType() == 7:
            return self.RestExpre(ModuleNode(tree, self.Term()))
        if token.getType() == 8:
            return self.RestExpre(PowerNode(tree, self.Term()))
        if token.getType() == 18:
            return self.RestExpre(LowerNode(tree, self.Term()))
        if token.getType() == 19:
            return self.RestExpre(HighNode(tree, self.Term()))
        if token.getType() == 20:
            return self.RestExpre(LowerEqualNode(tree, self.Term()))
        if token.getType() == 21:
            return self.RestExpre(HigherEqualNode(tree, self.Term()))
        if token.getType() == 22:
            return self.RestExpre(EqualNode(tree, self.Term()))
        if token.getType() == 23:
            return self.RestExpre(NotEqualNode(tree, self.Term()))
        if token.getType() == 24:
            print("TOKEN SUMCONDITION")
            print("EVALUAR TREE ", tree.evaluar())
            return self.RestExpre(SumCondition(tree, self.Term()))
        self.scan.putBackToken()
        print("tipo de arbol", type(tree))
        return tree