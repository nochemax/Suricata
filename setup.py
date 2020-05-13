#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LIBRERIAS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import sys
import os

# Programador David soto noche
# Correo: Sotodelanoche@gmail.com
# Lenguaje Python3 scrispt 
# Fecha 19:04:2020:
# Nombre del programa : 
# Accion: setup sericata

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PRESENTACION TERMINAL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
os.system('clear')
print("\033[1;31;1m ")
os.system('figlet -k -f usr/font/cosmike "   		Smp_A" && figlet -k -f usr/font/bulbhead " 						 		   	Setup"')
print("			  		Black_Hack")                 	
print("\033[1;37;1m ")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FUNCIONES PRINCIPALES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ SSETUP $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INSTALL DEPENDIENCIAS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class setup():
	def __init__(self):
		
		#self.repositorio='sudo add-apt-repository app:oisf/suricata-stable' no descomentar en kali 2020
		self.update='sudo apt-get update'	
		self.dependencia='apt-get install libpcre3 libpcre3-dbg libpcre3-dev build-essential libpcap-dev libnet1-dev libyaml-0-2 libyaml-dev pkg-config zlib1g zlib1g-dev libcap-ng-dev libcap-ng0 make libmagic-dev libjansson-dev libnss3-dev libgeoip-dev liblua5.1-dev libhiredis-dev libevent-dev python-yaml rustc cargo'
		self.installert='sudo apt-get install suricata jq'
		self.instalando=False
	
#metodos de la clase

	def install(self,instalando): #Accion de arrancar
		self.procedimiento=instalando
		
		if(self.procedimiento):
			#os.system(repositorio)
			os.system(self.update)
			os.system(self.ddependencia)
			os.system(self.installert)			
			return"Instalacion completada"
		else:
			return "La instalacion fallo"
	
suricata=setup() #instancia de una clase (objeto)
print(suricata.install(True))