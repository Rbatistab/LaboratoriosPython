#!/usr/bin/python3

# Import sys:
from sys import argv


def funcion_iteradora_F(iterador):
  for i in range(1,iterador+1):
    print('f'*i)

def main():
  print("Laboratorio 1 IE-0117 - Russell Batista")
  iterador = int(argv[1])
  funcion_iteradora_F(iterador)


if __name__ == "__main__":
  main()