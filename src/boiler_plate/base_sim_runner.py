
class SimulationRunner:
    """
    Class for running a Monte Carlo simulation.

    This class takes an instance of a SimulationLogic subclass and uses it
    to run a specified number of simulation iterations.
    """

    def __init__(self, simulation_logic, iterations=1000):
        """
        Initializes the SimulationRunner.

        Args:
            simulation_logic (SimulationLogic): An instance of a subclass of SimulationLogic.
            iterations (int): The number of iterations to run the simulation for.
        """
        self.simulation_logic = simulation_logic
        self.iterations = iterations

    def run(self):
        """
        Runs the Monte Carlo simulation for the specified number of iterations.

        Returns:
            A list of results from each simulation iteration.
        """
        return [self.simulation_logic.run_iteration() for _ in range(self.iterations)]
