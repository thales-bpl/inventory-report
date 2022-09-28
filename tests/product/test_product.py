from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1"
    )

    assert product.id == 1
    assert product.nome_do_produto == "Nicotine Polacrilex"
    assert product.nome_da_empresa == "Target Corporation"
    assert product.data_de_fabricacao == "2021-02-18"
    assert product.data_de_validade == "2023-09-17"
    assert product.numero_de_serie == "CR25 1551 4467 2549 4402 1"
    assert product.instrucoes_de_armazenamento == "instrucao 1"
