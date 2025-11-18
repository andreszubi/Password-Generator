# Password Generator

A Python-based password generator that creates secure, randomized passwords based on user preferences for letters, symbols, and numbers.

## Overview

The PyPassword Generator is a command-line tool that generates random passwords by allowing users to specify the number of letters, symbols, and numbers they want in their password. The generator creates two password candidates, sorts them, and randomly selects one as the final password.

## Features

- **Customizable Password Composition**: Specify the exact number of letters, symbols, and numbers
- **Dual Password Generation**: Creates two password candidates for increased randomness
- **Organized Output**: Passwords are sorted by character type (letters → symbols → numbers) and then alphabetically
- **Random Selection**: Randomly chooses between the two generated passwords for the final output
- **Multiple Password Generation**: Option to generate additional passwords without restarting the program

## How It Works

### Process Flow

1. **User Input**: The program prompts the user to specify:
   - Number of letters (uppercase and lowercase)
   - Number of symbols
   - Number of numbers

2. **Password Generation**: 
   - Two separate passwords (`password` and `password2`) are generated simultaneously
   - Each password is built by randomly selecting characters from predefined lists:
     - **Letters**: All 26 lowercase and uppercase letters (a-z, A-Z)
     - **Symbols**: `!`, `#`, `$`, `%`, `&`, `(`, `)`, `*`, `+`
     - **Numbers**: Digits 0-9

3. **Password Sorting**:
   - Both passwords are sorted using a custom sorting key:
     - First by type: letters (priority 0), symbols (priority 1), numbers (priority 2)
     - Then alphabetically within each type
   - This ensures a consistent, organized structure

4. **Final Selection**:
   - The program randomly selects one of the two sorted passwords
   - The selected password is displayed as the final result

5. **Repeat Option**:
   - After displaying the password, the program asks if you want to generate another password
   - Enter `y` to generate a new password with new preferences, or `n` to exit

### Code Structure

- **Character Lists**: Predefined lists of letters, numbers, and symbols
- **Input Collection**: Interactive prompts to gather user preferences
- **Password Building**: For loops that append random characters to password strings
- **Sorting Algorithm**: Lambda function that sorts characters by type and alphabetical order
- **Random Selection**: Uses `random.choice()` to pick the final password from the two candidates

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. Follow the prompts:
   - Enter the number of letters you want
   - Enter the number of symbols you want
   - Enter the number of numbers you want

3. The program will display:
   - The two sorted password candidates (for debugging/testing)
   - Your final randomly selected password
   - A prompt asking if you want to generate another password

4. (Optional) Generate another password:
   - Enter `y` to start the process again with new preferences
   - Enter `n` to exit the program

## Example

```
Welcome to the PyPassword Generator, a tool to generate random passwords for your accounts.
How many letters would you like in your password?
4
How many symbols would you like in your password?
2
How many numbers would you like in your password?
2
['A', 'B', 'c', 'd', '!', '#', '1', '2']
['X', 'y', 'Z', 'a', '$', '%', '5', '7']
Your password is: ABcd!#12
Thank you for using the PyPassword Generator!
Do you want to generate another password? (y/n)
n
Thank you for using the PyPassword Generator!
```

## Requirements

- Python 3.x
- Standard library modules: `random`

## Notes

- The passwords are sorted for consistency, which may make them more predictable
- The program generates two passwords and randomly selects one to add an extra layer of randomness
- All characters are selected with equal probability from their respective character sets

