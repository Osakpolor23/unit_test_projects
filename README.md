# Unit Testing in Python: Ensuring Code Reliability with Pytest

## Overview
Unit testing is a fundamental practice in software development that ensures individual components of a program function as expected. By isolating each function and testing its behavior under various conditions, developers can catch bugs early and maintain code reliability.

In this repository, I focused on unit testing using the pytest framework. The four test files i.e. test_fuel.py, test_plates.py, test_bank.py, and test_twttr.py each validate the correctness of specific functions from their corresponding source files. Through rigorous testing, I ensured that the functions handle both expected and edge cases properly, providing accurate results consistently.

Each test file follows the unit testing principles, checking various inputs, expected outputs, and error handling cases.

## Test Files Breakdown

### **1. test_fuel.py – Testing Fuel Gauge Functions**

This file tests the functionality of convert() and gauge() functions from fuel.py:

**convert(fraction: str) -> int**

    Converts a fraction (e.g., "1/4") into a percentage.

    Raises ValueError for invalid fractions.

    Raises ZeroDivisionError if the denominator is zero.

    Ensures rounding to the nearest whole number.

**gauge(percentage: int) -> str**

    Returns "E" if the percentage is ≤1 (empty).

    Returns "F" if the percentage is ≥99 (full).

    Returns the percentage formatted as "Z%" otherwise.

The Unit Tests Cover: Valid fraction conversions, handling division errors, incorrect inputs, and proper gauge outputs.

### **2. test_plates.py – Validating License Plate Formats**

This file tests the is_valid() function from plates.py, ensuring correct license plate formatting

**is_valid(plate: str) -> bool**

    Plate must start with two letters.

    Must be between 2-6 characters long.

    Numbers must follow letters without leading zeroes.

    Only alphanumeric characters are allowed(no special characters or symbols)

The Unit Tests Cover: Valid and invalid plate formats, length restrictions, number placement rules, and special character rejection.

### **3. test_bank.py – Checking Greeting-Based Bank Values**

This file tests the value() function from bank.py, ensuring correct responses based on greetings.

**value(greeting: str) -> int**

    "hello" or greetings starting with "hello" → Returns 0.

    Greetings starting with "h" but not "hello" → Returns 20.

    Other greetings → Returns 100.

The Unit Tests Cover: Different greeting styles, uppercase/lowercase variations, and unexpected inputs.

### **4. test_twttr.py – Testing Tweet Text Shortener**

This file tests the shorten() function from twttr.py, which removes vowels from words.

**shorten(text: str) -> str**

    Removes lowercase and uppercase vowels (a, e, i, o, u).

    Preserves spaces, numbers, and punctuation.

The Unit Tests Cover: Basic vowel removal, mixed-case words, sentences with punctuation, and input edge cases.

Feel free to fork this repository, submit pull requests, or suggest additional test cases to improve coverage.