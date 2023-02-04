# game-of-life
This is a game to simulate your outcome in life based on country statistics
like population size, median income, poverty rate, and life expectancy.

The game is written in python, and you will need python installed to run it.
To run the game:
  - python runner.py


This is also a practice coding exercise.
You can use the csv data I collected to create your own version of the game.
To do this:

    - do not look at data_parsing_helper.py or generate_odds.py in /src
    - Create steps to
        - parse the csv files
            - NOTE: the csv files are encoded in cp1252, so you will want to use "with open(csv_file, encoding="cp1252")..."
        - get the data for all the countries that have a population value
        - cross-reference this to all the countries that have a life expectancy value
        - cross-reference this to all the countries that have an extreme poverty rate.
          If there is no rate for a country set the poverty rate to 0
        - cross-reference this to all the countries that have a median income
            - use the more reliable annual income metrics first, if the country isn't in that data, use the monthly median
              income and multiply it by 12, if the country doesn't exist in either set of data drop it.
        - create a random way to select the countries based on their population sizes
        - once the country is selected, use the extreme poverty rate to print of they are in extreme poverty
            - if a person is not in extreme poverty, print out the stats associated with that country
        - create your own runner or re-use the runner.py


NOTE: The data was a bit hard to collect and seemed to vary a bit from source to source.
      If you have questions about my data, I included the sources.
