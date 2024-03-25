R1 = float(input('Valor da resistência 1: '))
R2 = float(input('Valor da resistência 2: '))
R3 = float(input('Valor da resistência 3: '))
R4 = float(input('Valor da resistência 4: '))
R5 = float(input('Valor da resistência 5: '))
R6 = float(input('Valor da resistência 6: '))
U = float(input('Valor da tensão na fonte: '))

def calcular_corrente(tensao, resistencia):
    return tensao/resistencia

def calcular_tensao(resistencia, corrente):
    return resistencia*corrente

def divisor_corrente(R_equivalente,R_interesse,i):
    return (R_equivalente/R_interesse)*i

Req1 = 1/((1/R1)+(1/R2)+(1/R3))
Req2 = R1*R2/(R1+R2)

Req_circuito = Req1 + Req2 + R3
i_total = calcular_corrente(U, Req_circuito)

resultados = {
    'Req_circuito': Req_circuito,
    'i_total': i_total,
    'R1_i': divisor_corrente(Req2, R1, i_total),
    'R1_U': calcular_tensao(Req2, i_total),
    'R2_i': divisor_corrente(Req2, R2, i_total),
    'R2_U': calcular_tensao(Req2, i_total), 
    'R3_i': i_total,
    'R3_U': calcular_tensao(R3, i_total),
    'R4_i': divisor_corrente(Req1, R4, i_total),
    'R4_U': calcular_tensao(Req1, i_total),
    'R5_i': divisor_corrente(Req1, R5, i_total),
    'R5_U': calcular_tensao(Req1, i_total),
    'R6_i': divisor_corrente(Req1, R6, i_total),
    'R6_U': calcular_tensao(Req1, i_total),
}

print(resultados)