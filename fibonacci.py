#!/usr/bin/python
# simple test program for SwiftNavigation

divby3 = 'Buzz'
divby5 = 'Fizz'
divby15 = 'FizzBuzz'
prime =   'BuzzFizz'
nth = 10000000000                   # nth fibonacci number


# isprime routine found on StackExchange
def isprime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

# generate fibonacci number, and output required strings

f0, fibonacci = (1, 1)
while fibonacci < nth:
    if  fibonacci % 15 == 0:
        print divby15
    elif  fibonacci % 5 == 0:
        print divby5
    elif  fibonacci % 3 == 0:
        print divby3
    elif isprime(fibonacci):
        print prime
    else:
        print '{0}'.format(fibonacci)
    
    f0, fibonacci = (fibonacci, f0 + fibonacci)


