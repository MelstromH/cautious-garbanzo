
fb = 0
for i in range(100):
    if i % 3 == 0:
        fb += 1

    if i % 5 == 0:
        fb += 2

    if fb == 1:
        print("Fizz")

    if fb == 2:
        print("Buzz")

    if fb == 3:
        print("Fizz Buzz")

    if fb == 0:
        print(i)

    fb = 0
