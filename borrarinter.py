#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  borrarinter.py
#  
#  Copyright 2017  <sofia@garu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

f = open('borrar','r')
lista = f.readlines()
texto = ''
for each in lista:
    linea = ''
    partes=each.split("=")
    
    
    linea = linea+'self.'+partes[1].split("(")[0]
    
    linea = linea+'('+partes[0].split(".")[0]
    
    #actor + atributo
    linea = linea +'.'+partes[0].split(".")[1]+",'"+partes[0].split(".")[2]+"',"
    
    
    
    #la posicion
    
    linea = linea +partes[1].split("(")[1]+"("
    
    #el resto
    linea = linea +''.join(each.split("(")[2:])
    
    #de tipo en adelante
    #~ otralinea = linea + "=" + ''.join(each.split("=",2)[2:])
    #~ print("otra linea {}".format(otralinea))
    #partes[1].split("(")[2:])
    texto = texto +  linea.replace(",demora=1","") 
    
    
print(texto)
f.close()
