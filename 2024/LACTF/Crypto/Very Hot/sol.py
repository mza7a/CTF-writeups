from z3 import *
from Crypto.Util.number import long_to_bytes

x = Real('x')
n = 10565111742779621369865244442986012561396692673454910362609046015925986143478477636135123823568238799221073736640238782018226118947815621060733362956285282617024125831451239252829020159808921127494956720795643829784184023834660903398677823590748068165468077222708643934113813031996923649853965683973247210221430589980477793099978524923475037870799
equation = x**3 + 18*x**2 - 72*x - n


solver = Solver()

solver.add(equation == 0)
if solver.check() == sat:
    model = solver.model()
    solution = model[x]

p = int(str(solution).split('.')[0])


n2 = p*(p+6)*(p+12)
if (n2 == n) : print("alike !")

e = 0x10001
ct = 9953835612864168958493881125012168733523409382351354854632430461608351532481509658102591265243759698363517384998445400450605072899351246319609602750009384658165461577933077010367041079697256427873608015844538854795998933587082438951814536702595878846142644494615211280580559681850168231137824062612646010487818329823551577905707110039178482377985

phi = (p-1)*((p + 6) - 1)*((p+12) - 1)
d = pow(e, -1, phi)

msg = pow(ct, d, n)

print(long_to_bytes(msg))
