#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


###################################
#CURVA DE POLARIZACIÓN CELDA PEMFC#
###################################


import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt



#CONSTANTES#
F = 96485 #C/mol
R = 8.314 #J/(mol K)
i0a = 0.2  # A/cm²
alpha_c, alpha_a = 0.5, 2.0
il_c, il_a = 0.9, 43


#TABLA DE PARÁMETROS#
C2_tabla = {50:0.0416,55:0.0393,60:0.0372,65:0.0353,70:0.0335,75:0.0318,80:0.0303}
C1_tabla = {50:1.932,55:1.916523,60:1.864,65:1.79948,70:1.742895,75:1.70385,80:1.63597}
i0c_tabla = {50:0.0000409,55:0.000069,60:0.00009361,65:0.000111235,70:0.000136,75:0.00016819,80:0.000214469}
in_tabla  = {50:0.0056,55:0.0077,60:0.009,65:0.0093,70:0.01009,75:0.01096,80:0.0119}


#CORROBORAR QUE LA TEMPERATURA ESTA EN LAS TABLAS
def Revision_en_tablas(table, T_C):
     T_C = float(T_C)
     if T_C in table:
        return float(table[T_C])
     else:
        raise ValueError(f"La temperatura {T_C} °C no esta en la tabla de temperaturas. Prueba alguno de estos valores: {list(table.keys())}")


#PRESIÓN DE SATURACIÓN AGUA
def saturacion_agua(T_C):
     A,B,C = 8.07131,1730.63,233.426
     Psat = 10**(A - B/(C+T_C))*0.00133322
     return Psat


#PRESIONES PARCIALES
def presiones_parciales(T_C):
    p_tot = 1
    p_H2O = min(saturacion_agua(T_C),0.98)
    p_H2, p_O2 = 1, 0.21
    return p_H2, p_O2, p_H2O


#CAMBIO DE GIBBS RESPECTO A LA TEMPERATURA Y VOLTAJE DE CIRCUITO ABIERTO
def Potencial_T(T_K):
    return 1.23+(T_K-298.15)*(-0.00085)

def E_cva(T_C,p_H2,p_O2,p_H2O):
    T_K = T_C + 273.15
    return Potencial_T(T_K) + (R*T_K)/(4*F)*math.log((p_H2**2)*p_O2/(p_H2O**2))


#POTENCIALES
def activacion(i,T_C,i0c,i0a,in_):
    T_K = T_C + 273.15
    termino_c = (R*T_K)/(alpha_c*F)*np.arcsinh((i+in_)/(2*i0c))
    termino_a = (R*T_K)/(alpha_a*F)*np.arcsinh((i+in_)/(2*i0a))
    return termino_c + termino_a

def ohmico(C1,C2,in_,i):
    return(C1 + C2*i)*(i+in_)
    

def concentracion(i,T_C,il_c,il_a,in_):
    T_K = T_C + 273.15
    term_c = (R*T_K)/(4*F)*np.log(1-(i+in_)/il_c)
    term_a = (R*T_K)/(2*F)*np.log(1-(i+in_)/il_a)
    return term_c + term_a


#CURVA DE POLARIZACION
def polarization_curve(T_C,i_array):
    C1  = Revision_en_tablas(C1_tabla,T_C)
    C2  = Revision_en_tablas(C2_tabla,T_C)
    i0c = Revision_en_tablas(i0c_tabla,T_C)
    in_ = Revision_en_tablas(in_tabla,T_C)
    
    
    p_H2,p_O2,p_H2O = presiones_parciales(T_C)
    E = E_cva(T_C,p_H2,p_O2,p_H2O)
    
    V=[]
    for i in i_array:
        Vc = E - activacion(i,T_C,i0c,i0a,in_) - ohmico(C1,C2,in_,i) - concentracion(i,T_C,il_c,il_a,in_)
        V.append(Vc)
    return np.array(V), dict(C1=C1,C2=C2,i0c=i0c,in_=in_,E=E)

#EDITAR
########################################################
TEMP_C = 50   # usar solo 50, 55, 60, 65, 70, 75 o 80
i_vals = np.linspace(0.0,0.25,101)
########################################################

#GENERADOR PUNTOS CURVA
V_vals,meta = polarization_curve(TEMP_C,i_vals)


#GRÁFICO
plt.plot(i_vals,V_vals)
plt.xlabel("i [A/cm²]")
plt.ylabel("V [V]")
plt.title(f"Curva V–i a {TEMP_C:.0f} °C")
plt.grid(True)
plt.show()

print("Parámetros usados a",TEMP_C,"°C:")


#TABLA BONITA CON PARÁMETROS
meta_df = pd.DataFrame(list(meta.items()), columns=["Parámetro", "Valor"])
meta_df.index = np.arange(1, len(meta_df) + 1)
display(meta_df.style.set_table_styles(
[{'selector': 'th', 'props': [('background-color', '#f2f2f2'), ('text-align', 'center'),('font-weight', 'bold')]}] ).set_properties(**{'text-align': 'center'}))








# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




