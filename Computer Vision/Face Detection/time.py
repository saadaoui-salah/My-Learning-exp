import timeit
import pyximport; pyximport.install()
import example_1
print(example_1.ex(100))
fast = timeit.timeit('example_1.ex(100)', setup='import example_1',number=100)
low  = timeit.timeit('example_2.ex(100)', setup='import example_2',number=100)

print('example 1 is {}x faster than example 2'.format(low/fast))