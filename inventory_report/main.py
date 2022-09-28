from reports.simple_report import SimpleReport
import csv


def main():
    file = csv.DictReader('./inventory_report/data/inventory.csv')
    print(file)
    print(SimpleReport.generate(file))
    pass


main()

# def main():
#     pass
