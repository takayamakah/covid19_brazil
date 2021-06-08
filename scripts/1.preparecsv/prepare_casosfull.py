#Importa bibliotecas
import os
import time
import pandas

#Função que captura em tela o caminho do diretório
def getpath():
    path = input('Qual o diretório dos arquivos de entrada e saída? (digite o caminho sem barra no final e pressione ENTER)\n')
    return path

#Função que defini em dicionário caminhos de diretórios de arquivos de entrada e saída
def getpathfull(path):
    #Atribui data atual a variavel datenow
    datenow = time.strftime('%Y%m%d', time.localtime())

    #Atribui caminhos de arquivos de entrada e saída a dicionário paths
    paths = {}
    paths['input'] = (f'{path}\\caso_full.csv')
    paths['outputuf'] = (f'{path}\\casos_full_ufs_{datenow}.csv')
    paths['outputct'] = (f'{path}\\casos_full_cities_{datenow}.csv')
    
    return paths

#Função que prepara os dados do arquivo csv em um objeto de dados
def preparedata(path):
    dataset = pandas.read_csv(path)
    return dataset  

#Função que elabora o dataset dependendo do tipo passado como parâmetro
def makedataset(datasource, type):
    #Elabora dataset por UFS
    if type == 'U':
        dataset = datasource[datasource['city'].isnull()]
        dataset = dataset.drop(columns = 'city')
    #Elabora dataset por Cidades
    elif type == 'C':
        dataset = datasource[datasource['city'].notnull()]      
    
    return dataset

#Função que escreve o arquivo csv com o dataset elaborado 
def writercsv(dataset, path):   
    ds = dataset
    ds.to_csv(path, index=False)

#Função que imprimi em tela mensagem final
def messagefinal(ufs, cities):
    #Imprime quantidade de registros processados em cada arquivo de saída e o total de registros processados
    print(f'\nArquivo (ufs): [{ufs}] registros processados!')
    print(f'Arquivo (cities): [{cities}] registros processados!')
    print(f'Total de registros processados: [{ufs+cities}]!')

 
#Função Principal
def main():
    #Limpa tela
    os.system('cls')
    
    #Imprimi título do programa
    print('**********PREPARAR ARQUIVOS DE CASOS DE COVID-19 POR UFS E CIDADES**********\n')

    #Atribui caminho do diretório a variável path
    path = getpath()        
    paths = getpathfull(path)

    #Atribui valores do arquivo csv de entrada em objeto de dados
    datasource = preparedata(paths['input'])
    
    #Atribui datasets separado por UF e por Cidade a objetos de dados
    casosfull_ufs = makedataset(datasource, 'U')
    casosfull_cities = makedataset(datasource, 'C')

    #Elabora os arquivos de saída
    writercsv(casosfull_ufs, paths['outputuf'])
    writercsv(casosfull_cities, paths['outputct']) 
    
    #Imprimi mensagens finais
    messagefinal(casosfull_ufs.shape[0], casosfull_cities.shape[0])
  
    #Fim do programa, executado com sucesso
    print('\nArquivos prontos!\n')  



#Chama função principal
if __name__ == '__main__':
    main()
