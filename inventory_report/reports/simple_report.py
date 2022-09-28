class SimpleReport:
    @classmethod
    def generate(cls, productList: list):
        return (
            f"Data de fabricação mais antiga: {cls.oldest_date(productList)}\n"
            f"Data de validade mais próxima: {cls.closest_date(productList)}\n"
            f"Empresa com mais produtos: {cls.cmpny_bigger_stock(productList)}"
        )

    def oldest_date(cls, productList: list):
        manufacturing_date = [row["data_de_fabricacao"] for row in productList]
        return min(manufacturing_date)

    def closest_date(cls, productList: list):
        expire_dates = [row["data_de_validade"] for row in productList]
        return min(expire_dates)

    def cmpny_bigger_stock(cls, productList: list):
        companies_list = [row["nome_da_empresa"] for row in productList]
        return max(set(companies_list), key=companies_list.count)
