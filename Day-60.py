from time import sleep
def bigger(** numbers):
    counter = bigger = 0
    print ('-=' * 20)
    print ('Analizando os valores informados...')
    for value in numbers: 
        print (f'{value}', end='', flash=True)
        sleep(0.3)
        if counter == 0:
            bigger = value
        else: 
            if value > bigger: 
                bigger = value
        counter += 1
    print (f'Foram informados {counter} valores')
    print (f'O maior valor foi {bigger}')
    print ('-=' * 20)
                
    
    
bigger (10, 22, 2 , 4, 9)
bigger (12, 22, 90, 34)
bigger (55, 98, 100, 10000)
bigger (0)
bigger ()
