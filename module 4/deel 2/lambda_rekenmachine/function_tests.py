import functions, lambdaa, test_lib

getal1 = 3
getal2 = 3

expected = functions.subtraction(getal1, getal2)
result_lambdafunction = lambdaa.calculations["subtract"](getal1, getal2)

test_lib.test(f'Test som functie', expected, result_lambdafunction)

test_lib.report()