from test_lib import test, report

month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    discount_brands = month_discount_brands.split(',')
    
    if brand in discount_brands:
        discount = (price * MONTH_DISCOUNT_PERC)/100
    else:
        discount = 0.0

    return round(discount, 2)

Vespa = calc_discount(100, 'Vespa', month_discount_brands)
expected_result = 10.0
test('Vespa', Vespa, expected_result)

Kymlo = calc_discount(200, 'Kymlo', month_discount_brands)
expected_result = 0.0
test('Kymlo', Kymlo, expected_result)

Yamama = calc_discount(150, 'Yamama', month_discount_brands)
expected_result = 15.0
test('Yamama', Yamama, expected_result)

Kymco = calc_discount(375, 'Kymco', month_discount_brands)
expected_result = 37.5
test('Kymco', Kymco, expected_result)

report()