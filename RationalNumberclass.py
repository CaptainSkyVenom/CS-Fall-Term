class RationalNumber:
    def __init__(self,nume,deno):

        if str(nume) == nume or str(deno) == nume:
            print("INTEGERS AS ARGUMENTS PLEASE")
            return

        if deno == 0:
            print("CANNOT HAVE 0 AS DENOMINATOR")
            return

        self.nume = nume;
        self.deno = deno;

    def simplify(self):
        x = self.nume
        y = self.deno
        while y != 0:
            (x, y) = (y, x % y)

        self.nume /= x
        self.deno /= x

        return self

    def __str__(self):
        return str(self.nume) + "/" + str(self.deno)

    def __add__(self, rational2):
        return RationalNumber(self.nume * rational2.deno + rational2.nume * self.deno, self.deno * rational2.deno)

    def __sub__(self, rational2):
        return RationalNumber(self.nume * rational2.deno - rational2.nume * self.deno, self.deno * rational2.deno)


    def __mul__(self, rational2):
        return RationalNumber(self.nume * rational2.nume, self.deno * rational2.deno)

    def __truediv__(self, rational2):
        return RationalNumber(self.nume * rational2.deno, self.deno * rational2.nume)

    def todec(self):
        return self.nume/self.deno

    def __pow__(self, num):
        return RationalNumber(self.nume ** num, self.deno ** num)

    def reciprocal(self):
        return RationalNumber(self.deno, self.nume)

    def __eq__(self, rational2):
        return self.nume == rational2.nume and self.deno == rational2.deno

    def __ne__(self, rational2):
        return self.nume != rational2.nume or self.deno != rational2.deno

    def __lt__(self, rational2):
        return self.nume * rational2.deno < rational2.nume * self.deno

    def __le__(self, rational2):
        return self.nume * rational2.deno <= rational2.nume * self.deno

    def __gt__(self, rational2):
        return self.nume * rational2.deno > rational2.nume * self.deno

    def __ge__(self, rational2):
        return self.nume * rational2.deno >= rational2.nume * self.deno



def main():
    a = RationalNumber(1,2)
    b = RationalNumber(1,3)
    print(a)
    print(b)
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a.todec())
    print(a**3)
    print(a.reciprocal())
    print(a == b)
    print(a != b)
    print(a < b)
    print(a >= b)
    c = RationalNumber(10,80)
    print(c.simplify())
    c = RationalNumber(1,0)
    c = RationalNumber("Dog", "Cat")


main()
