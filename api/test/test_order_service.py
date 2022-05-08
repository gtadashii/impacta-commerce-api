from math import prod
from api.service import order_service


def test_sum_total():
    # Given
    products = """
    [
        {
            "code": "1",
            "title": "Caneca Personalizada de Porcelana",
            "thumbnail": "https://meu-ecommerce.com/img/pt/tb-pers-porc.jpg",
            "qty": 1,
            "unitPrice": 123.45
        },
        {
            "code": "2",
            "title": "Caneca Importada Personalizada em Diversar Cores",
            "thumbnail": "https://meu-ecommerce.com/img/pt/tb-import-colors.jpg",
            "qty": 2,
            "unitPrice": 123.45
        },
        {
            "code": "3",
            "title": "Caneca de Tulipa",
            "thumbnail": "https://meu-ecommerce.com/img/pt/tb-tuli.jpg",
            "qty": 1,
            "unitPrice": 123.45
        }
    ]
    """
    expected = 493.8
    # When
    actual = order_service.sum_total(products)

    # Then
    assert expected == actual
