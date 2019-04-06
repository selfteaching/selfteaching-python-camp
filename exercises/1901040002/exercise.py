def __init__(self, name):
    # Assign the argument to the instance's name attribute
    self.name = name

    # Initialize property
    self._age = 0

# An instance method. All methods take "self" as the first argument
def say(self, msg):
    print("{name}: {message}".format(name=self.name, message=msg))