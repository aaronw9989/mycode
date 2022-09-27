#!/usr/bin/python3
import csv

def main():
    with open('superbirthday.csv', mode='r') as csv_file:
                    
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        with open('regularbirthday.csv', mode='w') as csv_custom:
            csv_reader2 = csv.DictReader(csv_custom)


            for row in csv_reader:
                if line_count == 0:
                # print(f'Column names are {", ".join(row)}') # python3.6 way
                                                              ## to do things
                    print('Column names are {}'.format(", ".join(row)))
                    print('Column names are {}'.format(", ".join(row)), file='regularbirthday.csv')
                    line_count += 1
            # print(f'\t{row["name"]} aka {row["heroname"]} was born in {row["birthday month"]}.')
            # above is the python3.6+ way to do things
                print('\t{} aka {} was born in {}.'.format(row["name"],row["heroname"],row["birthday month"]))
                line_count += 1
        # print(f'Processed {line_count} lines.') # python3.6 way to do things
        print('Processed {} lines.'.format(line_count))
if __name__ == "__main__":
    main()

