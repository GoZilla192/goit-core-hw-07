def input_error(func):
    def inner(*args, **kwargs):
        message = ""
        try:
            message = func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            message = "Invalid input, please check the correctness arguments."

        return message
    return inner

