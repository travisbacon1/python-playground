
import csv

def open_csv(filename):
    '''Opens a file an returns lines as an array
    
    Parameters
    ------
    filename: `string`
    
    Returns
    ------
    opened_file: `list`
    '''

    lines = []
    with open(filename, 'r', newline='') as csv_file:
        open_file = csv.reader(csv_file, delimiter=',')
        for line in open_file:
            lines.append(line)

    return lines


def print_line(file_lines, line_number):
    '''Prints the line number of a given file
    
    Parameters
    ------
    filename: `csv object`
    
    Returns
    ------
    None
    '''

    print(file_lines[line_number])


def main():
    file_to_print = open_csv('data.csv')
    print_line(file_to_print, 1)

if __name__ == "__main__":
    main()
