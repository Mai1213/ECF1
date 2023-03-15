import re

fichier = "liste_email.txt"

def extraire_emails_francais(fichier):
    emails_francais = []
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(?:[a-zA-Z]{2,}|\d{1,3})"

    with open(fichier, 'r', encoding='utf-8') as file:
        contenu = file.read()
        emails = re.findall(pattern, contenu)

        for email in emails:
            if email.endswith('.fr'):
                emails_francais.append(email)

    return emails_francais


emails_francais = extraire_emails_francais(fichier)
print("Liste des emails français:")
print(emails_francais)

# Ouvrez un nouveau fichier en mode écriture
with open('output.txt', 'w') as fichier:
    # Parcourez les éléments de la liste
    for element in emails_francais:
        # Écrivez chaque élément dans le fichier, suivi d'un retour à la ligne
        fichier.write(element + '\n')

print("Un fichier output avec la liste des emails finissant par fr a été créé")