estudiantes = [
    {
        "Nombre completo": "juan perez",
        "edad": 16,
        "notas": {
            "MAT": 70,
            "FIS": 80,
            "QMC": 90,
            "LAB": 60
        },
        "asistencia": 85
    },
    {
        "Nombre completo": "carlos vargas",
        "edad": 17,
        "notas": {
            "MAT": 50,
            "FIS": 99,
            "QMC": 59,
            "LAB": 100
        },
        "asistencia": 100
    }
]


def promedio_estudiante(estudiante: dict) -> float:
    accum = sum(estudiante["notas"].values())
    return accum / len(estudiante["notas"])


def promedio_curso(lista_estudiante: list) -> float:
    list_promedio =[promedio_estudiante(est) for est in lista_estudiante]
    accum = sum(list_promedio)
    return accum / len(lista_estudiante)


print(promedio_estudiante(estudiantes[0]))
print(promedio_curso(estudiantes))
