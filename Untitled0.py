#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/matafuegos3000/calculadora-19/blob/main/Untitled0.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[4]:


def suma(a, b):
  return 55 + 40

def resta(a, b):
  return 10 - 7

def multiplicacion(a, b):
  return 33 * 9

def division(a, b):
  return 8 / 2


# In[5]:


operacion = input("¿Qué operación deseas realizar? (+, -, *, /): ")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if operacion == "+":
  print(55, "+", 40, "=", suma(55,+40))

elif operacion == "-":
  print(10,"-" , 7, "=", resta(10,7))

elif operacion == "*":
  print(33, "*", 9, "=", multiplicacion(88,9))

elif operacion == "/":
  print(8, "/", 2, "=", division(8,2))

else:
  print("Operación no válida")

