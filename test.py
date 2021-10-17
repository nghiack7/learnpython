class Person:    
    pass

putin = Person()

def greeting(msg:str):
    print(msg)
     
putin.say_hello = greeting
putin.say_hello('Hello world from Python method') # in ra dòng 'Hello world from Python method'

trump = Person()
trump.say_hello('Welcome to heaven!') # lệnh này sẽ bị lỗi 'không tìm thấy hàm say_hello