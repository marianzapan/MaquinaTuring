from mt import *

#Inversión de bits (igual que en tabla)
funcionTransicion = {("q0"," "):(" ", "L", "q1"),
                     ("q0","0"):("0", "R", "q0"),
                     ("q0","1"):("1", "R", "q0"),
                     ("q1"," "):("1", "R", "q2"),
                     ("q1","0"):("1", "L", "q2"),
                     ("q1","1"):("0", "L", "q1"),
                     ("q2"," "):(" ", "L", "qf"),
                     ("q2","0"):("0", "R", "q2"),
                     ("q2","1"):("1", "R", "q2")}
qfinales = {"qf"}

mt = MT("101 ", q0="q0", qfinales=qfinales, funcionTransicion=funcionTransicion)

print("Input en Cinta: \n" + mt.getCinta())

while not mt.final(): 
    mt.step()

print("Resultado de la ejecución de la MT:")
print(mt.getCinta())