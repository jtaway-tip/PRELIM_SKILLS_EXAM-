import json
import csv

file_json = '/home/devasc/labs/devnet-src/python/Prelim_Taway/covid_cases.json'
file_csv = '/home/devasc/labs/devnet-src/python/Prelim_Taway/parsed_data.csv'

with open(file_json,'r') as infile:
    covid_data = json.loads(infile.read())

with open(file_csv, 'w') as outfile:
    file = csv.writer(outfile)
    file.writerow(["dateRep","countriesAndTerritories", "cases", "deaths" ])

    for items in covid_data["records"]:
        file.writerow([items["dateRep"],items["countriesAndTerritories"],items["cases"],items["deaths"]])