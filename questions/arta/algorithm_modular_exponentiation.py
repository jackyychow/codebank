# Question: Compute a modular exponent efficiently.
#
# Repeated squaring reduces the number of multiplications from O(b) to O(log b).


class Exponential:
    def findExponential(self, a, b):
        MOD = 10**9 + 7
        if b == 0:
            return 1
        if b == 1:
            return a % MOD
        half = self.findExponential(a, b // 2)
        if b % 2 == 0:
            return half * half % MOD
        return a * half * half % MOD


if __name__ == "__main__":
    exp = Exponential()
    assert exp.findExponential(2, 5) == 32
    assert exp.findExponential(2, 0) == 1
