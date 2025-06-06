import numpy as np

class AlphaTensor:
    def multiply(self):
        A = np.random.randint(1, 10, (3, 3))
        B = np.random.randint(1, 10, (3, 3))
        result = A @ B
        return {
            "Matrix A": A.tolist(),
            "Matrix B": B.tolist(),
            "Result": result.tolist()
        }