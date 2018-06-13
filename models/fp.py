#! /usr/bin/env pypy
import os
import timeit

from models.FPGrowth import FPGrowth
from predictors.generate_rules import generate_rules_obj

__author__ = 'mhwong'
if __name__ == '__main__':
    cwd = os.getcwd()
    with open("../data/trial2/fp_input.csv") as input_file:
        with open("../data/trial2/fp_input_temp.csv", 'w') as output_file:
            for line in input_file:
                output_file.write(line.replace(' ', '_'))
    start_time = timeit.default_timer()
    FPGrowth(cwd+'/../data/trial2/fp_input_temp.csv', float(0.05), float(0.7))
    end_time = timeit.default_timer()
    print(start_time, end_time, end_time-start_time)
    generate_rules_obj(cwd+'/../data/trial2/fp_output.csv')
