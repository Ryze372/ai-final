class FractranEngine:
    def __init__(self):
        self.sequence = [17/91, 78/85, 19/51, 23/38, 29/33, 77/29, 95/23, 77/19, 1/17, 11/13, 13/11, 15/2, 1/7, 55/1]

    def run_sequence(self, n):
        steps = [n]
        while True:
            for f in self.sequence:
                if n * f == int(n * f):
                    n = int(n * f)
                    steps.append(n)
                    break
            else:
                break
        return steps