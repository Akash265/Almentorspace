from flask import Flask, request, jsonify, render_template, send_file
import cv2
import numpy as np
from io import BytesIO
from OCR import process_image, remove_non_text_objects, spell_check, generate_pdf


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/ocr", methods=["POST"])
def ocr_endpoint():
    # Get the uploaded file from the request
    uploaded_file = request.files["file"]

    # Get the uploaded file from the request
    uploaded_file = request.files["file"]

    # Read the uploaded file as an image using OpenCV
    image = cv2.imdecode(
        np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR
    )
    print(np.fromstring(uploaded_file.read(), np.uint8))
    # Preprocess and extract text from the image
    text = process_image(image)

    # Remove non-text objects and detect text
    detected_text = remove_non_text_objects(text)

    # Perform spell checking on the detected text
    corrected_text = spell_check(detected_text)

    # Generate a PDF from the corrected text
    pdf_stream = generate_pdf(corrected_text)

    # Set the appropriate content headers
    headers = {
        "Content-Type": "application/pdf",
        "Content-Disposition": "attachment; filename=output.pdf",
    }

    # Return the PDF file as a response
    return send_file(BytesIO(pdf_stream.getvalue()), download_name="output.pdf")


if __name__ == "__main__":
    app.run()
