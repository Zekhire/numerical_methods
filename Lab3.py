import scipy.linalg

Qa = 200    # 200   m^3/h
ca = 2      # 2     mg/m^3
Ws = 1500   # 1500  mg/h
E12 = 25    # 25    m^3/h
Qb = 300    # 300   m^3/h
cb = 2      # 2     mg/m^3
E32 = 50    # 50    m^3/h
Wg = 2500   # 2500  mg/h
Qd = 350    # 350   m^3/h
E35 = 25    # 25    m^3/h
E34 = 50    # 50    m^3/h
Qc = 250    # 150   m^3/h

A1 = [E12+Qa, -E12, 0, 0, 0]
A2 = [-(E12+Qa), E12+E32+Qa+Qb, -E32, 0, 0]
A3 = [0, E32+Qa+Qb, -(E32+E35+E34+Qa+Qb), E34, E35]
A4 = [0, 0, E34+Qc, -(E34 + Qc), 0]
A5 = [0 , 0, -(E35+Qd), 0, Qd+E35]

A = scipy.array([A1, A2, A3, A4, A5])
B = scipy.array([Ws + Qa*ca, Qb*cb, 0, 0, Wg])

P, L, U = scipy.linalg.lu(A)

#print("P:\n", P, "\n")
#print("L:\n", L, "\n")
#print("U:\n", U, "\n")

d = scipy.linalg.solve_triangular(L, B, lower=True)             # Ld = b    ->  d=L^-1*b
x = scipy.linalg.solve_triangular(U, d)                         # Ux = d    ->  x=U^-1*d
print("Wektor stężeń CO: ", x, "\n")


Ws2 = 800    # 800   mg/h
Wg2 = 1200   # 2500  mg/h
B2 = scipy.array([Ws2 + Qa*ca, Qb*cb, 0, 0, Wg2])
d = scipy.linalg.solve_triangular(L, B2, lower=True)            # Ld = b    ->  d=L^-1*b
x2 = scipy.linalg.solve_triangular(U, d)                        # Ux = d    ->  x=U^-1*d
print("Wektor stężeń CO dla zmienionych warunków: ", x2, "\n")


d = scipy.linalg.solve_triangular(L, P, lower=True)
invA = scipy.linalg.solve_triangular(U, d)
print("Owdrocona:\n", invA, "\n")



papierosy = 100*invA[3, 0]*Ws/x[3]
grill = 100*invA[3, 4]*Wg/x[3]
ulica = 100*(Qa*ca*invA[3, 0] + Qb*cb*invA[3, 1])/x[3]

print("Udział procentowy CO w pokoju dla dzieci pochodzący z:")
print("papierosów: ", papierosy)
print("grilla: ", grill)
print("ulicy: ", ulica)