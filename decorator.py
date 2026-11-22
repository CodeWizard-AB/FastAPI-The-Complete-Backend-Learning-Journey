# * Function decorator
def log_function(fn):
    def wrapper(*args):
        print("function has started")
        fn(args)
        print("function has finished")

    return wrapper


# * Method decorator
def method_decorator(fn):
    def wrapper(self, *args):
        print('Before method execution')
        return fn(self, *args)

    return wrapper


# * Class decorator
def myclass(cls):
    cls.name = cls.__name__
    return cls


@log_function
def create_product(data):
    print("Product is created:", data)


create_product({"name": "Laptop", "price": 100})


@myclass
class MyClass:
    @method_decorator
    def say_hello(self, message: str) -> str:
        return f"hello, {message}"


obj = MyClass()
print(obj.say_hello("John"))
print(MyClass.name)
