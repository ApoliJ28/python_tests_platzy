def calculate_total(products, discount_percent=0):
    total = 0
    for product in products:
        total += product['price'] *  (1 + discount_percent/100)
    return round(total,2)


def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {"name": "Notebook", "price": 5}
    ]
    assert calculate_total(products) ==  5

def test_calculate_total_with_multiple_product():
    products = [
        {"name": "Notebook", "price": 5},
        {"name": "Book", "price": 1},
        {"name": "Pen", "price": 1},
    ]
    
    assert calculate_total(products) ==  7

def test_calculate_total_with_single_product_with_discount():
    products = [
        {"name": "Notebook", "price": 5}
    ]
    assert calculate_total(products, 10) ==  5.5

def test_calculate_total_with_multiple_product_with_discount():
    products = [
        {"name": "Notebook", "price": 5},
        {"name": "Book", "price": 1},
        {"name": "Pen", "price": 1},
    ]
    
    assert calculate_total(products, 10) ==  7.7

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()
    test_calculate_total_with_single_product_with_discount()
    test_calculate_total_with_multiple_product_with_discount()