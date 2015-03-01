import csv


def to_csv(data, filename, keys=None):
    if keys:
        if sorted(keys) != sorted(data[0].keys()):
            raise ValueError
    else:
        keys = data[0].keys()
    with open(filename, 'wb') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(data)
