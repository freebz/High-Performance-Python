import tornado.httpclient import HTTPClient
import math

httpclient = HTTPClient()
def save_prime_serial(prime):
    url = "http://127.0.0.1:8080/add?prime={}".format(prime)
    response = httpclient.fetch(url)
    finish_save_prime(response, prime)

def finish_save_prime(response, prime):
    if response.code != 200:
        print("Error saving prime: {}".format(prime))

def check_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def calculate_primes_serial(max_number):
    for number in range(max_number):
        if check_prime(number):
            save_prime_serial(number)
    return
