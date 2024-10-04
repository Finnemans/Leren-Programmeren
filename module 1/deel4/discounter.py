from test_lib import test, report

month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10

def discount(price: float, brand: str, discountbrands: str) -> float:
    try:
        discount_brands_list = discountbrands.split(',')
        if brand in discount_brands_list:
            discount = round(price * MONTH_DISCOUNT_PERC / 100, 2)
        else:
            discount = 0.00
    except (ValueError, TypeError):
        discount = 0.00
    return discount

price = 1200
brand = 'Vespa'
discountbrands = 'Vespa,Kymco,Yamama'
expect_content = 120.00
calculated_content = discount(price, brand, discountbrands)
name = 'korting'
test(name, expect_content, calculated_content )

report()