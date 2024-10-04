from test_lib import test, report

rond = 5

def roundtofive(prijs: float) -> float:
    return round(prijs * 100 / rond) * rond/ 100


prijs = 76.61
expect_content = 76.60
calculated_content = roundtofive(prijs)
name = f'rond {prijs} af naar het dichtste komma getal'
test(name, expect_content, calculated_content )

report()