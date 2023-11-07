class grandfather:
    def fun_grand(self):
        print("Grand Father Property")
class father(grandfather):
    def fun_fat(self):
        print("Father Property")
class child(father):
    def fun_ch(self):
        print("Child Property")
#OBJECT OF CHILD CLASS
c1=child()
c1.fun_grand()
c1.fun_fat()
c1.fun_ch()
