# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
from pilasengine.habilidades import Habilidad

TOLERANCIA = 10

class ArrastrableFicha(Habilidad):

    def iniciar(self, receptor):
        super(ArrastrableFicha, self).iniciar(receptor)
        self.pilas.eventos.click_de_mouse.conectar(self.cuando_hace_click)
        self.estado = "reposo"

    def cuando_hace_click(self, evento):
        actores_debajo_de_mouse = self.pilas.escena_actual().obtener_actores_en(evento.x, evento.y)
        if actores_debajo_de_mouse:
            actor_debajo_del_mouse = actores_debajo_de_mouse[-1]
            if actor_debajo_del_mouse is self.receptor:
                self.intentar_arrastrar()

    def intentar_arrastrar(self):
        self.pilas.eventos.termina_click.conectar(self.termina_de_arrastrar, id="termina_de_arrastrar")
        self.pilas.eventos.mueve_mouse.conectar(self.arrastrando, id="arrastrando")
        self.partida_x = self.receptor.x
        self.partida_y = self.receptor.y

    def arrastrando(self, evento):
        if self.estado == "mover_horizontal":
            self.receptor.x = evento.x
            if abs(evento.x - self.partida_x) < TOLERANCIA:
                self.estado = "iniciando_arrastre"
        elif self.estado == "mover_vertical":
            self.receptor.y = evento.y
            if abs(evento.y - self.partida_y) < TOLERANCIA:
                self.estado = "iniciando_arrastre"
        else:
            if self.estado == "iniciando_arrastre":
                if abs(evento.x - self.partida_x) > TOLERANCIA:
                    self.estado = "mover_horizontal"
                    self.receptor.x = self.partida_x
                    self.receptor.y = self.partida_y
                elif abs(evento.y - self.partida_y) > TOLERANCIA:
                    self.estado = "mover_vertical"
                    self.receptor.x = self.partida_x
                    self.receptor.y = self.partida_y
                else:
                    self.receptor.x = evento.x
                    self.receptor.y = evento.y
            elif self.estado == "reposo":
                self.estado = "iniciando_arrastre"

    def termina_de_arrastrar(self, evento):
        self.pilas.eventos.mueve_mouse.desconectar_por_id("arrastrando")
        self.pilas.eventos.termina_click.desconectar_por_id("termina_de_arrastrar")
        self.estado = "reposo"
        self.receptor.x = [self.partida_x]
        self.receptor.y = [self.partida_y]
