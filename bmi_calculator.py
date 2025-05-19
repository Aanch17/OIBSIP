def get_input(prompt):
    """Gets numerical input from the user with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_bmi(weight_kg, height_m):
    """Calculates BMI using weight in kg and height in m."""
    # BMI = weight (kg) / (height (m) * height (m))
    if height_m <= 0:
        return None # Avoid division by zero
    return weight_kg / (height_m ** 2)

def categorize_bmi(bmi):
    """Categorizes BMI based on standard ranges."""
    if bmi is None:
        return "Invalid input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("""
====================
  BMI Calculator
====================
""")
    
    weight_kg = get_input("Enter your weight in kilograms: ")
    height_m = get_input("Enter your height in meters: ")
    
    bmi = calculate_bmi(weight_kg, height_m)
    category = categorize_bmi(bmi)
    
    print(f"\nYour BMI is: {bmi:.2f}") # Format BMI to 2 decimal places
    print(f"Category: {category}")

if __name__ == "__main__":
    main() 