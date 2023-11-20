from mc_simulation.boiler_plate.base_sim_logic import MonteCarloSimulationLogic 
from mc_simulation.boiler_plate.base_sim_runner import MonteCarloRunner
import random

class CarPowerRequirement(MonteCarloSimulationLogic):
    def run_iteration(self):
        
        speed_kmph = 100

        params = self.generate_random_params()

        # Example usage
        base_power = self.calculate_power_requirements(speed_kmph= speed_kmph, 
                                                       car_weight= params['car_weight'],
                                                       frontal_area= params['frontal_area'], 
                                                       drag_coefficient= params['drag_coefficient'], 
                                                       rolling_resistance_coefficient= params['rolling_resistance_coefficient'])
        
        total_power = self.adjust_for_mechanical_losses(base_power,
                                                        mechanical_loss_factor=params['mechanical_loss_factor'])

        return total_power
    
    def generate_random_params(self):
        # Random car weight (normally distributed around 1500 kg, with a standard deviation of 200 kg)
        car_weight = random.gauss(mu=1500, sigma=200)

        # Random frontal area (normally distributed around 2.2 m², with a standard deviation of 0.2 m²)
        frontal_area = random.gauss(mu=2.2, sigma=0.2)

        # Random drag coefficient (uniformly distributed between 0.25 and 0.35)
        drag_coefficient = random.uniform(0.25, 0.35)

        # Random rolling resistance coefficient (uniformly distributed between 0.01 and 0.015)
        rolling_resistance_coefficient = random.uniform(0.01, 0.015)

        # Random mechanical loss factor (uniformly distributed between 0.15 and 0.25)
        mechanical_loss_factor = random.uniform(0.15, 0.25)

        return {'car_weight': car_weight, 
                'frontal_area': frontal_area, 
                'drag_coefficient': drag_coefficient, 
                'rolling_resistance_coefficient': rolling_resistance_coefficient,
                'mechanical_loss_factor': mechanical_loss_factor}

    def calculate_power_requirements(self, speed_kmph, car_weight, frontal_area, drag_coefficient, rolling_resistance_coefficient):
        """
        Calculate the power required to drive a car at a given speed.

        :param speed_kmph: Speed of the car in kilometers per hour.
        :param car_weight: Weight of the car in kilograms.
        :param frontal_area: Frontal area of the car in square meters.
        :param drag_coefficient: Drag coefficient of the car (dimensionless).
        :param rolling_resistance_coefficient: Rolling resistance coefficient (dimensionless).
        :return: Power in watts required to overcome aerodynamic drag and rolling resistance.
        """
        air_density = 1.225  # kg/m^3
        g = 9.81 # m/s^2

        # Convert speed from km/hr to m/s
        speed_mps = speed_kmph * 1000 / 3600

        # Calculate power to overcome aerodynamic drag
        power_drag = 0.5 * air_density * frontal_area * drag_coefficient * speed_mps**3

        # Calculate power to overcome rolling resistance
        rolling_resistance_force = rolling_resistance_coefficient * car_weight * g
        power_rolling_resistance = rolling_resistance_force * speed_mps

        # Total power required
        total_power = power_drag + power_rolling_resistance

        return total_power

    def adjust_for_mechanical_losses(self, base_power, mechanical_loss_factor):
        """
        Adjust the calculated power for mechanical losses.

        :param base_power: Base power calculated for overcoming drag and rolling resistance (in watts).
        :param mechanical_loss_factor: Factor representing mechanical losses (percentage as decimal).
        :return: Adjusted power including mechanical losses.
        """
        adjusted_power = base_power / (1 - mechanical_loss_factor)
        return adjusted_power


def mean(results):
    return sum(results) / len(results)

import seaborn as sns
import matplotlib.pyplot as plt

def visualize_simulation_results(results, plot_type='histogram'):
    """
    Visualize the distribution of the Monte Carlo simulation results.

    :param results: List of results from the Monte Carlo simulation.
    :param plot_type: Type of plot to generate ('histogram' or 'kde').
    """
    sns.set(style="whitegrid")  # Set the visual style of the plots

    # Create a figure and axis
    plt.figure(figsize=(10, 6))

    # Choose the type of plot
    if plot_type == 'histogram':
        sns.histplot(results, kde=False, color="blue", bins=30)
        plt.title('Histogram of Simulation Results')
    elif plot_type == 'kde':
        sns.kdeplot(results, shade=True, color="r")
        plt.title('KDE Plot of Simulation Results')

    # Labeling the plot
    plt.xlabel('Power Requirement (Watts)')
    plt.ylabel('Frequency')
    plt.grid(True)

    # Show the plot
    plt.show()


# Example Usage
if __name__ == "__main__":
    simulation = CarPowerRequirement()
    runner = MonteCarloRunner(simulation, iterations=10000)
    results = runner.run()

    mean_power = mean(results)
    print(f"Mean Power Requirement: {mean_power}")

    # Assuming 'results' contains the output from your Monte Carlo simulation
    visualize_simulation_results(results, plot_type='kde')





