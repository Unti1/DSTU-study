from lab1 import generator_of_nums
import test2
import time

elements = (10, 100, 10000, 100000,500000)
lst = generator_of_nums(1000)

start = time.time()

end =  time.time()

py_time = end - start
print("Python time = {}".format(py_time))

start = time.time()

end =  time.time()