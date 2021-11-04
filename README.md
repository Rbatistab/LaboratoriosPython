# LaboratoriosPython

Repositorio para Laboratorios de Python para IE-0117 con el profesor Julian Gairaud Benavides (**CDM**)

## Laboratorios:

### Laboratorio Python #3:  Serie de Fibonacci

1. (60 pts) Cree una función que reciba un número n, y este pueda calcular **RECURSIVAMENTE** el enésimo número en la serie de Fibonacci.
2. (40  pts)  Cree   el   programa   “laboratorio4.py”   que   recibe   a   través   de   la   línea   de   comandos   lossiguientes argumentos:Argumento obligatorio: Un número positivo N.Argumento opcional: -t, --tiempo (ambos son equivalentes)Argumento opcional: -c, --completa (ambos son equivalentes)Si   la   opción  -t  (o  –tiempo)   es   dada,   el   programa   debe   imprimir   en   consola   el   tiempo  TOTAL  deejecución del programa (puede usar la función time() del módulo time como referencia).Si la opción  -c  (o  –completa) es dada, el programa debe calcular TODOS los números de la serieFibonacci desde el índice 0 hasta el índice N.En Figura 2 se observa la ejecución cuando no se le dan argumentos.En Figura 3 se muestra cuando sólo se da el argumento N.En Figura 4 se ve el funcionamiento cuando se usa la opción -t.En Figura 5 está el funcionamiento cuando se usa la opción -c.En Figura 6 se observa el funcionamiento cuando se usan ambas opciones (-t y -c)

Para probar este programa debe correr: 

```shell
$ chmod +x Laboratorio3_RussellBatista/laboratorio3.py  
$ ./Laboratorio3_RussellBatista/laboratorio3.py [N] [--tiempo] [--completa]
```

Ejemplos:

```sh
$ ./Laboratorio3_RussellBatista/laboratorio3.py 5 -t
Laboratorio 3 IE-0117 - Russell Batista
El numero de Fibonacci del indice 5 es: 5
Tiempo total de ejecucion: 3.24249267578125e-05s

$ ./Laboratorio3_RussellBatista/laboratorio3.py 6 -c
Laboratorio 3 IE-0117 - Russell Batista
La serie Fibonacci hasta indice 6 es:
1
1
2
3
5
8
```



### Laboratorio Python #2: Strings

**Primera Parte:** Imprimir nombres normalizados

1. (0 pts) Cree un pequeño programa que separe el nombre, segundo nombre y apellidos de una cadenade   caracteres   (string)   de   la   forma   ***“Donald   Mickey   Trump   Obama”***.   Algunas   personas   no   tienensegundo nombre, pero TODAS tienen dos apellidos. Imprima cada parte por separado.
2. (0 pt)  Modifique   el   programa   anterior   para   que   el   nombre   completo   sea   dado   por   el   usuariointeractivamente, mediante la función input()
3. (0 pt) Modifque el programa anterior para que se pueda repetir el proceso infinitamente (hasta que elusuario digite “SALIR”). 

**Segunda Parte:** Imprimir nombres normalizados

Cree   un   programa   que   pueda   recibir   nombres   completos   de   personas  (hasta   que   el   usuario   escriba ***SALIR***). El programa debe procesar los nombres y corregirlos, usando la primera letra en mayúscula, yel resto en minúscula (para cada componente del nombre), por ejemplo:

**Aspectos a evaluar:**

1. (25 pts) El usuario debe ser capaz de introducir interactivamente el nombre completo.
2. (25 pts) El programa debe detectar errores en los nombres (más de 4 componentes, o menos de 3componentes) y volver a pedirle al usuario que escriba el nombre.
3. (25 pts) El programa debe ser capaz de corregir los nombres al formato correcto.
4. (25 pts) El usuario debe ser capaz de salirse del programa interactivo digitando SALIR. Una vez queescriba   SALIR   el   programa   debe   imprimir   la   lista   completa   de   nombres   corregidos   (sólo   en   estemomento debe imprimirlos).
5. (10 pts extra)  Opcionalmente,   para   10   puntos   extra,   el   programa   debe   reconocer   números   ycaracteres especiales en el nombre e indicar error (se despliega un error similar al del punto 2.). Elprograma debe volver a pedirle el nombre al usuario. 

Para probar este programa debe correr: 

```shell
$ chmod +x Laboratorio2_RussellBatista/laboratorio2.py  
$ ./Laboratorio2_RussellBatista/laboratorio2.py
```

### Laboratorio Python #1: Piramides

* Crear un repositorio en GitHUb, llamado: "LaboratoriosPython" 

* Entregable:

  ```
  Link al repositorio de GitHub: https://github.com/Rbatistab/LaboratoriosPython
  branch: main
  sha: En la descripcion de la tarea en mediacion virutal
  ```

* Crear un script, llamado: "labo1.py"

* Reciba un valor: iterador 

* Recibe un caracter: char

* El iterador definirá la altura de una pirámide:

* Carné termina en número par: ejemplo: char -> F

iterador -> 5

```
FFFFF 
FFFF
FFF
FF
F
```

- Carné termina en impar: 

```
F 
FF
FFF
FFFF
FFFFF
```



En este caso Carnet: B008457 (Impar)

Para probar este programa debe correr: 

```shell
$ chmod +x labo1.py  
$ ./labo1.py [ITERADOR]
```

Donde [ITERADOR] es el iterador deseado, por ejemplo:

```shell
$ ./labo1.py 5
```

Imprime:

````
F
FF
FFF
FFFF
FFFFF
````