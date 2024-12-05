def calculate_bmi(weight, height):
    #Calculate the BMI and return the result.
    return weight / (height ** 2)

def classify_bmi(bmi):
    #Classify BMI into categories based on predefined ranges.
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def calculate_weight_difference(bmi, height):
    """Calculate the difference between the user's weight and the normal range."""
    normal_bmi_lower = 18.5
    normal_bmi_upper = 24.9

    # Calculate weight for the normal BMI range
    weight_lower_bound = normal_bmi_lower * (height ** 2)
    weight_upper_bound = normal_bmi_upper * (height ** 2)

    return weight_lower_bound, weight_upper_bound

print("Welcome to the BMI Calculator!")
while True:
    try:
        # Get user input
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values. Please try again.")
            continue
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Classify BMI
        category = classify_bmi(bmi)
        
        # Calculate normal weight range
        weight_lower_bound, weight_upper_bound = calculate_weight_difference(bmi, height)
                    
        # Display the result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}\n")
        
         # Determine if overweight or underweight
        if bmi < 18.5:
            weight_difference = weight_lower_bound - weight
            print(f"\nYou are underweight by approximately {weight_difference:.2f} kg.")
        elif bmi > 24.9:
            weight_difference = weight - weight_upper_bound
            print(f"\nYou are overweight by approximately {weight_difference:.2f} kg.")

        # Ask the user if they want to calculate again
        again = input("Do you want to calculate another BMI? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")