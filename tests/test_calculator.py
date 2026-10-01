""" tests/test_calculator.py """
import sys
import pytest
from io import StringIO
from app.calculator import display_help, display_history, calculator

def test_display_help(capsys):
    """ 
    Tests to ensure that the correct help message is displayed.
    """
    display_help()
    captured = capsys.readouterr()
    expected_output = """
    REPL Calculator Help
    --------------------
    In order to use the REPL calculator: input <operation> <num1> <num2> to perform a specific operation with 2 numbers 
    
    Supported operations include: 
    - add
    - subtract (note: this subtracts the second number from the first)
    - multiply
    - divide (note: this divides the first number by the second)

    Some special commands that could be helpful: 
    - help : Displays this help message
    - history : Shows your history of calculations 
    - exit : Exits the calculator 

    Example operations: 
    add 1 1 
    subtract 5 3
    multiply 2 4
    divide 10 2
    """
    assert captured.out.strip() == expected_output.strip()

def test_display_history_empty(capsys):
    """Test to ensure that the correct message is displayed when history is empty."""
    history = []
    display_history(history)
    captured = capsys.readouterr()
    assert captured.out.strip() == "No calculations have been performed yet."

def test_display_history(capsys):
    """Test to ensure that the correct calculation history is displayed."""
    history = ["addition: 1.0 add 1.0 = 2.0",
                "subtraction: 5.0 subtract 2.0 = 3.0",
                "multiplication: 2.0 multiply 4.0 = 8.0",
                "division: 10.0 divide 2.0 = 5.0"]
    display_history(history)
    captured = capsys.readouterr()
    expected_output = """Calculation History:
1. addition: 1.0 add 1.0 = 2.0
2. subtraction: 5.0 subtract 2.0 = 3.0
3. multiplication: 2.0 multiply 4.0 = 8.0
4. division: 10.0 divide 2.0 = 5.0
    """
    assert captured.out.strip() == expected_output.strip()

def test_exit(monkeypatch, capsys):
    """Test the exit command in REPL."""
    user_input= "exit\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit) as exc_info:
        calculator()
    captured = capsys.readouterr()
    assert "Exiting calculator now... Thank you!" in captured.out
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0

def test_calculator_help_command(monkeypatch,capsys):
    """Test the help command in REPL."""
    user_input= "help\nexit\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit) as exc_info:
        calculator()
    captured = capsys.readouterr()
    assert "REPL Calculator Help" in captured.out
    assert "Exiting calculator now... Thank you!" in captured.out

def test_invalid_input(monkeypatch,capsys):
    """Test invalid input in REPL."""
    user_input = "invalid input\nadd 1\nsubtract 5\nexist\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit) as exc_info:
        calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please follow the format: <operation> <num1> <num2>" in captured.out
    assert "Type 'help' for more instructions!" in captured.out

# Helper function to capture print statements
def run_calculator_with_input(monkeypatch, inputs):
    """
    Simulates user input and captures output from the calculator REPL.
    
    :param monkeypatch: pytest fixture to simulate user input
    :param inputs: list of inputs to simulate
    :return: captured output as a string
    """
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Capture the output of the calculator
    #captured_output = StringIO()
    #sys.stdout = captured_output
    #calculator()
    #sys.stdout = sys.__stdout__  # Reset stdout
    #return captured_output.getvalue()

# Positive Tests
def test_addition(monkeypatch, capsys):
    """Test addition operation in REPL."""
    #inputs = ["add 2 3", "exit"]
    #output = run_calculator_with_input(monkeypatch, inputs)
    #assert "Result: 5.0" in output
    user_input = "add 1 1\nexit\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Result: AddCalculation: 1.0 Add 1.0 = 2.0" in captured.out

def test_subtraction(monkeypatch, capsys):
    """Test subtraction operation in REPL."""
    #inputs = ["subtract 5 2", "exit"]
    #output = run_calculator_with_input(monkeypatch, inputs)
    #assert "Result: 3.0" in output
    user_input = "subtract 5 2\nexit\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Result: SubtractCalculation: 5.0 Subtract 2.0 = 3.0" in captured.out

def test_multiplication(monkeypatch, capsys):
    """Test multiplication operation in REPL."""
    #inputs = ["multiply 4 5", "exit"]
    #output = run_calculator_with_input(monkeypatch, inputs)
    #assert "Result: 20.0" in output
    user_input = "multiply 2 4\nexit\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Result: MultiplyCalculation: 2.0 Multiply 4.0 = 8.0" in captured.out

def test_division(monkeypatch, capsys):
    """Test division operation in REPL."""
    #inputs = ["divide 10 2", "exit"]
    #output = run_calculator_with_input(monkeypatch, inputs)
    #assert "Result: 5.0" in output
    user_input = "divide 10 2\nexit\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Result: DivideCalculation: 10.0 Divide 2.0 = 5.0" in captured.out

# Negative Tests
def test_invalid_operation(monkeypatch, capsys):
    """Test invalid operation in REPL."""
    #inputs = ["modulus 5 3", "exit"]
    #output = run_calculator_with_input(monkeypatch, inputs)
    #assert "Unknown operation" in output
    user_input = "modulus 5 3\nexit\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Unsupported calculation type: 'modulus'. Available types: add, subtract, multiply, divide" in captured.out
    assert "Type 'help' for more instructions and the list of supported operations!" in captured.out

def test_invalid_input_format(monkeypatch, capsys):
    """Test invalid input format in REPL."""
    #inputs = ["add two three", "exit"]
    #output = run_calculator_with_input(monkeypatch, inputs)
    #assert "Invalid input. Please follow the format" in output
    user_input = "add two three\nexit\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please follow the format: <operation> <num1> <num2>" in captured.out or \
           "could not convert string to float: 'two'" in captured.out

def test_division_by_zero(monkeypatch, capsys):
    """Test division by zero in REPL."""
    #inputs = ["divide 5 0", "exit"]
    #output = run_calculator_with_input(monkeypatch, inputs)
    #assert "Division by zero is not allowed" in output
    user_input = "divide 5 0\nexit\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Division by zero is not allowed" in captured.out

def test_history(monkeypatch, capsys):
    """Test history functionality in REPL."""
    user_input = "add 1 1\nhistory\nexit\n"
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Result: AddCalculation: 1.0 Add 1.0 = 2.0" in captured.out
    assert "Calculation History:" in captured.out
    assert "1. AddCalculation: 1.0 Add 1.0 = 2.0" in captured.out

def test_calculator_keyboard_interrupt(monkeypatch, capsys):
    """
    Test the calculator's handling of KeyboardInterrupt (Ctrl+C)."""
    def mock_input(prompt):
        raise KeyboardInterrupt()
    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit) as exc_info:
        calculator()
    captured = capsys.readouterr()
    assert "\nKeyboard interrupt detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0

def test_calculator_eof_error(monkeypatch, capsys):
    """
    Test the calculator's handling of EOFError (Ctrl+D). """    
    def mock_input(prompt):
        raise EOFError()
    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit) as exc_info:
        calculator()
    captured = capsys.readouterr()
    assert "\nEOF detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0

def test_calculator_unexpected_exception(monkeypatch, capsys):
    """
    Test the calculator's handling of unexpected exceptions during calculation execution. """
    class MockCalculation:
        def execute(self):
            raise Exception("Mock exception during execution")
        def __str__(self):
            return "MockCalculation"
    def mock_create_calculation(operation, a, b):
        return MockCalculation()
    monkeypatch.setattr('app.calculation.CalculationFactory.create_calculation', mock_create_calculation)
    user_input = 'add 10 5\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "An error has occurred during calculation: Mock exception during execution" in captured.out
    assert "Please try again!" in captured.out