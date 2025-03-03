# lmao cmptgcs2 hw5. just wanted to write some python code. its been too long my bae.


def f(n: int) -> int:
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


def C(n: int, r: int) -> int:
    comb = f(n) / (f(r) * f(n - r))
    if comb == int(comb):
        return int(comb)
    else:
        raise Exception("combination gave a non-integer value")


print(f"just flavors: {C(28, 3)}")

c_sauces = 0
for m in range(0, 8 + 1):
    c_sauces += C(8, m)

c_toppings = 0
for n in range(0, 12 + 1):
    c_toppings += C(12, n)


print(f"all: {C(28, 3) * c_sauces * c_toppings}")

print(f"just one of everything: {C(28, 1) * C(8, 1) * C(12, 1)}")
print(f"28 * 8 * 12: {28 * 8 * 12}")

print(f"""
#3: {C(20, 8) * C(12, 3) * C(9, 4) * C(5, 5)}""")

print(f"factorial 20: {f(20)}")
print(
    f"ai answer: {f(20) / (f(8) * f(3) * f(4) * f(5))}"
)  # ai did factorial math wrong. idk whats going on in that crazy black box ai magic
