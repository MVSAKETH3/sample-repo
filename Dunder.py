
# Built in classes define many magic methods, dir() function can show you magic methods inherited by a class.
    # code 
# print(dir(int))


# methods that allow instances of a class to interact with the built-in functions and operators of the language. 
# The word “dunder” comes from “double underscore”, because the names of dunder methods start and end with two underscores, for example __str__ or __add__ .

print(int.__add__(12,6))
print(str.__add__('1','3'))

class Author:
    def __init__(self,name,book,pages):
        self.name=name
        self.book=book
        self.pages=pages
    def __str__(self):
        return f'{self.name} has {self.pages} pages of {self.book} book'
    def __len__(self):
        return self.pages
    def __call__(self):
        print(f'HI  i am {self.name}')
    def __del__(self):
        print(f'I am {self.name} and Autjor object has been deleted')
a=Author('saketh','python basic to advance',760)
a() #for this __call__ is used
print(a)
print(len(a))
del a
# print(a)  it will show error as d has been deleted



#pip is a package installer or package manager
#pyPI (python package index) it is like a repository we can publish or access packages from it.

#packages are nothing but collection of modules(which are having similar type of functionalities) as well as sub packages.
#packages when they are published they are called as Library.
#like numpy and pandas are packages.(libraries) 