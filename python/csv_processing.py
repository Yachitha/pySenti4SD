import argparse
import logging
import sys

from utils.csv_formatter import CsvFormatter
from utils.csv_utils import CsvUtils


logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def main():
    parser = argparse.ArgumentParser(description = "Csv file processing")
    parser.add_argument('-i',
                       '--input',
                       help = "path to csv file",
                       type = str,
                       required = True)
    parser.add_argument('-d',
                       '--delimiter',
                       help = 'csv delimiter, use c for comma and sc for semicolon',
                       type = str,
                       default = 'c')
    parser.add_argument('-c',
                       '--columns',
                       help = "column or columns to extract from csv [default = 'text']",
                       type = str,
                       action = 'append',
                       required = True)
    args = parser.parse_args()
    input_csv = args.input
    output_csv = "{}_jar.csv".format(input_csv.split('.')[0])
    print(args.columns)
    try:
        CsvUtils.check_csv(input_csv)
        logging.info("Start formatting csv file")
        try:
            if(args.delimiter == 'c'):
                csvFormatter = CsvFormatter(args.columns, ',')
            elif(args.delimiter == 'sc'):
                csvFormatter = CsvFormatter(args.columns, ';')
            else:
                logging.error('Wrong csv delimiter. Use "c" for comma and "sc" for semicolon.')
                sys.exit(1)
            data = csvFormatter.get_rows(input_csv)
            csvFormatter.write(data, output_csv)
        except IOError as e:
            logging.error(e)
            sys.exit(1)
        logging.info("End formatting csv file")
    except OSError as e:
        logging.error(e)
        sys.exit(1)
    
if __name__ == '__main__':
    main()