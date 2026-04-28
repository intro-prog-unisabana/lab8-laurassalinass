"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""
import sys
try:
    total_load=sys.argv[1]
    num_supports=sys.argv[2]
    calculo= total_load / num_supports
    print(f"Load per support point: {calculo:2f} N")
except ZeroDivisionError: 
    print("Error: Cannot divide by zero! Supports must be greater than zero.")
except (ValueError, IndexError): 
    print("Error: Invalid input! Enter numeric values only.")
