import csv
import random

class Country():
    def __init__(self, name, population, life_expectancy, poverty_rate,
                 yearly_median_income=None, daily_median_income=None):
        if yearly_median_income == None:
            if daily_median_income == None:
                raise Exception("Need median income input")
            else:
                self.median_income = 365 * float(daily_median_income)
        else:
            self.median_income = float(yearly_median_income)
        self.life_expectancy = float(life_expectancy)
        self.poverty_rate = float(poverty_rate)
        self.name = name
        self.population = int(population)

    def print_values(self):
        in_poverty = self.check_if_in_poverty()
        if in_poverty:
            print(
                f"You were born in {self.name} which has an extreme poverty rate of {self.poverty_rate}%. "
                f"\nYou suffer from a severe deprivation of basic human needs, including food, safe drinking water, "
                f"sanitation facilities, health, shelter, education and information")
        else:
            print(f"You were born in {self.name} which has a population of {self.population}."
                  f" You avoided the extreme poverty rate of {self.poverty_rate}%."
                  f"\nYou have a life expectancy of {self.life_expectancy} years"
                  f" and your annual salary is {self.median_income} USD")

    def check_if_in_poverty(self):
        rand_val = random.uniform(0, 100)
        if rand_val <= self.poverty_rate:
            return True
        else:
            return False

class ParseCsv():
    def _get_csv_dictionary(self, csv_file, dict):
        with open(csv_file, encoding="cp1252") as csv_object:
            reader = csv.reader(csv_object, delimiter=',')
            i = 0
            for row in reader:
                if i > 0:
                    dict[row[0].lower()] = float(row[1].strip('%').strip("$").replace(",", ""))
                i += 1

    def parse_csv_files(self):
        population = {}
        life_expectancy = {}
        median_income = {}
        median_income_per_day = {}
        poverty_rate = {}
        self._get_csv_dictionary('D:\Documents\CODE\python_code\where_in_the_world\data\country_by_population.csv',
                                 population)
        self._get_csv_dictionary('D:\Documents\CODE\python_code\where_in_the_world\data\country_life_expectancy.csv',
                                 life_expectancy)
        self._get_csv_dictionary('D:\Documents\CODE\python_code\where_in_the_world\data\country_median_income_MORE_ACCURATE.csv',
                                 median_income)
        self._get_csv_dictionary('D:\Documents\CODE\python_code\where_in_the_world\data\country_median_income_per_day_LESS_ACCURATE.csv',
                                 median_income_per_day)
        self._get_csv_dictionary('D:\Documents\CODE\python_code\where_in_the_world\data\country_poverty_rate.csv',
                                 poverty_rate)
        countries = {}
        for key in population.keys():
            if key in life_expectancy:
                if key in poverty_rate:
                    tmp_poverty_rate = poverty_rate[key]
                else:
                    tmp_poverty_rate = 0
                if key in median_income:
                    countries[key] = Country(key, population[key], life_expectancy[key], tmp_poverty_rate,
                                      yearly_median_income=median_income[key])
                elif key in median_income_per_day:
                    countries[key] = Country(key, population[key], life_expectancy[key], tmp_poverty_rate,
                                             daily_median_income=median_income_per_day[key])
        return countries

if __name__ == "__main__":
    with open('D:\Documents\CODE\python_code\where_in_the_world\data\country_by_population.csv') as f:
        print(f)
    parser = ParseCsv()
    countries = parser.parse_csv_files()
    vals = list(countries.values())
    vals.sort(key = lambda x:-x.population)
    for i, val in enumerate(vals):
        print(i)
        val.print_values()