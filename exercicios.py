from math import sqrt
from terminaltables import AsciiTable

listaNumeros = [15, 55, 65, 12, 5, 5, 79, 65, 14, 17, 19, 42, 23, 19, 17, 6, 8, 5, 29, 40, 32, 30, 31]
listaNumeros.sort()

def calcularMedia():
    soma = sum(listaNumeros)
    return soma / len(listaNumeros)

def calcularAmplitudeTotal():
    maior = max(listaNumeros)
    menor = min (listaNumeros)
    return maior - menor

def calcularDesvioMedio():
    media = calcularMedia()
    n = len(listaNumeros)
    somatoria = 0

    for c in range (n):
        somatoria += abs(listaNumeros[c] - media)

    return somatoria / n

def calcularVariancia():
    media = calcularMedia()
    n = len(listaNumeros)
    variancia = 0

    for c in range(n):
        variancia += (listaNumeros[c] - media) ** 2

    return variancia / n

def calcularDesvioPadrao():
    variancia = calcularVariancia()

    return sqrt(variancia)

def calcularPosicoesDesvioQuartilico():
    n = len(listaNumeros)

    Q1 = (n + 1) / 4
    Q2 = ((n + 1) * 2) / 4
    Q3 = ((n + 1) * 3) / 4

    return [Q1, Q2, Q3]

def calcularDesvioQuartilico():
    Q = calcularPosicoesDesvioQuartilico()

    return {'Q1': listaNumeros[int(Q[0])], 
            'Q2': listaNumeros[int(Q[1])],
            'Q3': listaNumeros[int(Q[2])]}

def calcularDesvioInterQuartilico():
    desvioQuartilico = calcularDesvioQuartilico()

    return desvioQuartilico['Q3'] - desvioQuartilico['Q1']

def listarItensDistintos():
    lista = list(set(listaNumeros)) # TRANSFORMA A LISTA NUM SET, QUE É UM TIPO DE LISTA QUE NÃO POSSUI VALORES REPETIDOS. DEPOIS, TRANFORMA DE VOLTA PARA UMA LISTA.
    lista.sort()
    return lista
    
def calcularTabelaFrequencia():
    listaDistinta = listarItensDistintos()
    freqTotal = len(listaNumeros)
    freqAcm = 0
    tabela = {}
    
    for c in range(len(listaDistinta)):
        
        freqAbs = listaNumeros.count(listaDistinta[c]) # CONTA A QUANTIDADE DE VEZES QUE UM NÚMERO APARECE NA LISTA
        freqRel = freqAbs / freqTotal
        freqAcm += freqAbs

        valores = [freqAbs, freqRel, freqAcm, round(freqRel * 100, 4)] 
        tabela[listaDistinta[c]] = valores[:]
        valores.clear()

    header = ['Intervalo', 'Frequência Absoluta', 'Frequência Relativa', 'Frequência Acumulada', '% com 4 decimais']
    table_data = [header]

    for key, value in tabela.items():
        linha = [key]
        linha.extend(value)

        table_data.append(linha)

    table = AsciiTable(table_data)

    return table.table

media = calcularMedia()
amplitudeTotal = calcularAmplitudeTotal()
desvioMedio = calcularDesvioMedio()
desvioPadrao = calcularDesvioPadrao()
posicoesDesvioQuartilico = calcularPosicoesDesvioQuartilico()
desvioQuartilico = calcularDesvioQuartilico()
desvioInterQuartilico = calcularDesvioInterQuartilico()
tabelaFrequencia = calcularTabelaFrequencia()


#-------------------- RESULTADOS --------------------

print(f'Lista: {listaNumeros}\n'
      f'\nExercício 2\n' +
      f'a) Média: {media:.2f}\n' +
      f'b) Amplitude Total: {amplitudeTotal:.2f}\n' +
      f'c) Desvio Médio: {desvioMedio:.2f}\n' +
      f'd) Desvio Padrão: {desvioPadrao:.2f}\n\n' +
      f'Posições do Desvio Quartílico: \n' +
      f'    Q1 -> {int(posicoesDesvioQuartilico[0])}\n'
      f'    Q2 -> {int(posicoesDesvioQuartilico[1])}\n'
      f'    Q3 -> {int(posicoesDesvioQuartilico[2])}\n'
      f'e) Desvio Quartílico: {desvioQuartilico}\n' +
      f'f) Desvio Interquartílico: {desvioInterQuartilico:.2f}\n' +
      f'g) Tabela de frequência:\n' +
      f'{tabelaFrequencia}')

