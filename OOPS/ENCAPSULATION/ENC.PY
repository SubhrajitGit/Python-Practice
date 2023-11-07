#ENCAPSULATION CAN DETERMINE BY SINGLE UNDERSCOPE(_)OR DOUBLE UNDERSCOPE(__)
#ACHIVE ENCAPSULATION BY PRIVATE
class A:
    def _init_(self,a):
        self._a # type: ignore
    def show(self):
        print("Privaate Variable OF A")
class B(A):
    def __init__(self,a):
        self.__a # type: ignore
    def showB(self):
        print("Privaate Variable OF B")