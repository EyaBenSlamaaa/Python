from typing import Union,List

from fastapi import FastAPI

app = FastAPI()

etudiants = [
    {"id": 1,
    "nom": "Sami",
    "age": 21,
    "departement": "Informatique",},
    {"id": 2,
    "nom": "Ali",
    "age": 22,
    "departement": "Informatique",},
    {"id": 3,
    "nom": "Ahmed",
    "age": 23,
    "departement": "Informatique",},
]

@app.get("/etudiant")
def getetudiant():
    return etudiants

@app.get("/etudiant/{id}")
def getetudiant(id: int):
    for etudiant in etudiants:
        if etudiant["id"] == id:
            return etudiant
    return "etudiant not found"

@app.post("/etudiant")
def createetudiant(etudiant: dict):
    etudiants.append(etudiant)
    return etudiant

@app.put("/etudiant/{id}")
def updateetudiant(id: int, etudiant: dict):
    for i in range(len(etudiants)):
        if etudiants[i]["id"] == id:
            etudiants[i] = etudiant
            return etudiant
    return "etudiant not found"

@app.delete("/etudiant/{id}")
def deleteetudiant(id: int):
    for i in range(len(etudiants)):
        if etudiants[i]["id"] == id:
            etudiants.pop(i)
            return "etudiant deleted"
    return "etudiant not found"