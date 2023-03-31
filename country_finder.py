#!/usr/bin/python3 python3
import json
import sys


def find_country(country_name):
    with open('countries.json', 'r', encoding='utf-8') as f:
        countries = json.load(f)
    found_countries = []
    input_words = country_name.split()
    for country in countries:
        for word in input_words:
            if word.lower() in country['country'].lower():
                found_countries.append(country)
                break
    return found_countries


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ./script.py <country name>')
        sys.exit()
    country_name = ' '.join(sys.argv[1:])
    found_countries = find_country(country_name)
    if found_countries:
        for country in found_countries:
            print('Country:', country['country'])
            print('Alpha-2 code:', country['alpha2'])
            print('Alpha-3 code:', country['alpha3'])
            print('---')
    else:
        print('Country not found')
