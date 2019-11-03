def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
       # equivalent to all_the_args(a=3, b=4)
print(all_the_args(*args, **kwargs))