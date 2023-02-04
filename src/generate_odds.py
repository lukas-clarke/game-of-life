import random
from data_parsing_helper import ParseCsv

class generateOdds():
    def __init__(self):
        parser = ParseCsv()
        self.countries = parser.parse_csv_files()
        self.total_pop, self.weighted_list = self.get_weighted_list()

    def get_weighted_list(self):
        sum_total = 0
        weighted_list = []
        for country in self.countries.values():
            sum_total += country.population
            weighted_list.append((sum_total, country))
        return sum_total, weighted_list

    def get_random_persons_country(self):
        rand_num = random.randint(0, self.total_pop)
        """We use the optimal search here. 
        However for the size of this data and for beginner coders, the naive approach is functional."""
        return self.binary_search_weighs(rand_num, self.weighted_list)

    def binary_search_weighs(self, target, weighted_list):
        lo = 0
        hi = len(weighted_list)
        while lo < hi:
            mid = (hi + lo) // 2
            sum_total, country = weighted_list[mid]
            if target <= sum_total:
                if mid == 0:
                    return country
                elif target > weighted_list[mid - 1][0]:
                    return country
                else:
                    hi = mid
            else:
                lo = mid + 1
        raise Exception(f"Binary search failed for target {target}")

    def naive_search(self, target, weighted_list):
        for sum_total, country in weighted_list:
            if target < sum_total:
                return country
        raise Exception(f"Naive search failed for target {target}")

if __name__ == "__main__":
    odds = generateOdds()
    for i in range(10000):
        odds.get_random_persons_country().print_values()