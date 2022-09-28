class SimpleReport:
    @classmethod
    def generate(cls, productList: list):
        return (
            f"Data de fabricação mais antiga: "
            f"{cls.get_older_manufactored(productList)}\n"
            f"Data de validade mais próxima: "
            f"{cls.get_nearest_expiration(productList)}\n"
            f"Empresa com mais produtos: "
            f"{cls.get_company_most_products(productList)}"
        )

    def get_older_manufactored(cls, productList: list):
        manufacturing_date = [row["data_de_fabricacao"] for row in productList]
        return min(manufacturing_date)

    def get_nearest_expiration(cls, productList: list):
        expire_dates = [row["data_de_validade"] for row in productList]
        return min(expire_dates)

    def get_company_most_products(cls, productList: list):
        companies_list = [row["nome_da_empresa"] for row in productList]
        return max(set(companies_list), key=companies_list.count)
