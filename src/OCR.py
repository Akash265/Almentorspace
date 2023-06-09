import cv2
import pytesseract
from spellchecker import SpellChecker
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def process_image(image):
    # Preprocess the image if needed (e.g., resize, denoise, etc.)
    # ...

    # Apply OCR using Tesseract
    text = pytesseract.image_to_string(image)

    return text


def remove_non_text_objects(text):
    # Split the text into individual lines
    lines = text.split("\n")

    # Remove non-text objects
    cleaned_lines = []
    for line in lines:
        # Remove lines with no alphanumeric characters (non-text)
        if any(char.isalnum() for char in line):
            cleaned_lines.append(line)

    # Join the cleaned lines back into a single string
    cleaned_text = "\n".join(cleaned_lines)

    return cleaned_text


def spell_check(text):
    spell = SpellChecker()

    # Split the text into individual words
    words = text.split()

    # Correct misspelled words
    corrected_text = []
    for word in words:
        corrected_word = spell.correction(word)
        corrected_text.append(corrected_word)

    # Join the corrected words back into a single string
    corrected_text = " ".join(corrected_text)

    return corrected_text


def generate_pdf(text):
    # Create a BytesIO stream to hold the PDF data
    pdf_stream = BytesIO()

    # Create a canvas with letter size page
    c = canvas.Canvas(pdf_stream, pagesize=letter)

    # Set the font and font size
    c.setFont("Helvetica", 12)

    # Calculate the max width and height of the canvas
    max_width, max_height = letter

    # Set the margin for the text
    margin = 50

    # Calculate the available width and height for the text
    text_width = max_width - 2 * margin
    text_height = max_height - 2 * margin

    # Split the text into lines
    lines = text.split("\n")

    # Start at the top-left corner of the text area
    x, y = margin, max_height - margin

    # Iterate over the lines and write them to the canvas
    for line in lines:
        # Check if the line exceeds the available height
        if y - margin < 0:
            break

        # Write the line to the canvas
        c.drawString(x, y, line)

        # Move to the next line
        y -= 16

    # Save the canvas as a PDF file
    c.showPage()
    c.save()

    # Reset the stream position to the beginning
    pdf_stream.seek(0)

    return pdf_stream
