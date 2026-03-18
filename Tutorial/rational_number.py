class Rational:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        gcd = self._gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)

    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Rational(num, den)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator


if __name__ == "__main__":
    r1 = Rational(1, 2)
    r2 = Rational(1, 3)

    print(f"r1 = {r1}")
    print(f"r2 = {r2}")
    print(f"r1 + r2 = {r1 + r2}")
    print(f"r1 - r2 = {r1 - r2}")
    print(f"r1 * r2 = {r1 * r2}")
    print(f"r1 == r2 : {r1 == r2}")
    print(f"r1 < r2  : {r1 < r2}")
    print(f"r1 > r2  : {r1 > r2}")
    print(f"GCD reduction: Rational(6, 9) = {Rational(6, 9)}")
