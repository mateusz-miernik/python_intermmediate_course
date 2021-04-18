import csv

with open(r'C:\Users\mateu\Desktop\temp\data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print(' | '.join(row))
    # print(next(csvreader))
    # print(next(csvreader))
    while True:
        try:
            print(' | '.join(next(csvreader)))

        except StopIteration as e:
            break
        else:
            print('--------------')
        finally:
            print("Processing is done!")

