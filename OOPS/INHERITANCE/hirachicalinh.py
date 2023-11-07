class parent:
    def fun_par(self):
        print("Parent Function:")
class c1(parent):
    print("!st Child")
class c2(parent):
    print("2nd Child")
c11=c1()
c11.fun_par()
c22=c2()
c22.fun_par()