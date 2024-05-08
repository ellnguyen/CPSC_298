import random

def correct_syntax():
    """ Generate correct Rho calculus syntax examples """
    processes = ['0', 'x!(P)', 'x?(y).P', 'P | Q', '*P']
    variables = ['x', 'y', 'z', 'P', 'Q', 'R']
    
    # Randomly pick process template
    process = random.choice(processes)
    
    # Replace placeholders with random variables
    for var in variables:
        if var in process:
            process = process.replace(var, random.choice(variables))
    
    return process

def incorrect_syntax():
    """ Generate incorrect Rho calculus syntax examples """
    incorrect_patterns = [
        'P..Q',       # Incorrect use of dot
        'x!( )',      # Empty send
        '|P',         # Misplaced parallel operator
        'x?(y P)',    # Missing dot
        '*( )',       # Empty replication
        'x?().P',     # Empty input variable
        'P | ',       # Trailing parallel operator without process
        'x!(P|Q).R'   # Dot after a complete expression
    ]
    
    # Return a random incorrect pattern
    return random.choice(incorrect_patterns)

def main():
    # Print examples
    print("Correct Rho Calculus Syntax Examples:")
    for _ in range(5):
        print(correct_syntax())
    
    print("\nIncorrect Rho Calculus Syntax Examples:")
    for _ in range(5):
        print(incorrect_syntax())

if __name__ == '__main__':
    main()
