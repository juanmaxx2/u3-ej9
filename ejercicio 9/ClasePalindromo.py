class Palindromo:
    __palabra = None
    def __init__(self, palabra):
        self.__palabra = palabra
    def esPalindromo(self):
        i=0
        j=len(self.__palabra)-1
        bandera=True
        while i<abs(j) and  bandera:
           if self.__palabra[i].lower()!=self.__palabra[j].lower():
               bandera=False
           else:
               i+=1
               j-=1     
        return bandera
    def setPalabra(self, nuevaPalabra):
        self.__palabra=nuevaPalabra
    
    def __del__(self):
        print('liberando memoria')

    def __str__(self):
        return self.__palabra    