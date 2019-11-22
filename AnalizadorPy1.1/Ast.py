

class AST:
    def __init__(self):
        print("CONTRUCTOR AST")

    def evaluar(self) -> float:
        pass


class BinaryNode(AST):
    def __init__(self, left: AST, right: AST):
        super().__init__()
        print("CONSTRUCTOR BINARY")
        self.leftTree: AST = left
        self.rightTree: AST = right
        print("left", type(self.leftTree))
        print("right", type(self.rightTree))

    def evaluar(self) -> float:
        pass


class UnaryNode(AST):
    def __init__(self, sub: AST):
        super().__init__()
        self.subTree: AST = sub

    def evaluar(self) -> float:
        pass


class TernaryNode(AST):
    def __init__(self, left: AST, right: AST, center: AST):
        super().__init__()
        self.leftTree: AST = left
        self.rightTree: AST = right
        self.centerTree: AST = center

    def evaluar(self) -> float:
        pass


class FourNode(AST):
    def __init__(self, left: AST, right: AST, center1: AST, center2: AST):
        super().__init__()
        self.left: AST = left
        self.right: AST = right
        self.center1: AST = center1
        self.center2: AST = center2

    def evaluar(self) -> float:
        pass


class NumNode(AST):
    def __init__(self, num: float):
        super().__init__()
        self.val: float = num

    def evaluar(self) -> float:
        return self.val


class HighNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> bool:
        return self.leftTree.evaluar() > self.rightTree.evaluar()


class LowerNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> bool:
        return self.leftTree.evaluar() < self.rightTree.evaluar()


class HigherEqualNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> bool:
        return self.leftTree.evaluar() >= self.rightTree.evaluar()


class LowerEqualNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> bool:
        return self.leftTree.evaluar() <= self.rightTree.evaluar()


class EqualNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> bool:
        return self.leftTree.evaluar() == self.rightTree.evaluar()


class NotEqualNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> bool:
        return self.leftTree.evaluar() != self.rightTree.evaluar()


class AddNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        print("CONSTUCTOR ADDNODE")
        super().__init__(left, right)

    def evaluar(self) -> float:
        print("subtree")
        print("left", type(self.leftTree))
        print("right", type(self.rightTree))
        return self.leftTree.evaluar()+self.rightTree.evaluar()


class SubNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> float:
        print("subtree")
        print("left", type(self.leftTree))
        print("right", type(self.rightTree))
        return self.leftTree.evaluar()-self.rightTree.evaluar()


class TimesNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> float:
        return self.leftTree.evaluar()*self.rightTree.evaluar()


class DivideNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> float:
        return self.leftTree.evaluar()/self.rightTree.evaluar()


class ModuleNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> float:
        return self.leftTree.evaluar() % self.rightTree.evaluar()


class PowerNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> float:
        return self.leftTree.evaluar()**self.rightTree.evaluar()

#LOG REPAIR


class LogNode(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> float:
        return self.leftTree.evaluar()+self.rightTree.evaluar()


class SumCondition(BinaryNode):
    def __init__(self, left: AST, right: AST):
        super().__init__(left, right)

    def evaluar(self) -> float:
        if self.leftTree.evaluar():
            print("TRUE DE SUM CONDITION")
            return self.rightTree.evaluar()
        print("FALSE DE SUM CONDITION")
        return 1

        '''
        else:
            print("FALSE DE SUM CONDITION")
            return self.rightTree.evaluar()
        '''


class LoopOperation(FourNode):
    def __init__(self, left: AST, right: AST, center1: AST, center2: AST):
        super().__init__(left, right, center1, center2)

    #REPAIR THIS METHOD
    #def evaluate(self) -> float:
