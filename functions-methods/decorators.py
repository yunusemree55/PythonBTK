
# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("Hello", name)


# sayHello("yunus")


import math,time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print(f"fonksiyon {str(finish - start)} saniye sürdü ")
    return inner

@calculate_time
def usAlma(a,b):
    print(math.pow(a,b))
    
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))
    

usAlma(2,3)







