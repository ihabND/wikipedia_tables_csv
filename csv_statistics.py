import csv

def normalize_num(num):
    digits = num.split(",")
    digits = "".join(digits)
    return int(digits)

def pprint_num(num):
    number_str = str(num)[::-1]
    new_num = ""
    inner = 0
    for i in range(len(number_str)):
        inner += 1
        new_num += number_str[i]
        if inner == 3:
            inner = 0
            new_num += "."
    if new_num.endswith("."):
        new_num = new_num[:-1]
    return new_num[::-1]

with open("data/country_populations.csv", newline="") as data_file:
    reader = csv.reader(data_file)
    header = next(reader)

    min_population = 1_000_000
    max_population = 1_500_000_000
    country_num = 0
    population_total = 0
    for row in reader:
        population = normalize_num(row[1])
        if population > min_population and population < max_population:
            country_num += 1
            population_total += population

print(f"""Total population of countries with more than {pprint_num(min_population)},
and less then {pprint_num(max_population)} people: {pprint_num(population_total)}.
Average population per country: {pprint_num(population_total // country_num)}.""")
