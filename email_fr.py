import re

fichier = "C:\DATA_ANALYST\ECF1\liste_email.txt"


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

