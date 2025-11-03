"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [20.0, 16.0, 27.0, 32.0, 30.3]
city_population = {"Riga" : 591882, "Tokyo": 14250000,
                  "Amsterdam": 1160000, "New York" : 8478000,
                  "London" : 9100000}

# TODO: Compute aggregates
average_temperature = sum(temperatures) / len(temperatures)
largest_city = ""
largest_population = 0
total_population = 0

for city, population in city_population.items():
    total_population += population
    if population > largest_population:
        largest_population = population
        largest_city = city

# TODO: Print results
print("Average temperature:", average_temperature)
print("Largest city:", largest_city, "-", largest_population)
print("Total population:", total_population)
