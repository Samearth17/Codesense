import pandas as pd

country_data = [ 
    ["Afghanistan", "Kabul"],
    ["Albania", "Tirana"],
    ["Algeria", "Algiers"],
    ["Andorra", "Andorra la Vella"],
    ["Angola", "Luanda"],
    ["Antigua and Barbuda", "St. John's"],
    ["Argentina", "Buenos Aires"],
    ["Armenia", "Yerevan"],
    ["Australia", "Canberra"],
    ["Austria", "Vienna"]
]

df = pd.DataFrame(country_data, columns=["Country", "Capital"])
print(df)