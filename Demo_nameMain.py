print('HI i am printed everytime you imported')
def display(name):
    return name
def do_something():
    print('this function is doing something')

# print(__name__)
if __name__=="__main__":
    n=input('enter name')
    print(display(n))
    do_something()
    print('i will not be printed when imported')

