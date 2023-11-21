import seaborn as sns
import matplotlib.pyplot as plt
import random
import numpy as np

class ResultAnalyzer:
    def mean(self, results):
        return sum(results) / len(results)
    
    def sample_mean(self, results, size_samples):
        sample = random.sample(results, size_samples)
        return self.mean(sample)

    def sample_means(self, results, num_samples, size_samples):
        sample_means = []
        for _ in range(num_samples):
            sample_mean = self.sample_mean(results, size_samples)
            sample_means.append(sample_mean)
        return sample_means
    
    
    def visualize_simulation_results(self, results, plot_type='histogram'):
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
            sns.kdeplot(results, fill=True, color="r")
            plt.title('KDE Plot of Simulation Results')

        # Labeling the plot
        plt.xlabel('Power Requirement (Watts)')
        plt.ylabel('Frequency')
        plt.grid(True)

        # Show the plot
        plt.show()
