#!/usr/bin/python3
import csv

with open('meuarquivo.xls',newline='') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=' ')
    for a in arquivo:
        print(a)

