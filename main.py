# Import required libraries
import statistics  # Built-in statistics module for verification
import math       # For mathematical operations like square root
from typing import List, Union  # For type hinting
import random    # For generating random test data

# Define a class to handle statistical calculations
class StatisticsCalculator:
    # Initialize the class with data
    def __init__(self, data: List[Union[int, float]]):
        # Store the input data as an instance variable
        self.data = data

    # Method to calculate arithmetic mean
    def mean(self) -> float:
        """Calculate the arithmetic mean of the data."""
        # Sum all numbers and divide by count of numbers
        return sum(self.data) / len(self.data)

    # Method to calculate median
    def median(self) -> float:
        """Calculate the median of the data."""
        # Sort the data in ascending order
        sorted_data = sorted(self.data)
        # Get the length of the data
        n = len(sorted_data)
        # Find the middle position
        mid = n // 2
        
        # If length is even, average the two middle numbers
        if n % 2 == 0:
            return (sorted_data[mid-1] + sorted_data[mid]) / 2
        # If length is odd, return the middle number
        return sorted_data[mid]

    # Method to calculate mode
    def mode(self) -> Union[float, str]:
        """Calculate the mode of the data."""
        # Check if data exists
        if not self.data:
            return "No data provided"
        
        # Create a dictionary to store frequency of each number
        frequency = {}
        # Count occurrence of each number
        for num in self.data:
            frequency[num] = frequency.get(num, 0) + 1
        
        # Find the highest frequency
        max_freq = max(frequency.values())
        # Get all numbers that appear with the highest frequency
        modes = [k for k, v in frequency.items() if v == max_freq]
        
        # If all values appear once, there is no mode
        if len(modes) == len(self.data):
            return "No mode found (all values appear once)"
        # If multiple values have the same highest frequency
        elif len(modes) > 1:
            return f"Multiple modes found: {modes}"
        # Return the single mode
        return modes[0]

    # Method to calculate standard deviation
    def standard_deviation(self) -> float:
        """Calculate the standard deviation of the data."""
        # First calculate the mean
        mean = self.mean()
        # Sum the squared differences from the mean
        squared_diff_sum = sum((x - mean) ** 2 for x in self.data)
        # Take the square root of the average squared difference
        return math.sqrt(squared_diff_sum / len(self.data))

    # Method to calculate variance
    def variance(self) -> float:
        """Calculate the variance of the data."""
        # Variance is the square of standard deviation
        return self.standard_deviation() ** 2

    # Method to calculate range
    def range(self) -> float:
        """Calculate the range of the data."""
        # Range is the difference between largest and smallest values
        return max(self.data) - min(self.data)

# Main function to demonstrate the calculator
def main():
    # Generate 20 random numbers between 0 and 100 for testing
    data = [random.uniform(0, 100) for _ in range(20)]
    # Print the generated data rounded to 2 decimal places
    print("Generated data:", [round(x, 2) for x in data])
    
    # Create an instance of our calculator with the test data
    calc = StatisticsCalculator(data)
    
    # Print all statistical measures with proper formatting
    print("\nStatistical Analysis:")
    print(f"Mean: {calc.mean():.2f}")          # Print calculated mean
    print(f"Median: {calc.median():.2f}")      # Print calculated median
    print(f"Mode: {calc.mode()}")              # Print calculated mode
    print(f"Standard Deviation: {calc.standard_deviation():.2f}")  # Print calculated standard deviation
    print(f"Variance: {calc.variance():.2f}")  # Print calculated variance
    print(f"Range: {calc.range():.2f}")        # Print calculated range

# Check if this file is being run directly (not imported)
if __name__ == "__main__":
    # If so, run the main function
    main()
