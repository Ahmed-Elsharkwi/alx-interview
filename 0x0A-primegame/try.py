import random
number_list = []
def check_the_prime_number(number_list):
    """
    it will check if the number is prime or not
    """
    for i in range(0, 100):
        number_list.append(random.randint(0, 100))
check_the_prime_number(number_list)
print(number_list)
