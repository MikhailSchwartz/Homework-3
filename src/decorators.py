from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                return result
            except Exception as exc_info:
                message = f"{func.__name__} error: {type(exc_info).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                raise
        return wrapper

    return decorator

#
# if __name__ == "__main__":
# #     @log(filename="mylog.txt")
# #     def my_function(x, y):
# #         return x - y
# #
# #     my_function(10, 0)
#
#
#     @log()
#     def function(x, y):
#         """Деление X на Y"""
#         return x / y
#
#
#     function(10, 0)

