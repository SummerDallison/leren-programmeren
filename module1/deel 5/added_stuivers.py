from test_lib import test, report

def round_to_vijf_cents(amount):
    rounded_amount = round(amount * 100/5) * 5/100
    return rounded_amount

for original_amount, expected_rounded_amount in [
    (62.60, 62.60),
    (76.61, 76.60),
    (28.82, 28.80),
    (2.23, 2.25),
    (28.34, 28.35),
    (-42.85, -42.85),
    (31.06, 31.05),
    (-138.47, -138.45),
    (14.88, 14.90),
    (149.69, 149.70)
]:
    result = round_to_vijf_cents(original_amount)
    test(f"original_amount: {original_amount}", expected_rounded_amount, result)

report()