def run_this():
    """This function prints the sum of the numbers from 100 to 0, counting down by 23. It returns None"""
    print("Run_This")
    idx = 0
    for i in range(100, 0, -23):
        idx += i
        print(f"i = {i}, idx = {idx}")
    print("\n")


run_this()


def run_that(num):
    """This function receives a number and returns the sum of the numbers from 0 to num, counting down by 23."""
    print("Run_That")
    idx = 0
    for i in range(num, 0, -23):
        idx += i
    return idx


print(f"run_that(10): {run_that(10)}\n")

# using keyword arguments.


def run_and_hide(defaultParam, optionalParam=10):
    print("Run_Hide")
    idx = optionalParam
    for i in range(0, defaultParam, 2):
        idx += 2+i
        print(f"i = {i}, idx = {idx}")


run_and_hide(100, 2)


def strip_my_string(my_str, start=None, end=None):
    try:
        if start == None:
            start = 0
        if end == None:
            end = len(my_str)
        if my_str is None or start is None or end is None:
            raise TypeError(
                "No value provided for(my_str:str, start:int, end:int)")
        if isinstance(my_str, str) and isinstance(start, int) and isinstance(end, int):
            if start < 0 or end <= len(my_str):
                return my_str[start:end]
        raise ValueError(
            "Wrong value provided for one of the following: my_str:str, start:int, end:int)")
    except Exception as err:
        print(f"Error: {err} at strip_my_string.")


my_sub_string = strip_my_string("Hello, World!", None, 4)
print(my_sub_string)
