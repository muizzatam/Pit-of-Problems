# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000


def sum_of_multiples_of_n_till(n, till):

    first_term = 1
    last_term = till // n

    return n * last_term * ((first_term + last_term) / 2)


def main():

    sum_of_multiples_of_3 = sum_of_multiples_of_n_till(3, 999)
    sum_of_multiples_of_5 = sum_of_multiples_of_n_till(5, 999)
    sum_of_multiples_of_15 = sum_of_multiples_of_n_till(15, 999)

    total = sum_of_multiples_of_3 + sum_of_multiples_of_5 - sum_of_multiples_of_15

    print(total)


if __name__ == "__main__":
    main()
