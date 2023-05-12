import csv
from Bio import Entrez

# Set email to identify yourself to NCBI
your_email = input("To access NCBI, please enter your email address: ")
Entrez.email = your_email

# Get user input of the CSV file name
csv_file_name = input("Please enter the CSV file name: ")

# Read positions and data from the CSV file
positions = []
data = []
with open(csv_file_name, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        positions.append((row["Chr"], int(row["Pos"])))
        data.append(row)

# Mus musculus whole genome assembly accession number
assembly_accession = "GCF_000001635.27"

# Loop through the positions and find SNP accessions
for i, (chr, position) in enumerate(positions):
    query = f"{assembly_accession}[Assembly] AND {chr}[Chromosome] AND {position}[Base Position] AND Mus musculus[Organism]"
    handle = Entrez.esearch(db="snp", term=query)
    record = Entrez.read(handle)
    handle.close()

    # Append the SNP accession numbers
    rs_accessions = ["rs" + accession for accession in record["IdList"]] if record["IdList"] else ["unknown"]

    # Print the position and SNP accessions to the screen
    print(f"Chromosome {chr}, Position {position}: {', '.join(rs_accessions)}")

    # Add SNP Accession to data
    data[i]["SNP Accession"] = ", ".join(rs_accessions)

# Save the updated data to a new CSV file
with open("updated_snp_accession_output.csv", "w", newline="") as csvfile:
    fieldnames = list(data[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in data:
        writer.writerow(row)

print("SNP Accessions added to 'updated_snp_accession_output.csv'")

