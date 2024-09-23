import csv
import random

# Set columns names
columns = ['sbp', 'Tobacco', 'ldl', 'Adiposity', 'Family', 'Type', 'Obesity', 'Alcohol', 'Age', 'chd']

# Generate fictitious data 
def generate_data(num_rows):
    data = []
    for _ in range(num_rows):
        row = [
            random.randint(101, 218),  # sbp (systolic blood pressure) - presión sistólica
            round(random.uniform(0.00, 31.20), 2),  # Tobacco (kg) - Tabaco (kg acumulado)
            round(random.uniform(0.98, 15.33), 2),  # ldl (low-density lipoprotein cholesterol) - colesterol LDL
            round(random.uniform(6.64, 42.49), 2),  # Adiposity (body fat level) - Adiposidad (nivel de grasa corporal)
            random.choice(['Present', 'Absent']),  # Family history (Present or Absent) - Historial familiar (Presente o Ausente)
            random.randint(13, 78),  # Type (numeric value) - Tipo (valor numérico)
            round(random.uniform(14.70, 46.58), 2),  # Obesity - Obesidad (rango numérico)
            round(random.uniform(0.00, 147.19), 2),  # Alcohol consumption (grams per day) - Consumo de alcohol (gramos por día)
            random.randint(15, 64),  # Age (years) - Edad (años)
            random.choice([0, 1])  # chd (coronary heart disease: 0 = no, 1 = yes) - Enfermedad coronaria (0 = no, 1 = sí)
        ]
        data.append(row)
    return data

# Generate and save the CSV file (Generar y guardar el archivo CSV)
def generate_csv(filename, num_rows):
    data = generate_data(num_rows)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)

# Call the function to generate a CSV file with 20 rows (Llamar a la función para generar un archivo CSV con 20 filas)
generate_csv('heart-data.csv', 100)