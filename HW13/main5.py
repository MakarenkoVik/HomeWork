def endless_fib_generator():
    number_one = 1
    number_two = 1
    print(number_one, number_two, end=" ")
    while number_one:
        number = number_one + number_two
        number_one = number_two
        number_two = number
        yield number
    return None


gen = endless_fib_generator()
while True:
	print(next(gen), end=" ")
