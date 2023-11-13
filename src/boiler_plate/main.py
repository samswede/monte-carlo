# simulation_logic.py
class BasicPiEstimation:
    def run_iteration(self):
        x, y = random.random(), random.random()
        return 1 if x**2 + y**2 <= 1 else 0

# simulation_runner.py
class MonteCarloRunner:
    def __init__(self, simulation_logic, iterations=1000):
        self.simulation_logic = simulation_logic
        self.iterations = iterations

    def run(self):
        results = [self.simulation_logic.run_iteration() for _ in range(self.iterations)]
        return results

# analysis.py
class ResultAnalyzer:
    def __init__(self, analysis_strategy):
        self.analysis_strategy = analysis_strategy

    def analyze(self, results):
        return self.analysis_strategy.analyze(results)

class MeanAnalysis:
    @staticmethod
    def analyze(results):
        return sum(results) / len(results) if results else 0

# Example Usage
if __name__ == "__main__":
    simulation = BasicPiEstimation()
    runner = MonteCarloRunner(simulation, iterations=10000)
    results = runner.run()

    analyzer = ResultAnalyzer(MeanAnalysis())
    pi_estimate = 4 * analyzer.analyze(results)
    print(f"Estimated value of π: {pi_estimate}")
