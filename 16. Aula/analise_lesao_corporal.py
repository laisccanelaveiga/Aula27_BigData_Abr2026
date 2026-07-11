import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# github copilot chat

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Obter dados

try:
    print("Obtendo dados...")

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # delimitando as variáveis
     
    # delimitando as variáveis
    df_lesao_corporal = df_ocorrencias[['munic', 'cisp', 'lesao_corp_dolosa', 'lesao_corp_morte']]

    # agrupar por município e cisp
    df_lesao_corporal = df_lesao_corporal.groupby(['munic', 'cisp'], as_index=False)[['lesao_corp_dolosa', 'lesao_corp_morte']].sum()

    # ordenar dados por lesão corporal dolosa
    df_lesao_corporal = df_lesao_corporal.sort_values(by='lesao_corp_dolosa', ascending=False)

    print(df_lesao_corporal.head(20))
    print("\nDados obtidos com sucesso!")
    

except Exception as e:
    print(f'Erro ao obter dados: {e}')


try:
    # calcular correlação entre lesão corporal dolosa e lesão corporal com morte
    print("\nCalculando correlação entre lesão corporal dolosa e lesão corporal com morte...")  

    # calcular a correlação
    correlacao = np.corrcoef(df_lesao_corporal['lesao_corp_dolosa'], df_lesao_corporal['lesao_corp_morte'])[0, 1]

    print(f"Correlação: {correlacao}") # a correlação ela tenta comparar todas as variáveis varias vezes, em matriz, a gente tem lesao_corp_dolosa e lesao_corp_morte, então ela vai comparar essas duas variáveis e vai retornar um valor entre -1 e 1, onde -1 é uma correlação negativa perfeita, 0 é nenhuma correlação e 1 é uma correlação positiva perfeita.
    

except Exception as e:
    print(f'Erro ao calcular correlação: {e}')

# crie uma estrutura de try expect para plotar o gráfico de dispersão entre lesão corporal dolosa e lesão corporal com morte    
try:
    print("\nPlotando o gráfico de dispersão entre lesão corporal dolosa e lesão corporal com morte...")  

    # plotando o gráfico de dispersão
    plt.scatter(df_lesao_corporal['lesao_corp_dolosa'], df_lesao_corporal['lesao_corp_morte'])
    plt.title('Correlação entre Lesão Corporal Dolosa e Lesão Corporal com Morte')
    plt.xlabel('Lesão Corporal Dolosa')
    plt.ylabel('Lesão Corporal com Morte')
    plt.show()

except Exception as e:
    print(f'Erro ao plotar gráfico: {e}')

print('\nAnálise dos Dados')
print('''
     0,815 é uma correlação linear forte e positiva entre lesão corporal dolosa e lesão corporal seguida de morte por CISP. 
     Delegacias com mais ocorrências de lesão dolosa em geral também registram mais casos fatais, 
     o que sugere que ambos os indicadores capturam um padrão comum de violência na área.
''')

# # R = 1: Correlação positiva perfeita; À medida que uma variável aumenta, a outra também aumenta de forma proporcional.​
# # R = −1: Correlação negativa perfeita; À medida que uma variável aumenta, a outra diminui de forma proporcional.​
# ​ = 0: Nenhuma correlação linear; as variáveis não apresentam relação linear.​      
# Guideline de observação do r²:
# Os valores de r podem variar entre -1 a 1:
#
# Por outro lado, Rumsey (2023) traz a seguinte sugestão de tamanhos de efeito:
#   • r = |±1|    -> relação linear perfeita;
#   • r = |±0,70| -> relação linear forte;
#   • r = |±0,50| -> relação linear moderada;
#   • r = |±0,30| -> relação linear fraca;
#   • r = 0       -> ausência de relação linear.
