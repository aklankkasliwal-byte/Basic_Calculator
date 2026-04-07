1. Project Overview
This project is a Python-based Basic Calculator that performs fundamental arithmetic operations such as addition, subtraction, multiplication, and division. The program takes input values from the user and allows them to choose an operation to perform. Based on the selected operation, the calculator processes the input and displays the result. This project demonstrates the use of conditional statements, functions, and user input handling in Python.
________________________________________
2. Problem Statement
In daily life, calculations are required in various applications such as education, business, and engineering. Manual calculations can be time-consuming and prone to errors. Therefore, this project aims to develop a simple and efficient calculator using Python that can perform basic arithmetic operations accurately and quickly.
________________________________________
3. Technology Stack
● Programming Language: Python 
● IDE: Python IDLE / VS Code
________________________________________
4. Implementation
•	Library Import:-
The program begins by importing the tkinter library to design the graphical user interface, along with ttk and math modules for extended functionality.
•	Class Creation:-
A class named Calculator is created to encapsulate all functionalities such as GUI design, input handling, and calculation logic in an organized manner.
•	Initialization :-
Inside the constructor, the main window is initialized with a title, fixed size, and background color.
Variables like current, previous, operation, and should_reset are initialized to manage user input and operations.
•	User Interface Design:-
The setup_ui() method constructs the interface, including a title label, a display frame, and buttons.
•	Two display sections are used:
One for showing the expression (previous calculation)
One for showing the current number or result
Buttons are arranged in a grid layout for proper alignment.
•	Button Control Mechanism :-
Each button is connected to a common method button_click() which determines the type of input and calls the appropriate function.
•	Number Input Handling :-
The input_number() method manages digit and decimal inputs, ensuring proper number formation and preventing multiple decimal points.
•	Operator Handling :-
The input_operation() method stores the selected operator and prepares the calculator for the next input while converting symbols into Python-compatible operators.
Expression Display Update
The update_expression() method updates the top display to show the ongoing mathematical expression clearly to the user.
•	Calculation Process :-
The calculate() method performs the arithmetic operation using the eval() function and displays the formatted result.
It also handles errors such as invalid operations.
•	Additional Functionalities :-
clear() resets all values and clears the display.
toggle_sign() changes the sign of the number.
percentage() converts the number into its percentage value.
•	Program Execution :- 
The main block creates the application window, initializes the calculator object, and runs the program using the main event loop.________________________________________
________________________________________
5. Sample Test Cases
Input	Operation	Output
5, 3	Addition	8
10, 4	Subtraction	6
6, 2	Multiplication	12
8, 2	Division	4
5, 0	Division	Error
________________________________________
6 . Challenges Faced
The main challenge faced during this project was handling division by zero, which can cause runtime errors. Additionally, validating user input to ensure correct operation selection was necessary to make the program more reliable.
________________________________________
7 . Results and Observations
The calculator successfully performs all basic arithmetic operations. It provides accurate results and handles special cases such as division by zero. The program is simple, efficient, and user-friendly.
________________________________________

