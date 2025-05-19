# Random Password Generator

A simple command-line password generator written in Python. This project was created as part of my Python Programming internship at Oasis Infobyte.

## Features
- User chooses password length
- User selects which character sets to include (letters, numbers, symbols)
- Input validation for length and character set selection
- Random password generation
- Ensures at least one character from each selected set

## How to Use
1. Run the script:
   ```bash
   python "Random Password Generator.py"
   ```
2. Enter your desired password length (minimum 4).
3. Choose which character sets to include by answering the prompts (y/n).
4. The generated password will be displayed on the screen.

## Example
```
==============================
  Random Password Generator
==============================
Enter desired password length (minimum 4): 10
Include letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n

Your generated password is: 8k2Jv1QwZp
Keep it safe and do not share it with others!
```

## What I Learned
- How to use Python's built-in `random` and `string` modules
- Validating user input and handling errors
- Building a user-friendly command-line interface
- Ensuring password security by including at least one character from each selected set
- Writing clean, commented, and readable code

## License
This project is for educational purposes as part of my internship at Oasis Infobyte.

## Requirements
- Python 3.x

## Installation
1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone or download this repository.
3. Navigate to the project directory in your terminal or command prompt.
4. Run the script using Python:
   ```bash
   python "Random Password Generator.py"
   ```

## Future Enhancements
- Add password strength checking.
- Implement an option to save generated passwords (with appropriate security warnings).
- Add a graphical user interface (GUI) for a more user-friendly experience. 
