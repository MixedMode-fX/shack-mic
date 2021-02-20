import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from resistors import *

st.title('Shack Mic')

V_Z = 2.2
V_CTRL = st.slider("V_CTRL", 0.0, 0.5, 0.5, 0.1)

R4 = 120000     # FROM ZENER
R6 = 1000       # CTRL
R8 = 10000


res_values = e_values(e24)

def v1a(vz, vctrl, r4, r6, r8):
    """
    voltage at input ov IC1A
    """
    return vz * r8 / (r4 + r8) + vctrl * r8 / (r6 + r8)

def non_invert_gain(vin, r_f, r_g):
    return vin * (1 + float(r_f) / r_g)

def invert_gain(vin, r_f, r_g):
    return -vin * float(f_f)/r_g

def mv(v):
    return round(v * 1000, 2)

R4 = st.selectbox(
     'R4 (bias)',
     list(res_values), res_index(R4, res_values), format_func=notation)

R6 = st.selectbox(
     'R6 (ctrl)',
     list(res_values), res_index(R6, res_values), format_func=notation)

R8 = st.selectbox(
     'R8',
     list(res_values), res_index(R8, res_values), format_func=notation)

V1A = v1a(V_Z, V_CTRL, R4, R6, R8)

st.markdown(f"""

$
V_z = {V_Z} V
$

$
V_{{ctrl}} = {V_CTRL} V
$

$
V_1 = V_z \\frac{{R_8}}{{R_4 + R_8}} + V_{{ctrl}} \\frac{{R_8}}{{R_6 + R_8}} = {mv(V1A)} mV
$

""")

R9 = 1000
R10 = 33000

R10 = st.selectbox(
     'R10 (gain)',
     list(res_values), res_index(R10, res_values), format_func=notation)

V_VACTROL = non_invert_gain(V1A, R10, R9)
V_LED = 1.65

R12 = 390
R12 = st.selectbox(
     'R12 (sense)',
     list(res_values), res_index(R12, res_values), format_func=notation)

I_VACTROL = (V_VACTROL - V_LED) / R12

st.markdown(f"""

$
V_{{vactrol}} = V_1 (1 + \\frac{{R_{{10}}}}{{R_9}}) = {mv(V_VACTROL)} mV
$

$
I_{{vactrol}} = \\frac{{V_{{vactrol}} - V_{{led}}}}{{R_{{12}}}} = {mv(I_VACTROL)} mA
$

""")

st.image(Image.open('docs/img/VTL5C4.png'), "VTL5C4 Datasheet")