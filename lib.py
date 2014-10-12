from collections import defaultdict
import numpy

def genPrimesTo(n):
    """ Generate all primes up to and including n. """
    assert int(n) == n
    n = int(n)
    yield 2
    sieve = (n+1) * [True]
    for trial in xrange(3, int(n**0.5) + 1, 2):
        if sieve[trial]:
            sieve[2*trial::trial] = (n/trial-1)*[False]
    for i in xrange(3, n+1, 2):
        if sieve[i]:
            yield i

def genPythagTrips(perimetermax):
    """ Generate all primitive pythagorean triples with perimeter at most perimetermax. """
    trips = [[3,4,5]]
    while trips:
        X, Y, Z = trips.pop()
        if X + Y + Z < perimetermax:
            yield sorted((X, Y, Z))
            trips.append((X - 2*Y + 2*Z, 2*X - Y + 2*Z, 2*X - 2*Y + 3*Z))
            trips.append((X + 2*Y + 2*Z, 2*X + Y + 2*Z, 2*X + 2*Y + 3*Z))
            trips.append((-1*X + 2*Y + 2*Z, -2*X + Y + 2*Z, -2*X + 2*Y + 3*Z))

def fitcurve(seq):
    """ Return a polynomial which fits the input sequence. """
    return numpy.polynomial.polynomial.Polynomial(
        [ int(round(coeff, 0)) for coeff in numpy.polynomial.polynomial.polyfit(
                [v[0] for v in seq], [v[1] for v in seq], len(seq) - 1) ])

def genFibs(n):
    """ Generate to nth element of fibonacci sequence. f_0 = 0 f_1 = 1, f_2 = 1 """
    if n < 0: return
    yield 0
    if n < 1: return
    yield 1
    prev2 = 0
    prev = 1
    for i in xrange(2, n+1):
        next = prev2 + prev
        yield next
        prev2 = prev
        prev = next

def factors(n, primes=None):
    """ Prime Factorization. output is {prime1:count1, prime2:count2, etc}  """
    if not primes: primes = genPrimesTo(n)
    result = defaultdict(int)
    for prime in primes:
        while n % prime == 0:
            result[prime] += 1
            n /= prime
        if n == 1:
            return result

    assert False

