import math # Serve per le funzioni matematiche
import random # Serve per generare numeri casuali


Dataset = [[4,20,0],[5,24,0],[18,70,1],[20,80,1]]

massimoPeso = 20
massimaAltezza = 80

thr = 0.1

random.shuffle(Dataset)


w1= random.random()
w2 = random.random()
bias = random.random()
lr = 0.05

def Sig (x): # Sigmoide (x)
    return 1/(1+math.exp(-x))

def dSig (x): # Derivata del Sigmoide(x)
    t = Sig (x)
    return t*(1-t)


def FNeurone (Peso, Altezza): # Funzione del neurone
    global w1,w2,bias
    return Peso*w1+Altezza*w2+ bias

def Output (Peso,Altezza): # Output del neurone passando per la funzione di attivazione Sigmoide che abbiamo definito (FeedForward)
    return Sig (FNeurone(Peso,Altezza))

def BackPropagation (Peso,Altezza, ValoreAtteso):
    global w1,w2,bias,lr
    Out = Output(Peso,Altezza)
    FN = FNeurone(Peso,Altezza)
    Errore = (Out - ValoreAtteso)**2
    dW1 = 2 * (Out - ValoreAtteso) * dSig(FN) * Peso
    dW2 = 2 * (Out - ValoreAtteso) * dSig(FN) * Altezza
    dBias = 2 * (Out - ValoreAtteso) * dSig(FN) * 1
    w1 = w1 - dW1 * lr
    w2 = w2 - dW2 * lr
    bias = bias - dBias * lr
    return Errore
    
    
#Addestriamo la nostra rete
for epoca in range (1500):
    
    ErroreEpoca = 0
    for elemento in Dataset:
        peso = elemento[0] / massimoPeso
        altezza = elemento[1] /massimaAltezza
        vatteso = elemento[2]
        ErroreEpoca = ErroreEpoca + BackPropagation(peso,altezza,vatteso)
    ErroreEpoca = math.sqrt(ErroreEpoca/len (Dataset))
    print (epoca, ErroreEpoca)
    
while True:
    peso = float (input ("Dammi il peso dell'animale: ")) / massimoPeso
    altezza = float (input ("Dammi l'altezza dell'animale: ")) / massimaAltezza
    
    risultato = Output (peso,altezza)
    
    if risultato < thr:
        print (f"E' un gatto ({risultato})!!!")
    elif risultato > 1-thr:
        print (f"E' un cane {risultato}!!!")
    else:
        print (f"Purtroppo non so di che animale si tratta! {risultato}")
    
    
    
    


    