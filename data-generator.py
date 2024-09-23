import csv
import random

# Set columns names
columns = ['sbp', 'Tobacco', 'ldl', 'Adiposity', 'Family', 'Type', 'Obesity', 'Alcohol', 'Age', 'chd']

# Generate fictitious data 
def generate_data(num_rows):
    data = []
    for _ in range(num_rows):
        row = [
            random.randint(100, 180),  # sbp (systolic blood pressure) - presión sistólica
            random.choice([0, 1]),     # Tobacco (0 = no, 1 = yes) - Tabaco (0 = no, 1 = sí)
            round(random.uniform(1.0, 6.0), 2),  # ldl (low-density lipoprotein cholesterol) - colesterol LDL
            round(random.uniform(15.0, 45.0), 2),  # Adiposity (body fat level) - Adiposidad (nivel de grasa corporal)
            random.choice(['Absent', 'Present']),  # Family history (Absent or Present) - Historial familiar (Ausente o Presente)
            random.randint(13, 78),   # Type (blood type or similar) - Tipo (grupo sanguíneo o similar)
            round(random.uniform(14.70, 46.58), 2),  # Obesity (Absent or Present) - Obesidad (Ausente o Presente)
            round(random.uniform(0, 50), 2),  # Alcohol consumption (grams per day) - Consumo de alcohol (gramos por día)
            random.randint(20, 80),  # Age (years) - Edad (años)
            random.choice([0, 1])   # chd (coronary heart disease: 0 = no, 1 = yes) - Enfermedad coronaria (0 = no, 1 = sí)
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