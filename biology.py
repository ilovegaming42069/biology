from collections import Counter

def get_genotypes(blood_type, rh_factor):
    if blood_type == "A":
        genotypes_abo = ["IA", "i"]
    elif blood_type == "B":
        genotypes_abo = ["IB", "i"]
    elif blood_type == "AB":
        genotypes_abo = ["IA", "IB"]
    elif blood_type == "O":
        genotypes_abo = ["i", "i"]
    else:
        raise ValueError("Invalid blood type input.")

    if rh_factor == "+":
        genotypes_rh = ["Rh+", "Rh-"]
    elif rh_factor == "-":
        genotypes_rh = ["Rh-", "Rh-"]
    else:
        raise ValueError("Invalid Rh factor input.")

    return genotypes_abo, genotypes_rh

def generate_punnett_square(genotypes1, genotypes2):
    return [g1 + g2 for g1 in genotypes1 for g2 in genotypes2]

def get_blood_type(genotype):
    if "IA" in genotype and "IB" in genotype:
        return "AB"
    elif "IA" in genotype:
        return "A"
    elif "IB" in genotype:
        return "B"
    else:
        return "O"

def get_rh_factor(genotype):
    if "Rh+" in genotype:
        return "+"
    else:
        return "-"

def calculate_probabilities(punnett_square):
    counter = Counter(punnett_square)
    total = sum(counter.values())
    probabilities = {key: (value / total) * 100 for key, value in counter.items()}
    return probabilities

def main():
    print("Enter blood type and Rh factor for Parent 1:")
    parent1_blood = input("Blood type (A, B, AB, O): ").strip().upper()
    parent1_rh = input("Rh factor (+ or -): ").strip()
    print("\nEnter blood type and Rh factor for Parent 2:")
    parent2_blood = input("Blood type (A, B, AB, O): ").strip().upper()
    parent2_rh = input("Rh factor (+ or -): ").strip()

    parent1_genotypes_abo, parent1_genotypes_rh = get_genotypes(parent1_blood, parent1_rh)
    parent2_genotypes_abo, parent2_genotypes_rh = get_genotypes(parent2_blood, parent2_rh)

    abo_combinations = generate_punnett_square(parent1_genotypes_abo, parent2_genotypes_abo)
    rh_combinations = generate_punnett_square(parent1_genotypes_rh, parent2_genotypes_rh)

    offspring_blood_types = [
        get_blood_type(abo) + get_rh_factor(rh) for abo in abo_combinations for rh in rh_combinations
    ]

    probabilities = calculate_probabilities(offspring_blood_types)

    print("\nPossible blood types of offspring and their probabilities:")
    for blood_type, probability in probabilities.items():
        print(f"{blood_type}: {probability:.2f}%")

if __name__ == "__main__":
    main()
