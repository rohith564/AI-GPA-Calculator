
from flask import Flask,render_template,request

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
    
@app.route('/calculator',methods=["GET","POST"])
def calc():
    if request.method == "GET":
        return render_template("calculator.html")

@app.route('/text_extraction',methods=["GET","POST"])
def extract():
    if request.method == "POST":
        # 1. Load your marksheet
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
        - If the same subject appears multiple times for Semester {semester}, keep the latest grade shown on the page which given lower on the page (lower the page  means latest grades).
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

        # 2. Generate the response using the new v1 client method
 
        response = client.models.generate_content(model="gemini-3-flash-preview",contents=[prompt, img])
    
        text = response.text.strip()

        # Remove markdown if Gemini returns it
        text = text.replace("```json", "")
        text = text.replace("```", "").strip()

        try:
            marks = json.loads(text)

        except json.JSONDecodeError:
            return f"""
            <h3>Gemini returned invalid JSON</h3>
            <pre>{text}</pre>
            """

        '''
        #        output looks like this:
        marks={
                    'CCS340':'A+',
                    'CCS375':'O'
        }'''

        credits={}
        for subject_code in marks:
            subject = Subject.query.filter_by(subject_code=subject_code).first()
            if subject:
                credits[subject_code] = subject.credits
                
            else:
                credits[subject_code] = "Subject not found in database"
        
        return render_template("grades.html", marks=marks,credits=credits)


@app.route("/gpa")
def gpa():
    a = request.args.get("marks")
    b = request.args.get("credits")

    grade_points = {
        "O": 10,
        "A+": 9,
        "A": 8,
        "B+": 7,
        "B": 6,
        "C": 5,
        "U": 0,
        "AB": 0
    }

    marks=json.loads(a)
    credits=json.loads(b)

    total_credits = 0
    total_points = 0

    for subject_code in marks:
        point = grade_points[marks[subject_code]]

        total_credits += credits[subject_code]
        total_points += point * credits[subject_code]

    if total_credits == 0:
        return "Total credits cannot be zero."

    gpa = total_points / total_credits

    return f"<h1> Your GPA is: <i><bold>{gpa:.4f}</bold></i></h1>"


if __name__=="__main__":
    app.run(debug=True)