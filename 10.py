## It's so hard that I reduce exe-time, so I refer to internet.

def prime_sieve(bound):
    """
    Return a list of prime numbers from 2 to n.
    Very fast, (n < 10,000,000) in 0.4 sec.
    ----
    Algorithm & Python source: Robert William Hanks
    http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
    """
    sieve = [True] * (bound/2)
    for i in xrange(3, int(bound**.5)+1, 2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((bound-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1, bound/2) if sieve[i]]

print sum(prime_sieve(2000000))
