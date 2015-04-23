le_arquivo=open("usuario.csv","r", encoding="utf-8").readlines()
usuario= le_arquivo[1].split(",")
nome = usuario[0] 
idade = int(usuario[1])
peso = float(usuario[2])
sexo = usuario[3].upper().strip()
altura = float(usuario[4])
fator = usuario[5].upper().strip() 
print(nome,",",idade,"anos",",", peso,"kg", "," "sexo", sexo,",", "altura", altura,",", "fator:", fator)

def Calculo_TMB(peso,altura,idade):                         
     
    if sexo == "M": 
        TMB= 88.36+(13.4*peso)+(4.8*altura*100)-(5.7*idade)
    elif sexo == "F":
        TMB= 447.6+(9.2*peso)+(3.1*altura)-(4.3*idade) 
    return TMB
print("A sua Taxa Metabolica Basal é: ", Calculo_TMB(peso,altura,idade))
 
    
def Calculo_Necessidade_Cal(fator):  
    
    if fator == "MÍNIMO":
        Calculo_Necessidade_Cal = Calculo_TMB(peso,altura,idade)*1.2
    elif fator == "BAIXO":
       Calculo_Necessidade_Cal  = Calculo_TMB(peso,altura,idade)*1.375
    elif fator == "MÉDIO":    
        Calculo_Necessidade_Cal  = Calculo_TMB(peso,altura,idade)*1.55
    elif fator == "ALTO":    
        Calculo_Necessidade_Cal  = Calculo_TMB(peso,altura,idade)*1.725
    elif fator == "MUITO ALTO":    
        Calculo_Necessidade_Cal  = Calculo_TMB(peso,altura,idade)*1.9        
    return Calculo_Necessidade_Cal 
print("A sua necessidade calórica diária é: ", Calculo_Necessidade_Cal(fator))


def Calculo_Imc(peso,altura):
    Imc=(1.3*peso) /altura**2.5
    return Imc
print("O seu Índice de Massa Corporal é: ", Calculo_Imc(peso,altura))

def Tipagem_Imc(peso,altura):
    if Calculo_Imc(peso,altura)<16:
        print("A partir do Imc, o seu nivel e: Magreza Grave")
    elif 16<= Calculo_Imc(peso,altura)<17:
        print("A partir do Imc, o seu nivel e: Magreza Moderada")
    elif 17<=Calculo_Imc(peso,altura)<18.5:
        print("A partir do Imc, o seu nivel e: Magreza Leve ")
    elif 18.5<=Calculo_Imc(peso,altura)<25:
        print("A partir do Imc, o seu nivel e: Saudavel")
    elif 25<=Calculo_Imc(peso,altura)<30:
        print("A partir do Imc, o seu nivel e: Sobrepeso")
    elif 30<=Calculo_Imc(peso,altura)<35:
        print("A partir do Imc, o seu nivel e: Obesidade grau 1")
    elif 35<=Calculo_Imc(peso,altura)<40:
        print("A partir do Imc, o seu nivel e: Obesidade Grau 2")
    else:
        print("A partir do Imc, o seu nivel e: Obesidade Grau 3")
print(Tipagem_Imc(peso,altura))
        

import matplotlib.pyplot as plt
import numpy as np

N = 7

cal_consumida = (2000, 3500, 3000, 3500, 270, 900,540)

numero_de_barras = np.arange(N)

comprimento = 0.35  # comprimento das barras

fig,ax = plt.subplots()

rects1 = ax.bar(numero_de_barras, cal_consumida,comprimento, color='purple')

cal_necessaria = (Calculo_Necessidade_Cal(fator), Calculo_Necessidade_Cal(fator), Calculo_Necessidade_Cal(fator),Calculo_Necessidade_Cal(fator),Calculo_Necessidade_Cal(fator),Calculo_Necessidade_Cal(fator),Calculo_Necessidade_Cal(fator))

rects2 = ax.bar(numero_de_barras + comprimento,cal_necessaria, comprimento, color='turquoise')


ax.set_xlabel('Dia da semana')
ax.set_ylabel('Quantidade')
ax.set_xticks(numero_de_barras+comprimento)
ax.set_xticklabels( ('domingo','segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado') )

ax.legend( (rects1[0], rects2[0]), ('Calorias Consumidas', 'Calorias Necessarias') )

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.show()




N = 7
proteina_consumida=(180,150,2060,903,90,87,105)
gordura_consumida=(70,30,40,45,54,19,29)
carboidrato_consumido=(130,300,209,340,189,320,2000)

numero_de_barras = np.arange(N)
comprimento = 0.35  # comprimento das barras

fig,ax = plt.subplots()

rects3=ax.bar(numero_de_barras,proteina_consumida, comprimento, color='orange')
rects4=ax.bar(numero_de_barras + comprimento, gordura_consumida,comprimento, color='blue')
rects5=ax.bar(numero_de_barras +comprimento*2, carboidrato_consumido,comprimento/2, color='navy')

ax.set_xlabel('Dia da semana')
ax.set_ylabel('Quantidade')
ax.set_xticks(numero_de_barras+comprimento)
ax.set_xticklabels( ('domingo','segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado') )

ax.legend( (rects3[0], rects4[0], rects5[0]), ('Proteinas Consumidas(g)', 'Carboidratos Consumidos(g)', 'Gorduras Consumida(g)'))


autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
plt.show()


            








