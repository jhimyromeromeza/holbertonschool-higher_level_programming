#!/usr/bin/python3
import sys

if __name__ == "__main__":
    suma = 0
    num = len(sys.argv)- 1
    for i in range(1, num + 1):
        suma = suma + int(sys.argv[i])
    print("{}".format(suma)) 
