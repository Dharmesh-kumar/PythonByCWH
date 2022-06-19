# DIAMOND SHAPE PROBLEM:- if there are many classes so which perform which tasks or overriding of them amd all so there are problem facing between the
# java:- doesn't suppoert multiple inheritance so there are issue regarding it thats why a problem between them which resolve like this
#here are many confusions like which class inherit by classS because if it is in D so it take D method and if not it take B then print it or dont have in both print A so there are whole overriding concepts contradict here thats why w cannot use multiple inheritance
class A:
    def met(self):
        print("This is a method from class A")
class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(C, B):
    def met(self):
        print("This is a method from class D")

a=A()
b=B()
c=C()
d=D()

d.met()
