import random
import math

def objective_function(x):
    # Example objective function: f(x) = x^2
    return x ** 2 

def simulated_annealing(initial_solution, initial_temp, cooling_rate, max_iterations):
    current_solution = initial_solution
    current_temp = initial_temp
    
    best_solution = current_solution
    best_value = objective_function(best_solution)
    
    # Initialize current_value to the value of the initial solution
    current_value = best_value

    for iteration in range(max_iterations):
        # Generate a new solution by perturbing the current solution
        new_solution = current_solution + random.uniform(-1, 1)  # small random step
        new_value = objective_function(new_solution)

        # Calculate the change in objective value
        delta_value = new_value - current_value
        
        # Accept the new solution with a certain probability
        if delta_value < 0 or random.random() < math.exp(-delta_value / current_temp):
            current_solution = new_solution
            current_value = new_value

            # Update best solution found so far
            if new_value < best_value:
                best_solution = new_solution
                best_value = new_value

        # Cool down the temperature
        current_temp *= cooling_rate

    return best_solution, best_value

# Example usage
initial_solution = random.uniform(-10, 10)
initial_temp = 1000
cooling_rate = 0.99
max_iterations = 1000

best_solution, best_value = simulated_annealing(initial_solution, initial_temp, cooling_rate, max_iterations)
print(f"The best x: {best_solution}, It's corresponding f(x): {best_value}")