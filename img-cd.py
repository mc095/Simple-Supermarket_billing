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

        # Checking if the text is not empty or just a whitespaces
        if text.strip():
            if text.isdigit():
                # If the text is a digit, converting it to an integer
                current_number = int(text)
                # Adding the current number to the current row
                current_row_numbers.append(current_number)
                # Printing a message indicating the number being added to the current row
                print("Adding rupees {} to the current list".format(current_number))
            elif current_row_numbers:
                # If the current row has numbers, extending the accumulated list with the numbers from the current row
                accumulated_numbers.extend(current_row_numbers)
                # Resetting the current row for the next set of numbers
                current_row_numbers = []

    # Handling the last row of numbers
    if current_row_numbers:
        # If there are numbers in the last row, extending the accumulated list with those numbers
        accumulated_numbers.extend(current_row_numbers)

    # Printing the accumulated numbers row-wise and the total sum
    print("\nPrices of Items as a list: {}".format(accumulated_numbers))
    print("\nTotal Bill of the Purchase: {}".format(sum(accumulated_numbers)))

# Inserting the Image path from the system file
image_path = input("Enter the path to your image file (with a .jpg extension): ")
extraction_and_accumulate_numbers(image_path)
