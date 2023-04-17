import math
FILENAME = "input.txt"


with open(FILENAME, "r") as file:
    data = file.read()
    p = data.count("1")/(data.count("1")+data.count("0"))
    q = 1-p


erwartungswert = p
varianz = p*q
standardabweichung = math.sqrt(p*q)
variationkoeffizient = math.sqrt(q/p)
schiefe = (1-2*p)/math.sqrt(p*q)
entropie = (-q*math.log2(q))-(p*math.log2(p))
print("erwartungswert " + str(erwartungswert))
print("varianz " + str(varianz))
print("standartabweichung " + str(standardabweichung))
print("variationkoeffizient " + str(variationkoeffizient))
print("schiefe " + str(schiefe))
print("entropie " + str(entropie))