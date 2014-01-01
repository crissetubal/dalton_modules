#!/usr/bin/env python


import re
import sys
import string
import math

file_name = sys.argv[1]
out_name = sys.argv[2]

f = open(file_name, 'r')
file_input = map(string.strip, f.readlines())
f.close()

# 

pattern1   = re.compile(' *@ Excited state no.*')
pattern2   = re.compile('@ +[0-9\.]+ +eV.*')
pattern3   = re.compile('@ Oscillator strength.*')

#lines = []

arquivos = []

i = 0

while i < len(file_input): 
	line = file_input[i]	
	if re.match(pattern1, line):
#		print line
		lines = []	
		lines.append(line)
		counter = 0
		i=i+1
		while i < len(file_input) and counter < 7:
			line = file_input[i]
			if re.match(pattern2, line) or re.match(pattern3, line):
#				print line
#				print counter
				lines.append(line)
				counter = counter + 1
			i=i+1
		arquivos.append(lines)
	i=i+1

numerodoarquivo = 1

#print arquivos

for arquivo in arquivos:
#	print arquivo
	f = open(out_name+str(numerodoarquivo), 'w')
	numerodoarquivo=numerodoarquivo+1
	for line in arquivo:
		f.write(line+"\n")
	f.close()

#pattern4 = re.compile('.*(/[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?/).*(/[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?/).*')

#pattern4 = re.compile('@ Oscillator strength \(LENGTH\)   : *(-{0,1}[0-9]+\.[0-9]+[E]{0,1}-{0,1}[0-9]{0,1}) *\(Transition moment : *(-{0,1}[0-9]+\.[0-9]+[E]{0,1}-{0,1}[0-9]{0,1}).*')

pattern4 = re.compile('@ Oscillator strength \(LENGTH\)   : *([0-9.E-]+) *\(Transition moment : *([0-9.E-]+).*')



lista_raizes_length = []
lista_raizes_momento = []

for arquivo in arquivos:
	length = 0
	momento = 0
	acumulador_de_length = 0
	acumulador_de_momento = 0
	for i in range(2, 5):
		#print arquivo[i]
		match = pattern4.match(arquivo[i])
		#if match:	
		#print match.group(0,1,2)	
		length = float(match.group(1))	
		#print 'length ' + str(length)
		momento = float(match.group(2))
		#print 'momento ' + str(momento)
		length = length ** 2
		momento = momento ** 2	
		
		#print 'length pwr' + str(length)
		#print 'momento pwr' + str(momento)

		acumulador_de_length = acumulador_de_length + length
		acumulador_de_momento = acumulador_de_momento + momento
	lista_raizes_length.append(math.sqrt(acumulador_de_length))
	lista_raizes_momento.append(math.sqrt(acumulador_de_momento))
	#print lista_raizes_length
	#print lista_raizes_momento


f = open('modulo.txt', 'w')
for i in range(0, len(lista_raizes_length)):
	f.write(arquivos[i][0]+"\n")	
	f.write(arquivos[i][1]+"\n")	
	f.write(arquivos[i][2]+"\n")
	f.write(arquivos[i][3]+"\n")
	f.write(arquivos[i][4]+"\n")
	f.write("|f|: "	+	str(lista_raizes_length[i])	+	"\n")
	f.write("|u|: "	+	str(lista_raizes_momento[i])	+	"\n")
f.close()
	
