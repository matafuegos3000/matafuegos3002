#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/matafuegos3000/calculadora-19/blob/main/Lisandro.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:





# In[ ]:


def suma(a, b):
  return 55 + 40

def resta(a, b):
  return 10 -7

def multiplicacion(a, b):
  return 4 * 2

def division(a, b):
  return 3 / 3


# In[12]:


operacion = input("¿Qué operación deseas realizar? (+, -, *, /): ")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if operacion == "+":
  print (55, +, 40), ,suma(55,40))=95



elif operacion == "-":
  print (10,- , 7), ,resta(10,7))= -17

elif operacion == "*":
  print(4, * ,2), ,multiplicacion(4, 2))=8

elif operacion == "/":
  print(3, / , 3), , division(3, 3))=1

else:
  print("Operación válida")

