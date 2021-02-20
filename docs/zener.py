V_z = 3
V_cc = 9
I = 1E-3

P_z = I * V_z
print(f"Pz = {P_z} mW")

R = (V_cc - V_z) / I

print(f"R = {R} Ohm")