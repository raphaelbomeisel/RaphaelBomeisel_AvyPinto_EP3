# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:49:29 2015

@author: Raphael
"""
def Dicionario():
    alimentos=open("alimentos.csv","r")
    ler=alimentos.readlines()


    dictio={}
    
#PREENCHE OS DICIONARIOS COM VALORES. AS CHAVES SÃO OS NOMES
    #DOS ALIMENTOS E SEUS VALORES NUTRICIONAIS SÃO O CONTEÚDO
    for linhas in ler[1:]:
        valores_tabela=linhas.strip().split(",")

        
        dictio[valores_tabela[0]]=[valores_tabela[1],valores_tabela[2],valores_tabela[3],valores_tabela[4],valores_tabela[5]]

    
    alimentos.close()
    return dictio
def AlimentosUsuario():
    usuario=open("usuario.csv","r")
    ler=usuario.readlines()

#SEPARA OS ITENS DOS NUTRIENTES INGERIDOS PELO USUARIO
    dictio2={}
#SEPARA AS LINHAS
    for linhas in ler[2:]:
        valores_usuario=linhas.strip().split(",")
#VERIFICA SE JÁ EXISTE UMA CHAVE (DATA) EXISTENTE. 
    #SE SIM, ACRESCENTA OS VALORES À CHAVE
        if valores_usuario[0]==dictio2[valores_usuario[0]]:
            dictio2[valores_usuario[0]].append([valores_usuario[1],valores_usuario[2]])
    #SENÃO, CRIA OUTRA CHAVE               
        else:
            dictio2[valores_usuario[0]]=[valores_usuario[1],valores_usuario[2]]
        
        usuario.close()
    return dictio2



#roda as chaves uma a uma, comparando os nomes e somando os
#valores nutriconais

def CalculaNutrientes(dictio,dictio2):
    
    n=0   
    for j in range(1,None,2):        
        for i in range(0,None,7):
            calorias=0    
            carboidratos=0
            proteinas=0
            gorduras=0
            if dictio2[n][j]==dictio[i]:
                gramas=dictio[0][j+1]/100
                calorias=calorias+dictio[i][i+1]*gramas                
                proteinas=proteinas+dictio[i][i+2]*gramas
                carboidratos=carboidratos+dictio[i][i+3]*gramas
                gorduras=gorduras+dictio[i][i+4]*gramas
            n=n+1  
        
    return calorias,proteinas,carboidratos,gorduras    
        
        
        
        
        
        
        
        
        
        
    