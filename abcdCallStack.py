# The call stack is how Python remembers where to return the execution after each function call. the call stack isn't stored in a variable in your program; rather, Python handles it behind the scenes. when your program calls a function, Python creates a frame object on the top of the call stack. Frame objects store the line number of the original function call so that Python can remember where to return. If another function call is made, Python puts another frame object on the call stack above the other one. 

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()