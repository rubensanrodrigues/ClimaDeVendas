import os
import shutil

# Etapa 01
from e01_01_join_estmet_pluv import juntar_dados_meteorologicos
from e01_02_analise_dados_plot import gerar_grafico_meteorologico
# Etapa 02
from e02_01_calcular_peso_media import calcular_pesos_estacoes
from e02_02_estimar_valor_media import estimar_valores_ibitinga
from e02_03_analise_dados_plot import gerar_grafico_estimado_ibitinga
# Etapa 03
from e03_01_calcular_distancia import calcular_distancias_ibitinga
from e03_02_calcular_peso_distancia import calcular_pesos_por_distancia
from e03_03_estimar_valor_distancia import estimar_valores_ibitinga_por_distancia
from e03_04_analise_dados_plot import gerar_grafico_estimativa_distancia
# Etapa 04
from e04_01_estimar_peso_media_e_distancia import calcular_pesos_media_e_distancia
from e04_02_estimar_valor_media_e_distancia import estimar_ibitinga_media_e_distancia
from e04_03_analise_dados_plot import plotar_grafico_estimado_med_dist

def run_all():
    print("\nIniciando execução completa das etapas...\n")
    
    print("Executando: juntar_dados_meteorologicos()")
    juntar_dados_meteorologicos()
    
    print("Executando: gerar_grafico_meteorologico()")
    gerar_grafico_meteorologico()
    
    print("Executando: calcular_pesos_estacoes()")
    calcular_pesos_estacoes()
    
    print("Executando: estimar_valores_ibitinga()")
    estimar_valores_ibitinga()
    
    print("Executando: gerar_grafico_estimado_ibitinga()")
    gerar_grafico_estimado_ibitinga()
    
    print("Executando: calcular_distancias_ibitinga()")
    calcular_distancias_ibitinga()
    
    print("Executando: calcular_pesos_por_distancia()")
    calcular_pesos_por_distancia()
    
    print("Executando: estimar_valores_ibitinga_por_distancia()")
    estimar_valores_ibitinga_por_distancia()
    
    print("Executando: gerar_grafico_estimativa_distancia()")
    gerar_grafico_estimativa_distancia()
    
    print("Executando: calcular_pesos_media_e_distancia()")
    calcular_pesos_media_e_distancia()
    
    print("Executando: estimar_ibitinga_media_e_distancia()")
    estimar_ibitinga_media_e_distancia()
    
    print("Executando: plotar_grafico_estimado_med_dist()")
    plotar_grafico_estimado_med_dist()

def apagar_diretorios_se_existirem(diretorios):
    """Apaga os diretórios fornecidos caso existam."""
    for diretorio in diretorios:
        if os.path.exists(diretorio) and os.path.isdir(diretorio):
            print(f"Apagando diretório: {diretorio}")
            shutil.rmtree(diretorio)
        else:
            print(f"Diretório não encontrado, pulando: {diretorio}")

def criar_diretorios_se_nao_existirem(diretorios):
    """Cria os diretórios fornecidos caso não existam."""
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f"Criado diretório: {diretorio}")
        else:
            print(f"Diretório já existe, pulando criação: {diretorio}")

if __name__ == "__main__":
    diretorios = ['e01', 'e02', 'e03', 'e04']
    
    apagar_diretorios_se_existirem(diretorios)
    criar_diretorios_se_nao_existirem(diretorios)

    run_all()
