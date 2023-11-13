from mc_simulation.boiler_plate.base_sim_logic import MonteCarloSimulationLogic 
from mc_simulation.boiler_plate.base_sim_runner import MonteCarloRunner
import random

# simulation_logic.py
class BasicPiEstimation(MonteCarloSimulationLogic):
    def run_iteration(self):
        x, y = random.random(), random.random()
        return 1 if x**2 + y**2 <= 1 else 0

def mean(results):
    return sum(results) / len(results)

# Example Usage
if __name__ == "__main__":
    simulation = BasicPiEstimation()
    runner = MonteCarloRunner(simulation, iterations=10000)
    results = runner.run()

    pi_estimate = 4 * mean(results)
    print(f"Estimated value of π: {pi_estimate}")
