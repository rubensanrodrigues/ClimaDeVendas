import json
from math import radians, sin, cos, sqrt, atan2

def calcular_distancias_ibitinga():
    # Diretório de entrada e saída
    dados = 'dados/'
    e03_dir = 'e03/'
    ponto_referencia = 'A737_IBITINGA'

    # Função para calcular a distância entre dois pontos geográficos
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371  # Raio da Terra em km

        # Converte graus para radianos
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d = R * c

        return d  # Distância em km

    # 1. Lê o arquivo JSON com as coordenadas
    caminho_coordenadas = f'{dados}coordenadas.json'
    with open(caminho_coordenadas, 'r') as arquivo_json:
        coordenadas = json.load(arquivo_json)

    # 2. Recupera a coordenada da estação de referência
    lat1 = coordenadas[ponto_referencia]['lat']
    lon1 = coordenadas[ponto_referencia]['lon']

    # 3. Calcula distâncias para as demais estações
    distancias_ibitinga = {}
    for ponto, info in coordenadas.items():
        if ponto == ponto_referencia:
            continue  # pula a própria estação

        lat2, lon2 = info['lat'], info['lon']
        distancia = haversine(lat1, lon1, lat2, lon2)
        distancias_ibitinga[ponto] = round(distancia, 3)

    # 4. Salva as distâncias em um arquivo JSON
    caminho_saida = f'{e03_dir}distancias_ibitinga.json'
    with open(caminho_saida, 'w') as arquivo_json:
        json.dump(distancias_ibitinga, arquivo_json, indent=4)

    print(f"Distâncias calculadas com sucesso e salvas em: {caminho_saida}")

# Executa a função se o script for chamado diretamente
if __name__ == "__main__":
    calcular_distancias_ibitinga()
