from flask import Flask, render_template, request, send_file
import PyPDF2
import os
import google.generativeai as genai
from io import BytesIO

app = Flask(__name__)

# Function to configure API key for Gemini/Generative AI
def configure_api(api_key):
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        return f"Error configuring API key: {e}"
    return None

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to generate HTML and CSS using the Gemini model
def generate_resume(resume_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Generate a professional HTML resume page with inline CSS using the following resume text while satisfying following conditions - 1) The page should be A4 2) The headings and texts must be properly aligned 3) The alignment and spaces between the headings and items must be quite profesional 4) The resume must be centered 5) Remove all the comments from the html and css code 6) The contents of the resume must be left aligned with bullet ponits 7) Limit the reusme to a single page that must look profesional 8) The summary part must be totaly ignored:\n{resume_text}"
    response = model.generate_content(prompt)
    return response.text

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get API Key
        print("chk kro ",request.method)
        api_key = request.form['api_key']
        
        # Check if the user uploaded a file
        if 'pdf_file' not in request.files or request.files['pdf_file'].filename == '':
            return render_template('index.html', error="Please upload a PDF file.")

        pdf_file = request.files['pdf_file']
        # Configure the API
        api_error = configure_api(api_key)
        if api_error:
            return render_template('index.html', error=api_error)
        
        # Extract text from the PDF
        try:
            extracted_text = extract_text_from_pdf(pdf_file)
            print("chk kro2 ",extracted_text)
        except Exception as e:
            return render_template('index.html', error=f"Error extracting text from PDF: {e}")
        
        # Generate HTML resume using Gemini
        try:
            html_and_css = generate_resume(extracted_text)
            print("chk kro3 ",html_and_css)
        except Exception as e:
            return render_template('index.html', error=f"Error generating HTML and CSS: {e}")
        
        # Store the HTML content in memory (or on disk)
        html_file = BytesIO()
        html_file.write(html_and_css.encode('utf-8'))
        html_file.seek(0)
        
        # Render result page with the generated HTML
        return render_template('result.html', html_content=html_and_css)

    return render_template('index.html')

# Route to download the generated HTML file
@app.route('/download', methods=['POST'])
def download():
    html_content = request.form['html_content']
    html_file = BytesIO()
    html_file.write(html_content.encode('utf-8'))
    html_file.seek(0)
    return send_file(html_file, as_attachment=True, attachment_filename="resume.html", mimetype='text/html')

if __name__ == "__main__":
    app.run(debug=True)
