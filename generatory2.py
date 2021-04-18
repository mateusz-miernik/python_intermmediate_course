import os
import requests

# try:
#     os.makedirs('c:/temp/links_to_check', exist_ok=True)
# except:
#     pass
#
# with open('c:/temp/links_to_check/pl.txt', 'w') as f:
#     f.write('http://www.wykop.pl/\n')
#     f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
#     f.write('http://www.demotywatory.pl')
#
# with open('c:/temp/links_to_check/com.txt', 'w') as f:
#     f.write('http://www.realpython.com/\n')
#     f.write('http://www.nonexistenturl.com/\n')
#     f.write('http://www.stackoverflow.com')

path = r'c:/temp/links_to_check/'


def gen_get_files(dir):
    for file in os.listdir(dir):
        yield(os.path.join(dir, file))


def gen_get_file_lines(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            current_line = line.rstrip('\n')
            yield current_line


def check_webpage(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except Exception as e:
        return False


for file in gen_get_files(path):
    for line in gen_get_file_lines(file):
        status = check_webpage(line)
        print(line, status)