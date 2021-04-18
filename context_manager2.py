import os
import zipfile
import requests


class FileFromWeb:
    """
        Context Manager class for downloading and saving ZIP files from internet.
    """

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'exc_type={exc_type}')
        print(f'exc_val={exc_val}')
        print(f'exc_tb={exc_tb}')
        if exc_type == FileNotFoundError:
            print('You choose not existing location at your PC!')
            return True
        elif exc_type == KeyError:
            print('You are trying to extract not existing file!')
            return True
        else:
            return False


with FileFromWeb(r'https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip',
                 r'c:/temp/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        # os.chdir(r'c:/temp/abc')
        z.extract(a_file, r'c:/temp', None)
