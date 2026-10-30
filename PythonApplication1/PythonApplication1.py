CursoLargo = 7
CursoMedio = 4
cursoCorto = 2.5

CursoDalto = 1.5

DifCursoRapido = 100-(CursoDalto*100)/cursoCorto
print("La diferencia es: "+str(DifCursoRapido)+"% ")

DifCursoRapido = 100-(CursoDalto*100)/CursoLargo
print("La diferencia es: "+str(round(DifCursoRapido,2))+"% ")

DifCursoRapido = 100-(CursoDalto*100)/CursoMedio
print("La diferencia es: "+str(DifCursoRapido)+"% ")

PromCrudo = 5
CrudoDalto = 3.5

DifCrudo = ((PromCrudo-CursoMedio)/PromCrudo)*100
print("Lo que se redujo fue un "+str(DifCrudo)+"%")

DifCrudo = ((CrudoDalto-CursoDalto)/CrudoDalto)*100
print("Lo que se redujo fue un "+str(round(DifCrudo,2))+"%")

DifHora = (10*CursoLargo)/CursoDalto
print("La cantidad de horas con el largo es: "+str(round(DifHora,2)))
DifHora = (10*CursoMedio)/CursoDalto
print("La cantidad de horas con el Medio es: "+str(round(DifHora,2)))
DifHora = (10*cursoCorto)/CursoDalto
print("La cantidad de horas con el Corto es: "+str(round(DifHora,2)))