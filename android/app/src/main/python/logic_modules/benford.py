import numpy as np

class BenfordChecker:
    def check_distribution(self):
        data = [np.random.randint(1, 10000) for _ in range(1000)]
        first_digits = [int(str(x)[0]) for x in data if x > 0]
        distribution = {d: first_digits.count(d) / len(first_digits) for d in range(1, 10)}
        benford = {d: np.log10(1 + 1/d) for d in range(1, 10)}
        return {
            "Observed": distribution,
            "Expected (Benford)": benford
        }