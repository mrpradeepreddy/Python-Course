# def get_squares_gen():
#     for i in range(5):
#         yield i * i

# gen = get_squares_gen()

# print(next(gen))  # ➜ 0
# print(next(gen))  # ➜ 1

def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()

for value in g:
    print(value)
