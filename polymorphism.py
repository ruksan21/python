class A:
    def display_name():
        print("class A")
        
class b(A):
    def deisplay_name():
        print("class b")
class c(b):
    def display_name():
        print("class c")
def sum(a,b=0,c=0,d=0):
    add = a + b + c + d
    return add


