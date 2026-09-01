
from flask import Flask,render_template,request, url_for

from google import genai
import os
from dotenv import load_dotenv
from PIL import Image
import json

from models import db, Subject

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///college.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/',methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
import json
from PIL import Image
from flask import request, render_template, url_for

@app.route('/calculator', methods=["GET", "POST"])
def calc():
    # 1. Handle the initial page load
    if request.method == "GET":
        return render_template("calculator.html", result=None)

    # 2. Handle the form submission
    if request.method == "POST":
        img_file = request.files.get("marksheet")
        semester = request.form.get("semester")

        if not img_file:
            return "Please upload a marksheet."

        try:
            img = Image.open(img_file)
        except Exception:
            return "Invalid image file."

        prompt = f""" 
        You are extracting examination results from an Anna University marksheet.

        The user wants to calculate GPA for Semester {semester}.

        Instructions:
        1. Extract ONLY the Subject Code and Grade for Semester {semester}.
        2. Ignore subjects from all other semesters.
        3. If multiple tables are present (Main Result, Revaluation, Photocopy, Arrear, Supplementary):
           - Use only the records that belong to Semester {semester}.
           - If the same subject appears multiple times for Semester {semester}, keep the latest grade shown on the page which given lower on the page (lower the page means latest grades).
        4. Ignore Register Number, Name, Branch, Semester column, Result, PASS/RA, SGPA, CGPA, GPA and any other text.
        5. Return ONLY a valid JSON object.
        6. Do not return markdown.
        7. Do not use ```json.
        8. Do not explain anything.

        Example:
        {{
            "CS3301": "O",
            "MA3354": "A+",
            "CS3351": "B+"
        }}
        """

        
        print("Analyzing table with Modern Vision AI...")

        # Generate response using Gemini
        try:
            response = client.models.generate_content(model="gemini-3-flash-preview", contents=[prompt, img])
            text = response.text.strip()
            text = text.replace("```json", "").replace("```", "").strip()
            marks = json.loads(text)
        except json.JSONDecodeError:
            return f"<h3>Gemini returned invalid JSON</h3><pre>{text}</pre>"
        except Exception as e:
            return f"<h3>Error connecting to AI:</h3><p>{str(e)}</p>"
            

        """marks = {
                "CCS347": "B",
                "CCS352": "A",
                "CCS356": "B+",
                "CCS366": "B",
                "CCS373": "C",
                "CS3691": "B+",
                "MX3085": "O",
                "SB8015": "O"
            }"""            
        # 3. Setup variables for FGPA Calculation
        grade_points = {
            "S": 10,"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "U": 0, "AB": 0
        }
        
        total_credits = 0
        total_points = 0
        subjects_data = [] # We will store all table info here to pass to HTML

        # 4. Loop through extracted marks, fetch credits, and do the math
        for subject_code, grade in marks.items():
            subject = Subject.query.filter_by(subject_code=subject_code).first()
            
            if subject:
                credit_val = subject.credits
                point = grade_points.get(grade, 0) # Safely gets the point value, defaults to 0
                
                # Math for final GPA
                total_credits += credit_val
                total_points += (point * credit_val)
                
                # Append to our list for the HTML table
                subjects_data.append({
                    "code": subject_code,
                    "grade": grade,
                    "credits": credit_val,
                    "grade_point": point,
                    "total": point * credit_val
                })
            else:
                # Handle cases where the subject isn't in your Anna University DB
                subjects_data.append({
                    "code": subject_code,
                    "grade": grade,
                    "credits": "N/A",
                    "grade_point": "N/A",
                    "total": "N/A"
                })

        # 5. Final Calculation and Error Checking
        if total_credits == 0:
            return "Total credits cannot be zero. Ensure valid subjects were found."

        gpa = total_points / total_credits

        # 6. Package everything neatly
        result = {
            "gpa": round(gpa, 6), # Rounds to 6 decimal places safely
            "total_credits": total_credits,
            "total_points": total_points,
            "subjects": subjects_data
        }

        # 7. Send the packaged data straight to the HTML template
        return render_template("calculator.html", result=result)        

if __name__=="__main__":
    app.run(debug=True)