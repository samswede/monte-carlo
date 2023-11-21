from mc_simulation.boiler_plate.base_sim_logic import MonteCarloSimulationLogic 
from mc_simulation.boiler_plate.base_sim_runner import MonteCarloRunner
from mc_simulation.boiler_plate.base_result_analyzer import ResultAnalyzer
import random
import numpy as np


# simulation_logic.py
class ProbDealerBust(MonteCarloSimulationLogic):

    def __init__(self, startingHand, target=21):
        self.startingHand = startingHand
        self.target = target

    def run_iteration(self):
        dealer_cards = [self.startingHand]
        while sum(dealer_cards) < self.target-4:
            dealer_cards.append(random.randint(1, 10))
        return 1 if sum(dealer_cards) > 21 else 0


# Example Usage
if __name__ == "__main__":
    startingHand = 15
    target = 80
    print(f"Starting Hand: {startingHand}")
    simulation = ProbDealerBust(startingHand)
    runner = MonteCarloRunner(simulation, iterations=10000)
    results = runner.run()

    analyzer = ResultAnalyzer()

    pure_mean = analyzer.mean(results)
    sample_means = analyzer.sample_means(results, num_samples=1000, size_samples=1000)
    
    print(f'Pure Mean: {pure_mean}')

    analyzer.visualize_simulation_results(sample_means, plot_type='kde')