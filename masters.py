def generate_numeric_recursion_tree(n):
    output = []
    
    
    output.append(f"Recursion Tree Analysis for T(n) = 2T(n/2) + n^2")
    output.append(f"Testing with n = {n}\n")
    output.append("-" * 105)
    
    header = f"{'Level':<10} | {'Subproblems':<15} | {'Subproblem Size':<20} | {'Cost per Subproblem':<25} | {'Total Cost at Level'}"
    output.append(header)
    output.append("-" * 105)
    
    
    level = 0
    subproblem_size = n
    total_work = 0
    
    while subproblem_size >= 1:
        num_subproblems = 2 ** level
        cost_per_subproblem = subproblem_size ** 2
        total_cost_level = num_subproblems * cost_per_subproblem
        
        total_work += total_cost_level
        
       
        row = f"{level:<10} | {num_subproblems:<15} | {subproblem_size:<20} | {cost_per_subproblem:<25} | {total_cost_level}"
        output.append(row)
        
        subproblem_size = subproblem_size // 2
        level += 1
        
   
    output.append("-" * 105)
    output.append(f"\nCalculated Total Work T({n}) = {total_work}")
    
    return "\n".join(output)

if __name__ == "__main__":
    try:
        
        n = int(input("Enter n (e.g., 16 or 32): "))
        
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            
            result_text = generate_numeric_recursion_tree(n)
            
            
            print("\n" + result_text)
            
           
            filename = "recursion_tree_output.txt"
            with open(filename, "w") as file:
                file.write(result_text)
                
            print(f"\n[Success] Results have been cleanly saved to '{filename}'.")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer for n.")