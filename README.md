# LinkedIn PDF to HTML Resume Generator with Gemini API

This project is a web application built using **Flask** that allows users to upload their LinkedIn PDF resume and converts it into an HTML resume. It leverages the **Gemini (Google Generative AI)** API to automatically generate professional HTML and CSS code for the resume.

## Project Overview

The objective of this project is to create a web application that:
1. Accepts a **PDF** resume (downloaded from LinkedIn).
2. Extracts the text from the PDF.
3. Sends the extracted resume text to the **Gemini API** to generate professional HTML and CSS code.
4. Displays the generated resume on the browser and provides an option to download it as an HTML file.



## Technologies Used

- **Python**: The backend language.
- **Flask**: The web framework to handle routes and requests.
- **PyPDF2**: Library to extract text from PDF files.
- **Gemini (Google Generative AI)**: The API used for generating HTML and CSS from the extracted resume text.
- **HTML/CSS**: For the front-end templates and styling.

## Approach

The approach followed to solve the problem is broken down into the following steps:

### Step 1: Input API Key and Upload PDF
- The user is asked to input their **Gemini API key** and upload their **LinkedIn PDF** file.
  
### Step 2: Extract Text from PDF
- The uploaded PDF file is parsed using **PyPDF2** to extract the text content.
  
### Step 3: Generate HTML and CSS Using Gemini API
- The extracted text is sent to the **Gemini API** along with a prompt to generate professional HTML and CSS code. The API returns a complete HTML page with inline CSS that represents the user's resume.
  
### Step 4: Display and Download the HTML Resume
- The generated HTML content is displayed on the result page.
- The user is provided an option to **download** the generated HTML resume.
