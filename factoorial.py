# def factorial(num):
#     fact=1
#     for i in range(num,1,-1):
#         fact=fact*i
#     return fact
# num=int(input("Entere Number To Find Out Factorial:"))
# print("factorial is:",factorial(num))



#RECURSIVE


def factorial(num):
    if(num==1):
        return 1
    else:
        return(num*factorial(num-1))
num=int(input("Entere Number To Find Out Factorial:"))
print("factorial is:",factorial(num))