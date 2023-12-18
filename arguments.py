# Accepting arguments in command line
# import sys

# name = sys.argv[1]

# print(f"Hello {name}")

import argparse

parser = argparse.ArgumentParser(description="This program prints the name of the user")

parser.add_argument('-c' , '--color' , metavar="color" , required=True , choices={'red' , 'blue' , 'green' , 'yellow'} , help="the color to search for ")

args = parser.parse_args()

print(args.color)