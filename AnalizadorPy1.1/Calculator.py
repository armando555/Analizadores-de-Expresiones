from Parser import *
from Scanner import *
from Ast import *


class Calculator:

    def __init__(self):
        self.memory = 0

    def eval(self, expr: str) -> float:
        print("EVAL CALCULATOR")
        parser = Parser(expr)
        tree: AST = parser.parse()
        print("YA EVALUAR EL ARBOL CREADO")
        print(type(tree))
        result: float = tree.evaluar()
        return result

    def store(self, val: float):
        self.memory = val

    def reCall(self) -> float:
        return self.memory


if __name__ == "__main__":
    try:
        expresion: str = input("Please enter a calculator expression: ")
        calc = Calculator()
        result: float = calc.eval(expresion)
        print("The result is: ", result)
    except ValueError:
        print("Error se fue al carajo :v")