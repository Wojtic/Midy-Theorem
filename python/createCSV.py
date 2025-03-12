import csv
import os
from tests import getMidyNumbersMatrix


def generate_csv(filename="midy_numbers.csv", max_n=5000, m_range=(1, 100)):
    start_m, end_m = m_range

    existing_data = {}
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                existing_data[int(row[0])] = row
    else:
        headers = ["n"]

    for m in range(start_m, end_m + 1):
        if str(m) not in headers:
            headers.append(str(m))

    midy_data = {}
    for m in range(start_m, end_m + 1):
        print(m)
        midy_data[m] = set(getMidyNumbersMatrix(m, max_n))

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for n in range(1, max_n + 1):
            row = existing_data.get(n, [n] + ["0"] * (len(headers) - 1))
            for m_idx, m in enumerate(headers[1:], start=1):
                if start_m <= int(m) <= end_m:
                    row[m_idx] = "1" if n in midy_data[int(m)] else "0"
            writer.writerow(row)

    print(
        f"CSV file '{filename}' updated successfully for m={start_m} to m={end_m}.")


# generate_csv(m_range=(1, 2))
