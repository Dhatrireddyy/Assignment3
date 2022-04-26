# ICSE 2019 Grade 12
# Question 10

# Name: Velma Dhatri Reddy
# Roll number: AI21BTECH11030

""" Problem Statement
A die is thrown once. Find the probability of getting
(i) a prime number
(ii) a number lying between 2 and 6
(iii) an odd number
"""

def main():
    total = 6  # total number of numbers on dice
    primes = 3  # total number of prime numbers on dice
    nos = 3 # number lying between 2 and 6
    odds = 3  # total number of odds on dice

    #Output
    print(f"The probability of getting a prime number is {prob1(total,primes)}")
    print(f"The probability of getting a number lying between 2 and 6 is {prob2(total,nos)}")
    print(f"The probability of getting a odd number is {prob3(total,odds)}")
     
def prob1(total,primes) -> float:
        """ Returns the probability of getting a prime number """
        return primes/total

def prob2(total,nos) -> float:
        """ Returns the probability of getting a number lying between 2 and 6 """
        return nos/total

def prob3(total,odds) -> float:
        """ Returns the probability of getting a number odd number """
        return odds/total

if __name__ == '__main__':
       main()