from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

        return wrapper
    return decorator



if __name__ == "__main__":
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y


    my_function(1, 2)


