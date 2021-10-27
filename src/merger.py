# https://stackoverflow.com/a/10593823/14345173

import zipfile

def merge(input_zips, reverse=False):

    with zipfile.ZipFile('output.zip', 'a') as output:
        for filename in input_zips:
            zf = zipfile.ZipFile(filename, 'r')
            for n in zf.namelist():
                output.writestr(n, zf.open(n).read())