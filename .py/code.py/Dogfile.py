def new_func():
    class Dog(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def speak(self):
            print("hi i am", self.name, 'and i am', self.age, 'years old')
 

 
    tim = Dog('tim', 20)
    fred = Dog('fred', 21)
    tim.speak()              
    fred.speak()

new_func()              

