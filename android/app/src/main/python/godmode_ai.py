from logic_modules.fractran import FractranEngine
from logic_modules.collatz import CollatzAnalyzer
from logic_modules.alpha_tensor import AlphaTensor
from logic_modules.benford import BenfordChecker

class GodModeAI:
    def __init__(self):
        self.fractran = FractranEngine()
        self.collatz = CollatzAnalyzer()
        self.tensor = AlphaTensor()
        self.benford = BenfordChecker()

    def execute(self, command):
        command = command.lower()
        if "fractran" in command:
            return self.fractran.run_sequence(int(command.split()[-1]))
        elif "collatz" in command:
            return self.collatz.analyze(int(command.split()[-1]))
        elif "tensor" in command:
            return self.tensor.multiply()
        elif "benford" in command:
            return self.benford.check_distribution()
        else:
            return "Unbekannter Befehl."