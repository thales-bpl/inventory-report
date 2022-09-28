from abc import ABC
import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory(ABC):
    @classmethod
    def import_data(path, type):
        report = Inventory.reader(path)

        if type == 'simples':
            return SimpleReport.generate(report)

        if type == 'completo':
            return CompleteReport.generate(report)

    @classmethod
    def reader(path):
        if ".csv" in path:
            report = Inventory.csv_to_dict(path)
        if ".json" in path:
            report = Inventory.json_to_dict(path)
        if ".xml" in path:
            report = Inventory.xml_to_dict(path)

        return report

    @classmethod
    def csv_to_dict(path):
        with open(path, encoding='utf-8') as file:
            data = list(csv.DictReader(file))
        return data

    @classmethod
    def json_to_dict(path):
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
        return data

    @classmethod
    def xml_to_dict(path):
        with open(path, encoding='utf-8') as file:
            data = xmltodict.parse(file.read())
        return data["dataset"]["record"]
