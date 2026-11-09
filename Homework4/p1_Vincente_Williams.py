class RndSeq():
    """Random number generator class with iterator interface"""
    def __init__(self, x0, n):
        self.m = 2**32
        self.a = 22695477
        self.c = 1
        self.n = n
        self.current_x = x0
        self.original_n = n
        self.original_x = x0

    def __iter__(self):
        self.n = self.original_n
        self.current_x = self.original_x
        return self
    
    def __next__(self):
        if self.n < 0:
            self.current_x = (self.a*self.current_x + self.c)%self.m
            return self.current_x
        elif self.n == 0:
            raise StopIteration 
        else:
            self.current_x = (self.a*self.current_x + self.c)%self.m
            self.n = self.n - 1
            return self.current_x

def rnd_gen(x0,n):
    """RNG function with n as number of values to generate 
    and x0 as the seed"""
    current_x = x0
    a = 22695477
    c = 1
    m = 2**32
    while n != 0:
        current_x = (a*current_x + c)%m 
        if n > 0:
            n = n - 1
        yield current_x

def main():
    rnd = RndSeq(1, 10)
    print([i for i in rnd])
    rnd = RndSeq(1, 0)
    print([i for i in rnd])
    rnd = RndSeq(1, -1)
    print(next(rnd))
    print(next(rnd))
    print(next(rnd))

    rnd = rnd_gen(1, 10)
    for i in rnd:
        print(i)
    rnd = rnd_gen(1, 0)
    for i in rnd:
        print(i)
    rnd = rnd_gen(1, -1)
    print(next(rnd))
    print(next(rnd))
    print(next(rnd))


if __name__ == "__main__":
    main()