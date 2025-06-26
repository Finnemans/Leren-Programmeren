def genereer_fibonacci(n):
    if n < 2:
        return [0] if n == 1 else []
    
    reeks = [0, 1]
    for _ in range(2, n):
        volgend_getal = reeks[-1] + reeks[-2]
        reeks.append(volgend_getal)
    return reeks

def bereken_gulden_snede(fib_reeks):
    if len(fib_reeks) < 2:
        return None
    return fib_reeks[-2] / fib_reeks[-1]

aantal_getallen = int(input("Aantal getallen: "))
reeks = genereer_fibonacci(aantal_getallen)
print("Fibonacci-reeks:", reeks)

verhouding = bereken_gulden_snede(reeks)
if verhouding is not None:
    print("Benadering van de gulden snede:", verhouding)
else:
    print("Niet genoeg getallen om de gulden snede te berekenen.")
