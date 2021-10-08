```python
quemjoga = input("Quem começa a jogar? Computador ou Utilizador? ")
print("                      ")

def jogar():
    c = 21
    if quemjoga == "utilizador": 
       while 1 < c and c <= 21:
             a = int(input("Qual a sua jogada? "))
             if a <= 4:
                 b = 5 - a
                 c = c - a - b
                 print("Computador jogou:", b)
                 print("O número restante de fósforos é:", c)
                 print("                                    ")
             else:
                print("Só é possível retirar 1, 2, 3 ou 4 fósforos em cada jogada.")
       if c == 1 or c == 0:
                print("O computador ganhou!")
       return()    

    else:
         while 1 < c and c <= 21:
               b2 = 1
               print("O computador jogou:", b2)
               j = 5 - b2
               a2 = int(input("Qual a sua jogada? "))
               while 1 < c and c <= 21:
                  if j != a2:
                     b3 = 5 - b2 - a2
                     c = c - a2 - b2
                     print("                                        ")
                     print("O computador jogou:", b3)
                     a2 = int(input("Qual a sua jogada? "))
                     print("O número restante de fósforos é:", c)
                     print("                                        ")
                  else:
                     c = c - a2 - b2
                     print("O computador jogou:", b2)
                     a2 = int(input("Qual a sua jogada? "))
                     print("O número restante de fósforos é:", c)
                     print("                                        ")
               if c == 1 or c == 0:
                    print("Parabéns! Ganhaste!")
               return()
         return ()
                 
print(jogar())
```

    Quem começa a jogar? Computador ou Utilizador? utilizador
                          
    Qual o valor a inserir? 4
    Computador jogou: 1
    O número restante de fósforos é: 16
                                        
    Qual o valor a inserir? 4
    Computador jogou: 1
    O número restante de fósforos é: 11
                                        
    Qual o valor a inserir? 3
    Computador jogou: 2
    O número restante de fósforos é: 6
                                        
    Qual o valor a inserir? 2
    Computador jogou: 3
    O número restante de fósforos é: 1
                                        
    O computador ganhou!
    ()
    


```python

```
