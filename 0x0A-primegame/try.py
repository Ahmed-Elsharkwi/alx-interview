def check_the_prime_number(number):
    """
    it will check if the number is prime or not
    """
    if number == 1:
        return 0;
    counter = 2
    number_factors = 0

    while (counter <= int(number / 2)):
        if number_factors > 1:
            return 0
        if number % counter == 0:
            number_factors += 1
        counter += 1
    return 1
print(check_the_prime_number(3))
