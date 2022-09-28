class SimpleReport:
    @classmethod
    def generate(self, productList: list):
        return (
            f"Data de fabricação mais antiga: "
            f"{self.oldest_date(productList)}\n"
            f"Data de validade mais próxima: "
            f"{self.closest_date(productList)}\n"
            f"Empresa com mais produtos: "
            f"{self.cmpny_bigger_stock(productList)}"
        )

    def oldest_date(productList):
        manufacturing_date = [row["data_de_fabricacao"] for row in productList]
        return min(manufacturing_date)

    def closest_date(productList):
        expire_dates = [row["data_de_validade"] for row in productList]
        return min(expire_dates)

    def cmpny_bigger_stock(productList):
        companies_list = [row["nome_da_empresa"] for row in productList]
        return max(set(companies_list), key=companies_list.count)
