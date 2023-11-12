# Image to Supermarket Billing

The code uses the easyocr library for optical character recognition (OCR).
extraction_and_accumulate_numbers is a function that takes an image path as an input parameter.
An OCR reader is created with the language set to English ('en').
The readtext method is used to extract text from the image.
The code iterates through the results, extracts numbers, and accumulates them row-wise.
The accumulated numbers and their individual addition to each row are printed.
The user is prompted to enter the path to the image file with a .jpg extension.

Let's go through each part of the code with detailed explanations:

```python
import easyocr
```
This line imports the `easyocr` library, which is used for optical character recognition (OCR).

```python
def extraction_and_accumulate_numbers(image_path):
```
Defines a function named `extraction_and_accumulate_numbers` that takes an `image_path` as a parameter.

```python
    # Creating an OCR reader
    reader = easyocr.Reader(['en'])
```
Creates an OCR reader using the `easyocr.Reader` class, specifying the language as English ('en').

```python
    # Reading text from the image
    result = reader.readtext(image_path)
```
Uses the `readtext` method of the OCR reader to extract text from the image specified by `image_path`.

```python
    # Processing the result to extract whole numbers in row-wise
    accumulated_numbers = []
    current_row_numbers = []
```
Creates empty lists (`accumulated_numbers` and `current_row_numbers`) to store accumulated numbers and numbers in the current row, respectively.

```python
    for detection in result:
```
Iterates through the results obtained from the OCR.

```python
        text = detection[1]
```
Extracts the text from the detection result.

```python
        # Checking if the text is not empty or just a whitespace
        if text.strip():
```
Ensures that the extracted text is not empty or just whitespace.

```python
            if text.isdigit():
```
Checks if the text consists of digits.

```python
                # If the text is a digit, converting it to an integer
                current_number = int(text)
```
Converts the digit text to an integer (`current_number`).

```python
                # Adding the current number to the current row
                current_row_numbers.append(current_number)
```
Appends the current number to the list of numbers in the current row.

```python
                # Printing a message indicating the number being added to the current row
                print("Adding rupees {} to the current list".format(current_number))
```
Prints a message indicating the current number being added to the current row.

```python
            elif current_row_numbers:
```
Checks if there are numbers in the current row.

```python
                # If the current row has numbers, extending the accumulated list with the numbers from the current row
                accumulated_numbers.extend(current_row_numbers)
```
Extends the list of accumulated numbers with the numbers from the current row.

```python
                # Resetting the current row for the next set of numbers
                current_row_numbers = []
```
Resets the list of numbers in the current row for the next set of numbers.

```python
    # Handling the last row of numbers
    if current_row_numbers:
```
Checks if there are numbers in the last row.

```python
        # If there are numbers in the last row, extending the accumulated list with those numbers
        accumulated_numbers.extend(current_row_numbers)
```
Extends the list of accumulated numbers with the numbers from the last row.

```python
    # Printing the accumulated numbers row-wise and the total sum
    print("\nPrices of Items as a list: {}".format(accumulated_numbers))
    print("\nTotal Bill of the Purchase: {}".format(sum(accumulated_numbers)))
```
Prints the accumulated numbers row-wise and the total sum of the prices of items.

```python
# Inserting the Image path from the system file
image_path = input("Enter the path to your image file (with a .jpg extension): ")
```
Prompts the user to enter the path to their image file with a .jpg extension.

```python
extraction_and_accumulate_numbers(image_path)
```
Calls the `extraction_and_accumulate_numbers` function with the provided `image_path` as an argument.

This code overall performs OCR on an image, extracts numbers, accumulates them row-wise, and prints the accumulated numbers and the total sum of the prices of items. Users are prompted to input the path to their image file.
