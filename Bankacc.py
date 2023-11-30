Compte = {}
Client = {}
ClientCompte = {}


def ajouterClient(numCl, MPC, numC, SoldeC):
    Client[numCl] = MPC
    Compte[numC] = SoldeC
    ClientCompte[numCl] = numC

def supprimerClient(numC):
    del Client[ClientCompte[numC]]
    del Compte[numC]
    del ClientCompte[numC]

def modifierMotDePasse(numCl, nvmps):
    Client[numCl] = nvmps

def deposer(numCl, montant):
    Compte[ClientCompte[numCl]] += montant

def retirer(numCl, montant):
    if Compte[ClientCompte[numCl]] >= montant:
        Compte[ClientCompte[numCl]] -= montant
    else:
        print("le solde est insuffisant!")

y = lambda numCl: int(str(numCl) + str(random.randint(0, 100)))


import csv
def ecrireFichierCSV(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for numCl, mdp in Client.items():
            writer.writerow([numCl, mdp])


