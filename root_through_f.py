import os
import sys

# CONSTANTS
WARNING = 'WARNING'

def writefile(fname, data):
    print(f'############################## Writing File: {fname} ############################## ')
    try:
        with open(fname, 'w', encoding='utf-8') as file:
            file.write(str(data))
    except Exception as e:
        print(e)
        sys.exit(1)

def clean_output(data):
    print('############################## Cleaning Data from Clam AV ############################## \n')
    if WARNING not in data:
        print('############################## Nothing to show from file ############################## \n')
        return

    lines = data.split('\n')
    clean_lines = []

    first_line_found = False
    last_line_found = False

    for index in range(len(lines)):
        line = lines[index]

        if WARNING in line:
            if not first_line_found:
                first_line_found = True
                line = lines[index - 1]
                clean_line = line.split(':')[0]
                clean_lines.append(clean_line)

            if not last_line_found:
                if WARNING not in lines[index + 1] and WARNING not in lines[index + 2]:
                    last_line_found = True
        elif first_line_found:
            clean_line = line.split(':')[0]
            clean_lines.append(clean_line)

    writefile('output.txt', '\n'.join(clean_lines))

def read_file(fname):
    with open(fname, 'r', encoding='utf-8') as file:
        clean_output(file.read())
    os.remove(os.path.join(os.getcwd(), fname))

def usage():
    print('This script just cleans the output from ClamAV')
    print('Use this command:')
    print('python3 root_through_f.py /clamav/output/path')
    print()
    print('Get ClamAV read file as root:')
    print('Run this command')
    print('sudo /usr/bin/clamav -f /pathof/file/toread')
    print('Copy the output to a file and use it on this script')

def main():
    if len(sys.argv) < 2:
        usage()
        return
    read_file(sys.argv[1])

if __name__ == '__main__':
    main()
