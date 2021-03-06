import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    save_url_to_file(url, tmpfile_path)
    shutil.copyfile(tmpfile_path, file_path)
except requests.exceptions.ConnectionError as e:
    print(f'Probably an url address is wrong... {e}')
except PermissionError as e:
    print('"Read only" attribute is set for file desired to download.\n{}'.format(e))
except FileNotFoundError as e:
    print(f'{e}')
except Exception as e:
    print(f"Some undefined exception occurred, {e}")
else:
    print('Job is done! Success!')
finally:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    print('Processing is done!')