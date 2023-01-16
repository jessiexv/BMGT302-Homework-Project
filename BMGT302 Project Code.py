# Name: Qingyue Li
# Course: BMGT302 
# Section: 0101 
# Date: 11/2/2022

# Read the file of export values and store them in a dictionary
with open('HW4_Export Values.txt', mode = 'r') as exports:
    exports_dict = {} # Stores all the country and its corresponding export amount data
    for each_export in exports:
        country, value = each_export.split('|')
        value = int(value.replace(',', '').replace('\n',''))
        exports_dict[country] = value
        
    print(f'The data has been lodaded and is ready for querying.\
\nThe number of countries available for querying is {len(exports_dict)}')

# Get an corresponding export amount of the input country
def get_export(country, countries_dict):
    one_billion = 1000000000
    export_amt = exports_dict[country]/one_billion # Convert the export anmount in billions
    countries_dict[country] = export_amt
    print(f'{country}: ${export_amt:,.2f}B')

# Generate a dictionary that contains all the report data
def generate_report(values_dict):
    country_name = (input('Country Name/First Letter (Enter 1 when done querying): ')).title()

    # Keep prompting user to query until they have indicated they have finished
    while country_name != '1':
        if len(country_name) > 1 and country_name in exports_dict:
            get_export(country_name, values_dict)
        elif len(country_name) == 1:
            match = False
            for each_country in exports_dict.keys():
                if country_name == each_country[0]:
                    match = True
                    get_export(each_country, values_dict)
            if not match:
                    print('No matching country found')
        else:
            print('No matching country found')
        country_name = (input('Country Name/First Letter (Enter 1 when done querying): ')).title()

# Generate a text file containing each country name and export amount if the user wish so
def generate_file():
    reports_dict = {} # Used to store all the query history data
    generate_report(reports_dict)
    if_report = input('Would you like to have a formatted file of all countries (Yes = 1, No = 0): ')

    # Keep prompting until the user provide an adequate answer
    while if_report != '1' and if_report != '0':
        if_report = input('Would you like to have a formatted file of all countries (Yes = 1, No = 0): ')
    if if_report == '1':
        with open('report.txt', mode = 'w') as reports:
            for country,value in reports_dict.items():
                reports.write(f'{country}: ${value:,.2f}B\n')

# Start the script
generate_file()

# "I pledge on my honor that I have not given nor received any unauthorized 
# assistance on this assignment." 
# -- Qingyue Li
