## ✨ Key Features

*   **AI Marksheet Parsing:** Upload your marksheet (JPG, PNG, or PDF) and let the Gemini API automatically analyze the document to extract your subject codes and grades with high accuracy.
*   **Smart Credit Fetching:** Automatically retrieves the exact subject credits from the database based on your selected Regulation, Department, and Semester.
*   **High-Precision Calculation:** Calculates your final GPA accurately up to 6 decimal points using the official Anna University grading system.
*   **Export Results:** View subject-wise results, total grade points, and instantly download your final GPA report as a PDF.
*   **Responsive UI:** A clean, mobile-friendly interface built with HTML, CSS, and Vanilla JS.



## 🗄️ Database Architecture & AI Flow

This project combines the vision capabilities of **Google's Gemini API** with a **SQLite database** managed via a Python **ORM**. 

**How the Data Flows:** 
1. **Upload & AI Extraction:** The user uploads a marksheet image. The Flask backend sends this image to the Gemini API, which acts as an advanced data extractor, pulling out the exact `subject_code` and `grade` pairs from the document.
2. **Dynamic DB Querying:** Instead of hardcoding subject credits, the database uses relational models (Regulation, Department, Subject). 
3. **Calculation:** When Gemini returns a subject code (e.g., `CS3351`), the Flask backend queries the ORM to instantly fetch the exact credit weight for that specific course. It then matches the extracted grade to the official grade points and calculates the GPA.