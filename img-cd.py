import easyocr

def extraction_and_accumulate_numbers(image_path):
    # Creating an OCR reader
    reader = easyocr.Reader(['en'])

    # Reading text from the image
    result = reader.readtext(image_path)

    # Processing the result to extract whole numbers in row-wise
    accumulated_numbers = []
    current_row_numbers = []

    for detection in result:
        text = detection[1]

        # Checking if the text is not empty or just whitespace
        if text.strip():
            # If the text is a digit, converting it to an integer
            if text.isdigit():
                current_number = int(text)
                # Adding the current number to the current row
                current_row_numbers.append(current_number)
            # If the text is not a digit and the current row has numbers
            elif current_row_numbers:
                # Extending the accumulated list with the numbers from the current row
                accumulated_numbers.extend(current_row_numbers)
                # Resetting the current row for the next set of numbers
                current_row_numbers = []

    # Handling the last row of numbers
    if current_row_numbers:
        # Extending the accumulated list with the numbers from the last row
        accumulated_numbers.extend(current_row_numbers)

    # Printing the accumulated numbers and the total sum
    print("\nPrices of Items as a list: {}".format(accumulated_numbers))
    print("\nTotal Bill of the Purchase: {}".format(sum(accumulated_numbers)))

# Main loop
while True:
    # Inserting the Image path from the user
    image_path = input("Enter the path to your image file (with a .jpg or .png extension): ")
    
    # Processing the bill
    extraction_and_accumulate_numbers(image_path)

    # Asking the user if they want to enter another bill
    another_bill = input("Do you want to enter another bill? (yes/no): ").lower()
    if another_bill != 'yes':
        break
