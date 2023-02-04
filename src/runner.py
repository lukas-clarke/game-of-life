from generate_odds import generateOdds

if __name__ == "__main__":
    odds = generateOdds()
    input("Welcome to the game of Life!\n"
          "You will be born somewhere on earth and be given the stats of your life."
          "\nWhere you are born is generated by the weighted population size of each country."
          "\nUnfortunately, sometimes you will end up in extreme poverty,"
          " depending on the extreme poverty rate of your country"
          "\n\nPress enter to continue")
    while True:
        input("\nPress enter to generate your person.")
        odds.get_random_persons_country().print_values()