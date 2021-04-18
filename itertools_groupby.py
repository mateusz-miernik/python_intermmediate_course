import os
import itertools as it

path = r'C:\Users\mateu\PycharmProjects\pre_advance_course2'


def scantree(path):
    for obj in os.scandir(path):
        if obj.is_dir():
            yield obj
            yield from scantree(obj.path)
        else:
            yield obj


listening = scantree(path)
listening = sorted(listening, key=lambda x: x.is_dir())
for obj in listening:
    print('Object: {}, is dir? {}'.format(obj.path, obj.is_dir(),))

for item in it.groupby(listening, key=lambda x: x.is_dir()):
    print('is_dir?: {}, elements: {}'.format(item[0], [x.path for x in list(item[1])]))