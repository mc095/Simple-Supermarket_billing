# predicting total cost image to sum up billing at supermarket

This code defines a Python function that uses the EasyOCR library to perform optical character recognition (OCR) on an image, extract numerical values, and accumulate them. It then incorporates this function into a loop, allowing the user to input the path to an image file, process the bill, and decide whether to enter another bill.

Let's break down the code:

1. **Importing the EasyOCR library:**
   ```python
   import easyocr
   ```
   This line imports the `easyocr` library, which is a Python wrapper for the EasyOCR optical character recognition engine.

2. **Defining the OCR function:**
   ```python
   def extraction_and_accumulate_numbers(image_path):
   ```
   This function takes an `image_path` parameter, representing the path to an image file.

3. **Creating an OCR reader:**
   ```python
   reader = easyocr.Reader(['en'])
   ```
   This line creates an OCR reader object for the English language (`'en'`).

4. **Reading text from the image:**
   ```python
   result = reader.readtext(image_path)
   ```
   This line uses the OCR reader to extract text from the specified image, and the result is stored in the `result` variable.

5. **Processing the result to extract whole numbers:**
   ```python
   accumulated_numbers = []
   current_row_numbers = []
   ```
   Initialize two lists, `accumulated_numbers` and `current_row_numbers`, to store the extracted numbers.

6. **Iterating through OCR results:**
   ```python
   for detection in result:
   ```
   Loop through each text detection in the OCR result.

7. **Checking and extracting numbers:**
   ```python
   text = detection[1]
   if text.strip():
       if text.isdigit():
           current_number = int(text)
           current_row_numbers.append(current_number)
       elif current_row_numbers:
           accumulated_numbers.extend(current_row_numbers)
           current_row_numbers = []
   ```
   If the detected text is not empty or just whitespace, check if it's a digit. If it is, convert it to an integer and add it to the `current_row_numbers` list. If the text is not a digit and the current row has numbers, extend the `accumulated_numbers` list with the numbers from the current row and reset the `current_row_numbers` for the next set of numbers.

8. **Handling the last row of numbers:**
   ```python
   if current_row_numbers:
       accumulated_numbers.extend(current_row_numbers)
   ```
   After the loop, check if there are numbers in the last row and extend the `accumulated_numbers` list accordingly.

9. **Printing the result:**
   ```python
   print("\nPrices of Items as a list: {}".format(accumulated_numbers))
   print("\nTotal Bill of the Purchase: {}".format(sum(accumulated_numbers)))
   ```
   Print the accumulated numbers as a list and their total sum.

10. **Main loop for user interaction:**
    ```python
    while True:
    ```
    Enter a loop that continues until the user decides to exit.

11. **User input for image path:**
    ```python
    image_path = input("Enter the path to your image file (with a .jpg or .png extension): ")
    ```
    Prompt the user to input the path to an image file.

12. **Processing the bill:**
    ```python
    extraction_and_accumulate_numbers(image_path)
    ```
    Call the defined function to process the bill using the provided image path.

13. **Asking the user if they want to enter another bill:**
    ```python
    another_bill = input("Do you want to enter another bill? (yes/no): ").lower()
    if another_bill != 'yes':
        break
    ```
    Prompt the user if they want to enter another bill. If the response is not 'yes', exit the loop, ending the program.
