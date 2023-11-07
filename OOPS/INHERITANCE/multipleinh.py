class father:
    def fun_fath(self):
        print("Father Property")
class mother:
    def fun_moth(self):
        print("Mother Property")
class child(father,mother):
    def fun_ch(self):
        print("Child Property")
        #OBJECT OF CHILD
c1=child()
c1.fun_fath()
c1.fun_moth()
c1.fun_ch()