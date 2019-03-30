from math import exp, log, pow


def round_years(yr):
    """Round years to two decimal places"""
    return round(yr, 2)


class CompoundInterestException(ValueError):
    """"""


class BaseParams:

    _attrs = ('A', 'P', 'r', 't')

    def __init__(self, **kwargs):
        for attr in self._attrs:
            setattr(self, attr, None)
        for k in kwargs:
            if k in self._attrs:
                setattr(self, k, kwargs[k])
    
    def validate(self):
        num_valid = len(tuple(filter(lambda attr: getattr(self, attr), self._attrs)))
        threshold = len(self._attrs) - 1
        return num_valid >= threshold


class ContinuousCompoundInterestParams(BaseParams):
    """
    A = Accrued interest
    P = Principal
    r = Annual nominal rate of return
    t = Time in years
    """

    def __str__(self):
        return "<ContinuousCompoundInterestParams(A=%r, P=%r, r=%r, t=%r)>" % (
            self.A, self.P, self.r, self.t)


class CompoundInterestParams(BaseParams):
    """
    A = Accrued interest
    P = Principal
    r = Annual nominal rate of return
    t = Time in years
    n = Number of compounding periods in time unit t
    """

    _attrs = ('A', 'P', 'r', 't', 'n')

    def __str__(self):
        return "<CompoundInterestParams(A=%r, P=%r, r=%r, t=%r, n=%r)>" % (
            self.A, self.P, self.r, self.t, self.n)


class USD:
    """United States Dollar"""
    CENTS = 2


class BaseCI:
    def __init__(self, params: BaseParams):
        if params.validate():
            self._params = params
        else:
            raise CompoundInterestException('No more than one parameter can be null')
        self._cache = {}


class CompoundInterest(BaseCI, USD):
    """
    A = P * (1 + r/n) ^ (nt)
    P = A / (1 + r/n) ^ (nt)
    t = ln(A / P) / (n * ln(1 + r/n))
    """

    def accrued_amount(self):
        o = self._params
        if o.A is not None:
            return o.A
        cached = self._cache.get('A')
        if cached is not None:
            return cached
        A = round(o.P * pow(1 + o.r / o.n, o.n * o.t), self.CENTS)
        self._cache['A'] = A
        return A

    def principal(self):
        o = self._params
        if o.P is not None:
            return o.P
        cached = self._cache.get('P')
        if cached is not None:
            return cached
        P = round(o.A / pow(1 + o.r / o.n, o.n * o.t), self.CENTS)
        self._cache['P'] = P
        return P

    def time(self):
        o = self._params
        if o.t is not None:
            return o.t
        cached = self._cache.get('t')
        if cached is not None:
            return cached
        t = round_years(log(o.A / o.P) / (o.n * log(1 + o.r / o.n)))
        self._cache['t'] = t
        return t


class ContinuousCompoundInterest(BaseCI, USD):
    """
    A = P * e ^ (rt)
    P = A / e ^ (rt)
    t = ln(A / P) / r
    """

    def accrued_amount(self):
        o = self._params
        if o.A is not None:
            return o.A
        cached = self._cache.get('A')
        if cached is not None:
            return cached
        A = round(o.P * exp(o.r * o.t), self.CENTS)
        self._cache['A'] = A
        return A

    def principal(self):
        o = self._params
        if o.P is not None:
            return o.P
        cached = self._cache.get('P')
        if cached is not None:
            return cached
        P = round(o.A / exp(o.r * o.t), self.CENTS)
        self._cache['P'] = P
        return P

    def time(self):
        o = self._params
        if o.t is not None:
            return o.t
        cached = self._cache.get('t')
        if cached is not None:
            return cached
        t = round_years(log(o.A / o.P) / o.r)
        self._cache['t'] = t
        return t


def display(p: BaseParams, c: BaseCI) -> None:
    print(p)
    print("Accrued Amount: ${:.2f}".format(c.accrued_amount()))
    print("Principal: ${:.2f}".format(c.principal()))
    print("Profit: ${:.2f}".format(c.accrued_amount() - c.principal()))
    print("Years: {:.2f}".format(c.time()))
    print()


if __name__ == '__main__':

    # Example 1: Find accrued amount and profit
    p1 = CompoundInterestParams(P=1250000, r=0.06, t=5, n=365)
    c1 = CompoundInterest(p1) 
    display(p1, c1)

    # Example 2: Find principal and profit
    p2 = CompoundInterestParams(A=1687000, r=0.06, t=5, n=365)
    c2 = CompoundInterest(p2)
    display(p2, c2)

    # Example 3: Find accrued amount when continuously compounding
    p3 = ContinuousCompoundInterestParams(P=1250000, r=0.06, t=5)
    c3 = ContinuousCompoundInterest(p3)
    display(p3, c3)

    # Example 4: Attempt to calculate accrued amount with incomplete params
    p4 = CompoundInterestParams(P=1250000, r=0.06, t=5)  # Error! Missing `n`
    try:
        c4 = ContinuousCompoundInterest(p4)
    except CompoundInterestException as e:
        print(p4)
        print(e)

    # Example 5: Find time when given accrued amount, principal, rate
    p5 = CompoundInterestParams(A=1250000, P=1000000, r=0.1, n=365)
    c5 = CompoundInterest(p5)
    display(p5, c5)

    # Example 6: Find time when given accrued amount, principal, rate, continuous
    p6 = ContinuousCompoundInterestParams(A=1250000, P=1000000, r=0.1)
    c6 = ContinuousCompoundInterest(p6)
    display(p6, c6)
