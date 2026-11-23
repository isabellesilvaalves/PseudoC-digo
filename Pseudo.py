  ALGORITMO "somar e escrever se a soma é maior, ou igual a 10"
    VAR 
        valor: real 
        soma: real 
    INÍCIO
        soma <-
    ESCREVA ("Digite um 'valor' ou 0 para parar:")
    LEIA valor
    ENQUANTO valor <> 0 FAÇA
      soma <- soma + valor 
    ESCREVA ("Soma atual: soma")
    ESCREVA ("Digite um 'valor' ou 0 para parar")
    LEIA valor 
    FIMENQUANTO
    SE soma > 10 ENTÂO 
        ESCREVA ("Soma é maior que 10")
    SENÂO 
        ESCREVA ("Soma é menor ou igual a 10")
   FIMSE
 FIMALGORITMO 
        
