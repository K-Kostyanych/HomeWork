import os

class Example:
  def __new__(cls, *args, **kwargs):
   print(args)
   print(kwargs)
   return object.__new__(cls)

  def __init__(self, first, second, third):
    print(first)
    print(second)
    print(third)

ex = Example('data', second=25, third=3.14)
print(os.getcwd())
print(os.listdir())
for i in os.walk('..'):
    print(i)
file = [i for i in os.listdir() if os.path.isfile(i)]
dirs = [f for f in os.listdir() if os.path.isdir(f)]
print(file)
print(dirs)
print(os.stat(file[2]))