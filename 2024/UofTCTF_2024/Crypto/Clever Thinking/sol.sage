m = 235322474717419
F = GF(m)
C = EllipticCurve(F, [0, 8856682])

public_base = (185328074730054:87402695517612:1)

Q1 = (184640716867876:45877854358580:1)
Q2 = (157967230203538:128158547239620:1)

my_private_key = discrete_log(Q1, public_base, public_base.order(), operation='+')

print(my_private_key * Q2)
