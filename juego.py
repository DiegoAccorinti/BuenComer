#!/usr/bin/env python
# -*- coding: utf-8
# por Diego Accorinti - 2017 - para Huayra gnu/linux - licencia GPL 3.0
# Emoji artwork provided by EmojiOne · http://emojione.com


import pilasengine, os, random
from arrastrableFicha import ArrastrableFicha
from OpenGL import GL

pilas = pilasengine.iniciar(ancho=900, alto=550, titulo='BuenComer')

#Habilitando el Audio
try:
  pilas.forzar_habilitacion_de_audio()
except AttributeError:
  print u"Omitiendo Habilitación forzada de audio, version anterior a 1.4.8".encode('utf-8')

#cargo los sonidos
sonido_coincidencia = pilas.sonidos.cargar('snd/sfx_sounds_fanfare2.wav')

ruta = os.path.dirname(os.path.realpath(__file__))
url_fuente = ruta + '/DancingScript-Regular.otf'
url_fuente_puntos = ruta + '/acknowtt.ttf'

#vinculo la habilidad nueva
pilas.habilidades.vincular(ArrastrableFicha)

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self):

        # Boton vitamina A --------------------------------------------------------------
        vitaA = pilas.actores.Boton(ruta_normal = ruta + "/img/popA.png", x=-369, y=230)
        popA_over = pilas.actores.Actor(y=90)
        popA_over.z = -9999
        popA_over.transparencia = 100
        popA_over.x = -300
        popA_over.y = 0
        url = ruta + '/img/popA_over.png'
        popA_over.imagen = pilas.imagenes.cargar(url)
        def cuando_pasa_sobre_vitaA(): popA_over.transparencia = [0],0.2
        def cuando_no_pasa_vitaA(): popA_over.transparencia = [100],0.2
        vitaA.conectar_sobre(cuando_pasa_sobre_vitaA)
        vitaA.conectar_normal(cuando_no_pasa_vitaA)

        # Boton vitamina B --------------------------------------------------------------
        vitaB = pilas.actores.Boton(ruta_normal = ruta + "/img/popB.png", x=-216, y=232)
        popB_over = pilas.actores.Actor(y=90)
        popB_over.z = -9999
        popB_over.transparencia = 100
        popB_over.x = -300
        popB_over.y = 20
        url = ruta + '/img/popB_over.png'
        popB_over.imagen = pilas.imagenes.cargar(url)
        def cuando_pasa_sobre_vitaB(): popB_over.transparencia = [0],0.2
        def cuando_no_pasa_vitaB(): popB_over.transparencia = [100],0.2
        vitaB.conectar_sobre(cuando_pasa_sobre_vitaB)
        vitaB.conectar_normal(cuando_no_pasa_vitaB)

        # Boton vitamina C --------------------------------------------------------------
        vitaC = pilas.actores.Boton(ruta_normal = ruta + "/img/popC.png", x=-66, y=232)
        popC_over = pilas.actores.Actor(y=90)
        popC_over.z = -9999
        popC_over.transparencia = 100
        popC_over.x = -300
        popC_over.y = 20

        url = ruta + '/img/popC_over.png'
        popC_over.imagen = pilas.imagenes.cargar(url)
        def cuando_pasa_sobre_vitaC(): popC_over.transparencia = [0],0.2
        def cuando_no_pasa_vitaC(): popC_over.transparencia = [100],0.2
        vitaC.conectar_sobre(cuando_pasa_sobre_vitaC)
        vitaC.conectar_normal(cuando_no_pasa_vitaC)

        # Boton vitamina D --------------------------------------------------------------
        vitaD = pilas.actores.Boton(ruta_normal = ruta + "/img/popD.png", x=78, y=232)
        popD_over = pilas.actores.Actor(y=90)
        popD_over.z = -9999
        popD_over.transparencia = 100
        popD_over.x = -300
        popD_over.y = -10

        url = ruta + '/img/popD_over.png'
        popD_over.imagen = pilas.imagenes.cargar(url)
        def cuando_pasa_sobre_vitaD(): popD_over.transparencia = [0],0.2
        def cuando_no_pasa_vitaD(): popD_over.transparencia = [100],0.2
        vitaD.conectar_sobre(cuando_pasa_sobre_vitaD)
        vitaD.conectar_normal(cuando_no_pasa_vitaD)

        # Boton vitamina E --------------------------------------------------------------
        vitaE = pilas.actores.Boton(ruta_normal = ruta + "/img/popE.png", x=226, y=232)
        popE_over = pilas.actores.Actor(y=110)
        popE_over.z = -9999
        popE_over.transparencia = 100
        popE_over.x = -300
        popE_over.y = 20

        url = ruta + '/img/popE_over.png'
        popE_over.imagen = pilas.imagenes.cargar(url)
        def cuando_pasa_sobre_vitaE(): popE_over.transparencia = [0],0.2
        def cuando_no_pasa_vitaE(): popE_over.transparencia = [100],0.2
        vitaE.conectar_sobre(cuando_pasa_sobre_vitaE)
        vitaE.conectar_normal(cuando_no_pasa_vitaE)

        # Boton vitamina K --------------------------------------------------------------
        vitaK = pilas.actores.Boton(ruta_normal = ruta + "/img/popK.png", x=374, y=232)
        popK_over = pilas.actores.Actor(y=110)
        popK_over.z = -9999
        popK_over.transparencia = 100
        popK_over.x = -300
        popK_over.y = 20
        url = ruta + '/img/popK_over.png'
        popK_over.imagen = pilas.imagenes.cargar(url)
        def cuando_pasa_sobre_vitaK(): popK_over.transparencia = [0],0.2
        def cuando_no_pasa_vitaK(): popK_over.transparencia = [100],0.2
        vitaK.conectar_sobre(cuando_pasa_sobre_vitaK)
        vitaK.conectar_normal(cuando_no_pasa_vitaK)
        #--------------------------------------------------------------------------------

        fondo = pilas.fondos.Color(pilas.colores.negro)
        fondo = pilas.fondos.Fondo()
        url = ruta + '/img/interfaz.png'
        fondo.imagen = pilas.imagenes.cargar(url)
        fondo.z = 0
        
        
        # armo el tablero
        casilleros = pilas.actores.Grupo()
        alimentos = pilas.actores.Grupo()
        tablero = []
        contador = 1
        for y in range(-1,4):
            for x in range(-1,6):

                casillero = self.Casillero(pilas);
                casilleros.agregar(casillero)
                if (len(casilleros)%2 == 0):
                    url = ruta + '/img/casillaA.png'
                else:
                    url = ruta + '/img/casillaB.png'
                casillero.imagen = pilas.imagenes.cargar(url)
                casillero.x = x * 73
                casillero.y = y * -73

                #generar el alimento que irá en ese casillero
                alimento = self.Alimento(pilas);
                alimentos.agregar(alimento)

                tablero.append(alimento)

                alimento.aprender(pilas.habilidades.ArrastrableFicha)
                alimento.radio_de_colision = 30

                alimento.id = contador -1 # Casillero en el que está inicialmente
                alimento.x = casillero.x
                alimento.y = casillero.y + 20
                alimento.posicionx = alimento.x
                alimento.posiciony = alimento.y
                contador += 1

        for casillero in casilleros:
            casillero.x += 0 # Acomodo todo el tablero +50 px a la derecha
            casillero.y += 20
            casillero.z = 0

        # Puntajes Vitaminas

        global sprite_vit_A, sprite_vit_B, sprite_vit_C, sprite_vit_D, sprite_vit_E, sprite_vit_K
        sprite_vit_A = pilas.actores.Texto("0", magnitud=22, fuente= url_fuente_puntos, y= 223, x= -370, ancho = 0)
        sprite_vit_B = pilas.actores.Texto("0", magnitud=22, fuente= url_fuente_puntos, y= 223, x= -215, ancho = 0)
        sprite_vit_C = pilas.actores.Texto("0", magnitud=22, fuente= url_fuente_puntos, y= 223, x= -65, ancho = 0)
        sprite_vit_D = pilas.actores.Texto("0", magnitud=22, fuente= url_fuente_puntos, y= 223, x= 85, ancho = 0)
        sprite_vit_E = pilas.actores.Texto("0", magnitud=22, fuente= url_fuente_puntos, y= 223, x= 235, ancho = 0)
        sprite_vit_K = pilas.actores.Texto("0", magnitud=22, fuente= url_fuente_puntos, y= 223, x= 385, ancho = 0)

        def combinoAlimentos(alimento1, alimento2):
			
            global sprite_vit_A
            
            def eliminoOtros(aBorrar):
                for x in aBorrar:
                    tablero[x].hacer("Desaparecer")
                
                if len(aBorrar) > 2:    
	                combo = self.Combo(pilas)
	                combo.escala = 0.1
	                combo.escala = [1],0.5
	                combo.rotacion = [360]
	                combo.transparencia = [0,30,100],0.3
	                combo.hacer("Desaparecer")

            # guardo las posiciones iniciales de cada alimento
            if alimento1.tipo == alimento2.tipo:

                sonido_coincidencia.reproducir()
                
                for q in range(0,alimento1.vitaminas[0]): #creo bolas de energía que iran hasta la vitamina A
                    energia = self.Energia(pilas, x= alimento1.x, y=alimento2.y)
                    energia.x = [alimento1.x + random.randint(-100,100), -320],0.7
                    energia.y = [alimento1.y + random.randint(-100,100), 240],0.7
                    sprite_vit_A.texto = str(int(sprite_vit_A.texto) +1) 
                                        
                for q in range(0,alimento1.vitaminas[1]): #creo bolas de energía que iran hasta la vitamina B
                    energia = self.Energia(pilas, x= alimento1.x, y=alimento2.y)
                    energia.x = [alimento1.x + random.randint(-100,100), -165],0.8
                    energia.y = [alimento1.y + random.randint(-100,100), 240],0.8     
                    sprite_vit_B.texto = str(int(sprite_vit_B.texto) +1) 
                           
                for q in range(0,alimento1.vitaminas[2]): #creo bolas de energía que iran hasta la vitamina c
                    energia = self.Energia(pilas, x= alimento1.x, y=alimento2.y)
                    energia.x = [alimento1.x + random.randint(-100,100), -15],0.9
                    energia.y = [alimento1.y + random.randint(-100,100), 240],0.9
                    sprite_vit_C.texto = str(int(sprite_vit_C.texto) +1) 
                                                              
                for q in range(0,alimento1.vitaminas[3]): #creo bolas de energía que iran hasta la vitamina D
                    energia = self.Energia(pilas, x= alimento1.x, y=alimento2.y)
                    energia.x = [alimento1.x + random.randint(-100,100), 125],1
                    energia.y = [alimento1.y + random.randint(-100,100), 240],1
                    sprite_vit_D.texto = str(int(sprite_vit_D.texto) +1)
                                 
                for q in range(0,alimento1.vitaminas[4]): #creo bolas de energía que iran hasta la vitamina E
                    energia = self.Energia(pilas, x= alimento1.x, y=alimento2.y)
                    energia.x = [alimento1.x + random.randint(-100,100), 275],1.1
                    energia.y = [alimento1.y + random.randint(-100,100), 240],1.1
                    sprite_vit_E.texto = str(int(sprite_vit_E.texto) +1)
                    
                for q in range(0,alimento1.vitaminas[5]): #creo bolas de energía que iran hasta la vitamina K
                    energia = self.Energia(pilas, x= alimento1.x, y=alimento2.y)
                    energia.x = [alimento1.x + random.randint(-100,100), 425],1.2
                    energia.y = [alimento1.y + random.randint(-100,100), 240],1.2
                    sprite_vit_K.texto = str(int(sprite_vit_K.texto) +1)
                             

                #armo un array con los alimentos a borrar
#print alimento1.id
                print alimentos[alimento1.id].id -1

                aBorrar=[]
                aBorrar.extend([alimento1.id, alimento2.id])
                                
                eliminoOtros(aBorrar)
                


        for x in range(0,34):
            pilas.colisiones.agregar(alimentos[x],alimentos[x+1], combinoAlimentos)
            if x <= 27:
                 pilas.colisiones.agregar(alimentos[x],alimentos[x+7], combinoAlimentos)




    class Casillero(pilasengine.actores.Actor):

        def iniciar(self):
            self.x = 0
            self.y = 0

        def actualizar(self):
            # aleatoriamente creo un movimiento, meramente estético.
            self.rnd = random.randint(1, 1000)
            if self.rnd == 14:
                self.escala = [1.1,1],0.2


    class Alimento(pilasengine.actores.Actor):
        def iniciar(self):
            self.id = 0
            self.posicion = 0
            self.casillero = 0
            self.posicion = 0
            self.tipo = random.choice(["sandia", "leche", "pancho", "palta", "ensalada"])
            if self.tipo == "sandia":
                url = ruta + "/img/sandia.png";
                self.imagen = url
                #      VITAMINAS  A  B C D E K
                self.vitaminas = [3,10,6,0,0,0]

            if self.tipo == "leche":
                url = ruta + "/img/leche.png";
                self.imagen = url
                self.vitaminas = [10,6,4,1,5,0]

            if self.tipo == "pancho":
                url = ruta + "/img/pancho.png";
                self.imagen = url
                self.vitaminas = [0,1,0,0,0,0]
                        
            if self.tipo == "palta":
                url = ruta + "/img/palta.png";
                self.imagen = url
                self.vitaminas = [4,4,4,4,12,3]
                
            if self.tipo == "ensalada":
                url = ruta + "/img/ensalada.png";
                self.imagen = url
                self.vitaminas = [7,8,7,7,6,6]

            self.z = -1

    class Combo(pilasengine.actores.Actor):
        def iniciar(self):
            url = ruta + "/img/" + random.choice(["excelente", "genial", "sorprendente"]) + ".png";
            self.imagen = url

    class Energia(pilasengine.actores.Actor):
        def iniciar(self,x , y):
            url = ruta + "/img/energia.png";
            self.imagen = url
            self.x = x
            self.y = y
            self.escala = random.randint(1,2)


        def actualizar(self):
            self.rotacion += 25
            if self.y == 240:
                if self.escala < 2:
                    self.escala += 0.3
                else:
					self.eliminar()

# Escena Menu
def cargar_escena_juego():
	pilas.escenas.PantallaJuego()

def salir_del_juego():
	pilas.terminar()

class Desaparecer(pilasengine.comportamientos.Comportamiento):

    def iniciar(self, receptor):
        self.receptor = receptor

    def actualizar(self):
        if self.receptor.escala < 10:
            self.receptor.escala += 0.2
            self.receptor.transparencia += 10
        else:
            self.receptor.eliminar()
            return True

class PantallaMenu(pilasengine.escenas.Escena):

 
	def iniciar(self):

		url = ruta + '/img/menu_fondo.png'
		self.pilas.fondos.FondoMozaico(url)
		self._crear_el_titulo_del_juego()

		menu = pilas.actores.Menu([
					('JUGAR', cargar_escena_juego),
					('SALIR', salir_del_juego),
				], fuente = url_fuente, y = 110)
		menu.escala = 1
		menu.x = [320],1
		menu.transparencia = 100
		menu.transparencia = [0],3
		
		
		pilas.fisica.eliminar_suelo()
		comida_intro = PantallaJuego.Alimento(pilas) * 30
		comida_intro.aprender(pilas.habilidades.RebotarComoPelota)
		comida_intro.x = 300
		comida_intro.empujar(10,15)

	def _crear_el_titulo_del_juego(self):

		titulo = self.pilas.actores.Actor()
		url = ruta + '/img/titulo_A.png'
		titulo.imagen = url
		titulo.y = 300
		titulo.rotacion = 30
		titulo.y = [0], 0.7
		titulo.rotacion = [0], 0.7
		titulo.z = -100


pilas.comportamientos.vincular(Desaparecer)

pilas.escenas.vincular(PantallaJuego)
pilas.escenas.vincular(PantallaMenu)
pilas.escenas.PantallaMenu()
#pilas.escenas.PantallaJuego()

pilas.ejecutar()


