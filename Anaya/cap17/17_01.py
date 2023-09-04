# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:45:41 2023

@author: shama

Capitulo 17 Clases y Objetos

"""

'''
# Objeto 1 

class Dispositivo:
    """ Clase dispositivo, para objetos conectados a la red """
    
    def __init__(self, IP):
        """ Constructor """
        self.IP = IP            # Atributo con valor definido
        self.encendido = False  # Atributo con valor por defecto
        
    def __del__(self):
        """ Destructor """
        print("Destruyendo dispositivo en", self.IP)
        
    def encender(self):
        """ Enciende el dispositivo"""
        self.encendido = True
        
    def apagar(self):
        """ Apaga el dispositivo"""
        self.encendido = False
        
    def estado(self):
        """ Muestra en pantalla el estado del dispositivo """
        mensaje = f"IP: {self.IP}\n"
        if self.encendido:
            mensaje += 'Estado: encendido'
        else:
            mensaje += 'Estado: apagado'
        return mensaje
    
  '''  
  

  
 # Objeto 2  Con metodos y atributos privados

class Dispositivo:
      """ Clase dispositivo, para objetos conectados a la red """
      
      def __init__(self, IP):
          """ Constructor """
          # Atributo con valor definido al crear el objeto
          self.IP = IP            
          # Atributo privado con valor por defecto
          self.__encendido = False  
          
      def __del__(self):
          """ Destructor """
          print("Destruyendo dispositivo en", self.IP)
          
      def encender(self):
          """ Enciende el dispositivo"""
          self.__encendido = True
          
      def apagar(self):
          """ Apaga el dispositivo"""
          self.__encendido = False
          
      def estado(self):
          """ Muestra en pantalla el estado del dispositivo """
          mensaje = f"IP: {self.IP}\n"
          if self.__encendido:
              mensaje += 'Estado: encendido'
          else:
              mensaje += 'Estado: apagado'
          return mensaje
      
      def enciende_dispositivos(lista_dispositivos):
            for d in lista_dispositivos:
                d.encender()



# Objeto 3 Televisor, atributos encapsulados

class Televisor():
    
    def __init__(self):
        self.__canal = 0            # atributo privado
        self.__num_canales = 55     # atributo privado
        
    def __ajusta_canal(self, canal):
        self.__canal = canal % self.__num_canales
        
    def siguiente_canal(self):
        self.__ajusta_canal(self.__canal + 1)
        
    def anterior_canal(self):
        self.__ajusta_canal(self.__canal - 1)
        
    def cambia_canal(self, canal):
        if canal > self.__num_canales:
            self.__canal = self.__num_canales - 1
        elif canal < 0:
            self.__canal = 0
        else:
            self.__canal = canal
            
    def canal_actual(self):
        return self.__canal
    
''' 
  

# Objeto 4 Televisor, decoradores para atributos

class Televisor():
    
    def __init__(self, modelo):
        self.__canal = 0
        self.__num_canales = 55
        self.__modelo = modelo
        
    @property
    def canal(self):
        return self.__canal
    
    @canal.setter 
    def canal(self, valor):
        self.__canal = valor
        if self.__canal == self.__num_canales:
            self.__canal = 0
        elif self.__canal == -1:
            self.canal = self.__num_canales - 1
        elif self.__canal > self.__num_canales:
            self.__canal = self.__num_canales - 1
        elif self.__canal < 0:
            self.__canal = 0
            
            
    @canal.deleter
    def canal(self):
        del self.__canal
        
        
    def __str__(self):
        """ Devuelve una descripcion del televisro """
        return f"Televisor en canal{self.__canal} de {self.__num_canales} posibles"
    
    def __ne__(self, obj):
        """ Sobre carga del operador != """
        return self.__modelo != obj.__modelo
    
    def __eq__(self, obj):
        """ Sobrecarga del operador == """
        return self.__modelo == obj.__modelo
    
    
    
# Objeto 5 Perro, atributos y metodos de clase y de objeto

class Perro():
    
    especie = "Canis lupus"
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def traer_palo(self):
        print(self.nombre, "trae el palo")
        
    def ladrar():
        print("guau!")
        
# Objeto 6 Tableta, Herencia

class Tableta(Dispositivo):
    
    def __init__(self, IP):
        super().__init__(IP)
        self.__bateria =  0
    
    def cargar(self):
        self.__bateria = 100
        
    def encender(self):
        if self.__bateria > 0:
            super().encender()
            
    def __str__(self):
        mensaje = super().estado()
        mensaje += f"\nBateria: {self.__bateria}"
        return mensaje
    
   
            
'''
    
        