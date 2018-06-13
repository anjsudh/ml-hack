import json
import os
import timeit
from itertools import chain
from models.apyori import parse_args, load_transactions, apriori
from predictors.generate_rules import generate_rules_obj


def main(**kwargs):
    cwd = os.getcwd()
    _parse_args = kwargs.get('_parse_args', parse_args)
    _load_transactions = kwargs.get('_load_transactions', load_transactions)
    _apriori = kwargs.get('_apriori', apriori)

    args = [
                '-d=;',
                '-s=0.05',
                '-c=0.7',
                '-o='+cwd+'/../data/trial2/apriori_output_temp.json',
                cwd+'/../data/trial2/apriori_input.csv'
            ]
    args = _parse_args(args)
    start_time = timeit.default_timer()
    transactions = _load_transactions(
        chain(*args.input), delimiter=args.delimiter)
    result = _apriori(
        transactions,
        max_length=args.max_length,
        min_support=args.min_support,
        min_confidence=args.min_confidence)
    with open("../data/trial2/apriori_output.csv", 'w') as output_file:
        for record in result:
            for i in range(len(record[2])):
                base = record[2][i][0]
                add = [x for x in record[2][i][1]][0]
                conf = record[2][i][2]
                output_file.write(("%s|%s|%.2f\n" % (";".join(base), add, conf)))
    end_time = timeit.default_timer()
    print(start_time, end_time, end_time - start_time)
    generate_rules_obj("../data/trial2/apriori_output.csv")

if __name__ == '__main__':
    main()
