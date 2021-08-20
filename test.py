import csv

nomes = ['claudio', 'jonas', 'valter']
nome_count = 0

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()

    for nome in nomes:
        nome_count += 1
        writer.writerow({'first_name': nome, 'last_name': 'santos'})
        




