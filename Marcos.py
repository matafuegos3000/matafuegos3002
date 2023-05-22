#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/matafuegos3000/calculadora-19/blob/main/Marcos.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[10]:


def division(a, b):
  if b != 0:
    return a / b
  else:
    return "No se puede dividir entre cero"


# In[11]:


def suma(a, b):
  return a + b

def resta(a, b):
  return a - b

def multiplicacion(a, b):
  return a * b

def division(a, b):
  if b != 0:
    return a / b
  else:
    return "No se puede dividir entre cero"

operacion = input("¿Qué operación deseas realizar? (+, -, *, /): ")

if operacion in ['+', '-', '*', '/']:
  num1 = float(input("Introduce el primer número: "))
  num2 = float(input("Introduce el segundo número: "))

  if operacion == "+":
    resultado = suma(num1, num2)
    print(num1, "+", num2, "=", resultado)

  elif operacion == "-":
    resultado = resta(num1, num2)
    print(num1, "-", num2, "=", resultado)

  elif operacion == "*":
    resultado = multiplicacion(num1, num2)
    print(num1, "*", num2, "=", resultado)

  elif operacion == "/":
    resultado = division(num1, num2)
    if resultado == "No se puede dividir entre cero":
      print(resultado)
    else:
      print(num1, "/", num2, "=", resultado)
else:
  print("Operación no válida")


