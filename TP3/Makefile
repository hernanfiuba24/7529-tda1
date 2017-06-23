#Configuracion Entrega
ARCHIVOS=*.py 	#Tipos de archivos que se van a agregar
CUATRIMESTRE=2017-1C
ENTREGA=TP1
ENCODING=ISO-8859-1
OUTPUTFILE=out.ps 		 	#archivo intermedio
FORMATO=portrait 			#portrait o landscape (vertical u horizontal)
COLUMNAS=1 	  			#paginas por hoja (en columnas)
NUMEROS_LINEA=1   			#cada cuantas lineas se imprime el numero de linea

ARCHIVO_ENTREGA=$(ENTREGA)
NOMBRE_ZIP= $(ARCHIVO_ENTREGA).zip
NOMBRE_PDF= $(ARCHIVO_ENTREGA).pdf
ENCABEZADO = "[75.29] Teoría de Algoritmos I"
PIE = "$(CUATRIMESTRE) Entrega: $(ENTREGA)"
#Fin configuracion


#Seccion Entrega
pdf:
	a2ps $(ARCHIVOS) -Av --header=$(ENCABEZADO) --footer=$(PIE) --line-numbers=$(NUMEROS_LINEA) --borders=yes --columns=$(COLUMNAS)  --$(FORMATO) --output=$(OUTPUTFILE) --encoding=$(ENCODING) --tabsize=4 --major=columns --toc  | ps2pdf $(OUTPUTFILE) $(NOMBRE_PDF)
	rm -f *.ps #elimino los archivos temporales

entrega: pdf
	zip $(NOMBRE_ZIP) $(ARCHIVOS) *.pdf

clean_entrega: clean
	rm *.zip *.pdf
