def genPrimesTo(n):
    """ generate all primes up to and including n """
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
    """ fibonacci box method """
    trips = [[3,4,5]]
    while trips:
        X, Y, Z = trips.pop()
        if X + Y + Z < perimetermax:
            yield sorted((X, Y, Z))
            trips.append((X - 2*Y + 2*Z, 2*X - Y + 2*Z, 2*X - 2*Y + 3*Z))
            trips.append((X + 2*Y + 2*Z, 2*X + Y + 2*Z, 2*X + 2*Y + 3*Z))
            trips.append((-1*X + 2*Y + 2*Z, -2*X + Y + 2*Z, -2*X + 2*Y + 3*Z))

