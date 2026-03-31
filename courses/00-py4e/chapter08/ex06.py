# Exercise 6: Max/min with a list

# Initialize empty list to store the numbers
num_list = []

while True:
    inp = input("Enter a number: ")
    
    # Check for "done" input
    if inp.lower() == "done":
        break
    
    # Convert input to float and add to list
    try:
        f_val = float(inp)
        num_list.append(f_val)
    except ValueError:
        print("Invalid input")
        continue

# Check if list is empty to avoid errors
if len(num_list) > 0:
    print(f"Maximum: {max(num_list)}")
    print(f"Minimum: {min(num_list)}")
else:
    print("No numbers were entered.")
