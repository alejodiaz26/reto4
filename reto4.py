n, m = input("").split()
verde = amarillo = naranja = rojo = morado = marron = suma_ica = 0
verde1 = amarillo1 = naranja1 = rojo1 = morado1 = marron1 = 0
m = int(m)
n = int(n)

ldatos = []
lcolor = []
for i in range(n):
    ldatos.append([])
    lcolor.append([])

while m > 0:
    ciudad, c = input("").split()
    c = float(c)
    ciudad = int(ciudad)
    if 0 <= c < 0.060:
        ica = ((50 - 0) / (0.059 - 0)) * (c - 0) + 0
    elif 0.060 <= c < 0.076:
        ica = ((100 - 51) / (0.075 - 0.060)) * (c - 0.060) + 51
    elif 0.076 <= c < 0.096:
        ica = ((150 - 101) / (0.095 - 0.076)) * (c - 0.076) + 101
    elif 0.096 <= c < 0.116:
        ica = ((200 - 151) / (0.115 - 0.096)) * (c - 0.096) + 151
    elif 0.116 <= c <= 0.375:
        ica = ((300 - 201) / (0.374 - 0.116)) * (c - 0.116) + 201


    for i in range(n):
        if ciudad == i + 1:
            ldatos[i].append(ica)
    m -= 1

lpromedio = []
for i in range(n):
    if len(ldatos[i]) == 0:
        lpromedio.append(0)
    else:
        lpromedio.append(sum(ldatos[i]) / len(ldatos[i]))

for i in range(n):
    if 0 <= lpromedio[i] <= 5:
        verde += 1
    elif 50 < lpromedio[i] <= 100:
        amarillo += 1
    elif 100 < lpromedio[i] <= 150:
        naranja += 1
    elif 150 < lpromedio[i] <= 200:
        rojo += 1
    elif 200 < lpromedio[i] <= 300:
        morado += 1
    elif lpromedio[i] > 300:
        marron += 1

minval = min(lpromedio)
maxval = max(lpromedio)

if 0 <= minval <= 50:
    colormin = "verde"
elif 50 < minval <= 100:
    colormin = "amarillo"
elif 100 < minval <= 150:
    colormin = "naranja"
elif 150 < minval <= 200:
    colormin = "rojo"
elif 200 < minval <= 300:
    colormin = "morado"
elif minval > 300:
    colormin = "marron"


if 0 <= maxval <= 50:
    colormax = "verde"
elif 50 < maxval <= 100:
    colormax = "amarillo"
elif 100 < maxval <= 150:
    colormax = "naranja"
elif 150 < maxval <= 200:
    colormax = "rojo"
elif 200 < maxval <= 300:
    colormax = "morado"
elif maxval > 300:
    colormax = "marron"


for i in range(n):
    print(i+1)
    if ldatos[i] == []:
        ldatos[i] = [0]
    if lpromedio[i] == []:
        lpromedio[i] = [0]
    print(f"{min(ldatos[i]):.2f} {lpromedio[i]:.2f} {max(ldatos[i]):.2f}")

    ldatossep = ldatos[i]
    verde1 = amarillo1 = naranja1 = rojo1 = morado1 = marron1 = 0
    icamenor = icaigual = icamayor = 0
    for j in range(len(ldatossep)):
        if ldatossep == [0]:
            verde1 = amarillo1 = naranja1 = rojo1 = morado1 = marron1 = 0
        elif 0 <= ldatossep[j] <= 50:
            verde1 += 1
        elif 50 < ldatossep[j] <= 100:
            amarillo1 += 1
        elif 100 < ldatossep[j] <= 150:
            naranja1 += 1
        elif 150 < ldatossep[j] <= 200:
            rojo1 += 1
        elif 200 < ldatossep[j] <= 300:
            morado1 += 1
        elif ldatossep[j] > 300:
            marron1 += 1
        if ldatossep == [0]:
            icamenor = icaigual = icamayor = 0
        elif ldatossep[j] < lpromedio[i]:
            icamenor += 1
        elif ldatossep[j] == lpromedio[i]:
            icaigual += 1
        else:
            icamayor += 1

    print(f"{verde1} {amarillo1} {naranja1} {rojo1} {morado1} {marron1}")
    print(f"{icamenor} {icaigual} {icamayor}")

