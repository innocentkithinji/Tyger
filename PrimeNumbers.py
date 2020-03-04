import random
PRIMES = []



def prime_test(candidate):
    for divisor in range(2, int(candidate ** 0.5) + 2):
        if candidate % divisor != 0:
            PRIMES.append(candidate)
            return True
        else:
            return False

def get_prime_3d_array():
    primes = [[[1] * 10] * 10] * 10
    # Count my primes
    candidate = 1
    while len(PRIMES) != 1000:
        if candidate % 2 != 0 and candidate != 1:
            prime_test(candidate)
        if candidate == 2:
            PRIMES.append(2)
        candidate += 1

    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                random_choice = random.choice(PRIMES)
                primes[i][j][k]= random_choice
                PRIMES.remove(random_choice)

    return primes


if __name__ == '__main__':
    print(get_prime_3d_array())