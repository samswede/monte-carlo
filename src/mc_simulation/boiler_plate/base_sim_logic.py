

class MonteCarloSimulationLogic:
    """
    Base class for defining the simulation logic of a Monte Carlo simulation.
    
    Subclasses should override the run_iteration method to implement
    specific simulation logic for each iteration.
    """

    def run_iteration(self):
        """
        Runs a single iteration of the simulation.

        This method should be overridden by subclasses to define the specific
        behavior for one iteration of the simulation.

        Returns:
            The result of one simulation iteration. The type of result can
            vary depending on the simulation (e.g., a number, a boolean,
            a complex data structure, etc.).
        """
        raise NotImplementedError("Each SimulationLogic subclass must implement the run_iteration method.")

