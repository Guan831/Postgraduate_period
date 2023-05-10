import csv


def csv_jian(csv_reader1, csv_reader2):
    csv_write = [csv_reader2[0], csv_reader2[1]]
    for i in range(2, len(csv_reader1)):
        csv_write.append(csv_reader2[i]-csv_reader1[i])
    return csv_write


if __name__ == '__main__':
    file = "2022/probspace/train_data.csv"
    open_file = open(file)
    csv_reader = csv.reader(open_file)
    open_file.close()
    print(csv_reader)
    csv_write = []
    len_csv = 351
    for i in range(1, len_csv-1):
        csv_jian
        csv_write.append(csv_jian(csv_reader[i+1], csv_reader[i]))
    print(csv_write)
