from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, productList: list):
        simple_report = super().generate(productList)
        return (
            f"{simple_report}\n"
            f"{self.get_companies_stock(productList)}"
        )

    def get_companies_stock(productList):
        company_report = "Produtos estocados por empresa:\n"

        companies_list = super().get_companies_list(productList)
        company_stock = Counter(companies_list)
        for company, quantity in company_stock.items():
            company_report += f"- {company}: {quantity}\n"

        return company_report
