# A number is a perfect square, or a square number, if it is the square of a positive integer. For example, 25 is a square number because 5^2 = 5 * 5 = 25; it is also an odd square. The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 1 + 9 + 25 = 35. Among the first 279 thousand square numbers, what is the sum of all the odd squares?


def list_of_odd_squares(till):

    return [i**2 for i in range(1, till + 1, 2)]


def sum_of(numbers):

    sum = 0
    for i in numbers:
        sum += i

    return sum


def main():

    odd_squares = list_of_odd_squares(279_000)
    print(sum(odd_squares))


if __name__ == "__main__":
    main()
