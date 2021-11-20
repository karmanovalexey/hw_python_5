import argparse
import json
import os
import tempfile

def get_value(data, key):
    if key not in data:
        return ''
    else:
        return data[key]


def main(args):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    data = {}
    open(storage_path, 'a').close()

    with open(storage_path, 'r+') as f:
        file_con = f.read()
        f.seek(0)
        if file_con: data = dict(json.loads(file_con))
        value = get_value(data, args.key)

        if args.value == None:
                print(value)
        else:
            if value:
                value = ', '.join([value, args.value]) 
            else:
                value = args.value
            data[args.key] = value
            f.write(json.dumps(data))
        return 0

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--value')
    main(parser.parse_args())