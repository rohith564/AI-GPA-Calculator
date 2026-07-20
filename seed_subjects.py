from app import app
from models import db, Subject

subjects = [
    # =====================================
    # 2021 Regulation CSE Sem 1 Subjects
    # =====================================
    {
        "department": "CSE",
        "regulation": 2021,
        "semester": 1,
        "subject_code": "IP3151",
        "subject_name": "Induction Programme",
        "credits": 0,
        "category": "-"
    },
    {
        "department": "CSE",
        "regulation": 2021,
        "semester": 1,
        "subject_code": "HS3152",
        "subject_name": "Professional English - I",
        "credits": 3,
        "category": "HSMC"
    },
    {
        "department": "CSE",
        "regulation": 2021,
        "semester": 1,
        "subject_code": "MA3151",
        "subject_name": "Matrices and Calculus",
        "credits": 4,
        "category": "BSC"
    },
    {
        "department": "CSE",
        "regulation": 2021,
        "semester": 1,
        "subject_code": "PH3151",
        "subject_name": "Engineering Physics",
        "credits": 3,
        "category": "BSC"
    },
    {
        "department": "CSE",
        "regulation": 2021,
        "semester": 1,
        "subject_code": "CY3151",
        "subject_name": "Engineering Chemistry",
        "credits": 3,
        "category": "BSC"
    },
    {
        "department": "CSE",
        "regulation": 2021,
        "semester": 1,
        "subject_code": "GE3151",
        "subject_name": "Problem Solving and Python Programming",
        "credits": 3,
        "category": "ESC"
    },
    {
        "department": "CSE",
        "regulation": 2021,
        "semester": 1,
        "subject_code": "GE3152",
        "subject_name": "Heritage of Tamils",
        "credits": 1,
        "category": "HSMC"
    },
    {
        "department": "CSE",
        "regulation": 2021,
        "semester": 1,
        "subject_code": "GE3171",
        "subject_name": "Problem Solving and Python Programming Laboratory",
        "credits": 2,
        "category": "ESC"
    },
    {
        "department": "CSE",
        "regulation": 2021,
        "semester": 1,
        "subject_code": "BS3171",
        "subject_name": "Physics and Chemistry Laboratory",
        "credits": 2,
        "category": "BSC"
    },
    {
        "department": "CSE",
        "regulation": 2021,
        "semester": 1,
        "subject_code": "GE3172",
        "subject_name": "English Laboratory",
        "credits": 1,
        "category": "EEC"
    },
    # ==========================================
    # 2021 Regulation CSE Sem 2 Subjects
    # ==========================================
    {
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "HS3252",
    "subject_name": "Professional English - II",
    "credits": 2,
    "category": "HSMC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "MA3251",
    "subject_name": "Statistics and Numerical Methods",
    "credits": 4,
    "category": "BSC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "PH3256",
    "subject_name": "Physics for Information Science",
    "credits": 3,
    "category": "BSC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "BE3251",
    "subject_name": "Basic Electrical and Electronics Engineering",
    "credits": 3,
    "category": "ESC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "GE3251",
    "subject_name": "Engineering Graphics",
    "credits": 4,
    "category": "ESC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "CS3251",
    "subject_name": "Programming in C",
    "credits": 3,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "GE3252",
    "subject_name": "தமிழரும் தொழில்நுட்பமும் (Tamils and Technology)",
    "credits": 1,
    "category": "HSMC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "BE3271",
    "subject_name": "Basic Electrical and Electronics Engineering Laboratory",
    "credits": 2,
    "category": "ESC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "CS3271",
    "subject_name": "Programming in C Laboratory",
    "credits": 2,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "GE3271",
    "subject_name": "Engineering Practices Laboratory",
    "credits": 2,
    "category": "ESC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 2,
    "subject_code": "GE3272",
    "subject_name": "Communication Laboratory / Foreign Language",
    "credits": 1,
    "category": "EEC"
},

# ==============================
# 2021 Regulation CSE Sem 3 Subjects
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 3,
    "subject_code": "MA3354",
    "subject_name": "Discrete Mathematics",
    "credits": 4,
    "category": "BSC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 3,
    "subject_code": "CS3351",
    "subject_name": "Digital Principles and Computer Organization",
    "credits": 4,
    "category": "ESC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 3,
    "subject_code": "CS3352",
    "subject_name": "Foundations of Data Science",
    "credits": 3,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 3,
    "subject_code": "CS3301",
    "subject_name": "Data Structures",
    "credits": 3,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 3,
    "subject_code": "CS3391",
    "subject_name": "Object Oriented Programming",
    "credits": 3,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 3,
    "subject_code": "CS3311",
    "subject_name": "Data Structures Laboratory",
    "credits": 1.5,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 3,
    "subject_code": "CS3381",
    "subject_name": "Object Oriented Programming Laboratory",
    "credits": 1.5,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 3,
    "subject_code": "CS3361",
    "subject_name": "Data Science Laboratory",
    "credits": 2,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 3,
    "subject_code": "GE3361",
    "subject_name": "Professional Development",
    "credits": 1,
    "category": "EEC"
},

# ==============================
# 2021 Regulation CSE Sem 4 Subjects
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 4,
    "subject_code": "CS3452",
    "subject_name": "Theory of Computation",
    "credits": 3,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 4,
    "subject_code": "CS3491",
    "subject_name": "Artificial Intelligence and Machine Learning",
    "credits": 4,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 4,
    "subject_code": "CS3492",
    "subject_name": "Database Management Systems",
    "credits": 3,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 4,
    "subject_code": "CS3401",
    "subject_name": "Algorithms",
    "credits": 4,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 4,
    "subject_code": "CS3451",
    "subject_name": "Introduction to Operating Systems",
    "credits": 3,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 4,
    "subject_code": "GE3451",
    "subject_name": "Environmental Sciences and Sustainability",
    "credits": 2,
    "category": "BSC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 4,
    "subject_code": "CS3461",
    "subject_name": "Operating Systems Laboratory",
    "credits": 1.5,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 4,
    "subject_code": "CS3481",
    "subject_name": "Database Management Systems Laboratory",
    "credits": 1.5,
    "category": "PCC"
},

# ==============================
# 2021 Regulation CSE Sem 5 Subjects
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 5,
    "subject_code": "CS3591",
    "subject_name": "Computer Networks",
    "credits": 4,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 5,
    "subject_code": "CS3501",
    "subject_name": "Compiler Design",
    "credits": 4,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 5,
    "subject_code": "CB3491",
    "subject_name": "Cryptography and Cyber Security",
    "credits": 3,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 5,
    "subject_code": "CS3551",
    "subject_name": "Distributed Computing",
    "credits": 3,
    "category": "PCC"
},

# ==============================
# 2021 Regulation CSE Sem 6 Subjects
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 6,
    "subject_code": "CCS356",
    "subject_name": "Object Oriented Software Engineering",
    "credits": 4,
    "category": "PCC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 6,
    "subject_code": "CS3691",
    "subject_name": "Embedded Systems and IoT",
    "credits": 4,
    "category": "PCC"
},

# ==============================
# 2021 Regulation CSE Sem 7 Subjects
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 7,
    "subject_code": "GE3791",
    "subject_name": "Human Values and Ethics",
    "credits": 2,
    "category": "HSMC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 7,
    "subject_code": "CS3711",
    "subject_name": "Summer Internship",
    "credits": 2,
    "category": "EEC"
},

# ==============================
# 2021 Regulation CSE Sem 8 Subjects
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 8,
    "subject_code": "CS3811",
    "subject_name": "Project Work / Internship",
    "credits": 10,
    "category": "EEC"
},

# ==============================
# 2021 Regulation CSE Professional Electives - Batch 1
# Vertical I - Data Science
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS346",
    "subject_name": "Exploratory Data Analysis",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS360",
    "subject_name": "Recommender Systems",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS355",
    "subject_name": "Neural Networks and Deep Learning",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS369",
    "subject_name": "Text and Speech Analysis",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCW331",
    "subject_name": "Business Analytics",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS349",
    "subject_name": "Image and Video Analytics",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS338",
    "subject_name": "Computer Vision",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS334",
    "subject_name": "Big Data Analytics",
    "credits": 3,
    "category": "PE"
},

# ==============================
# 2021 Regulation CSE Professional Electives - Batch 2
# Vertical II - Full Stack Development
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS375",
    "subject_name": "Web Technologies",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS332",
    "subject_name": "App Development",
    "credits": 3,
    "category": "PE"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS370",
    "subject_name": "UI and UX Design",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS366",
    "subject_name": "Software Testing and Automation",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS374",
    "subject_name": "Web Application Security",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS342",
    "subject_name": "DevOps",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS358",
    "subject_name": "Principles of Programming Languages",
    "credits": 3,
    "category": "PE"
},

# ==============================
# 2021 Regulation CSE Professional Electives - Batch 3
# Vertical III - Cloud Computing and Data Center Technologies
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS335",
    "subject_name": "Cloud Computing",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS372",
    "subject_name": "Virtualization",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS336",
    "subject_name": "Cloud Services Management",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS341",
    "subject_name": "Data Warehousing",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS367",
    "subject_name": "Storage Technologies",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS365",
    "subject_name": "Software Defined Networks",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS368",
    "subject_name": "Stream Processing",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS362",
    "subject_name": "Security and Privacy in Cloud",
    "credits": 3,
    "category": "PE"
},

# ==============================
# 2021 Regulation CSE Professional Electives - Batch 4
# Vertical IV - Cyber Security and Data Privacy
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS344",
    "subject_name": "Ethical Hacking",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS343",
    "subject_name": "Digital and Mobile Forensics",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS363",
    "subject_name": "Social Network Security",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS351",
    "subject_name": "Modern Cryptography",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CB3591",
    "subject_name": "Engineering Secure Software Systems",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS339",
    "subject_name": "Cryptocurrency and Blockchain Technologies",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS354",
    "subject_name": "Network Security",
    "credits": 3,
    "category": "PE"
},


# ==============================
# 2021 Regulation CSE Professional Electives - Batch 5
# Vertical V - Creative Media
# (Unique Subjects Only)
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS333",
    "subject_name": "Augmented Reality/Virtual Reality",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS352",
    "subject_name": "Multimedia and Animation",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS371",
    "subject_name": "Video Creation and Editing",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCW332",
    "subject_name": "Digital Marketing",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS373",
    "subject_name": "Visual Effects",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS347",
    "subject_name": "Game Development",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS353",
    "subject_name": "Multimedia Data Compression and Storage",
    "credits": 3,
    "category": "PE"
},

# ==============================
# 2021 Regulation CSE Professional Electives - Batch 6
# Vertical VI - Emerging Technologies
# (Unique Subjects Only)
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS361",
    "subject_name": "Robotic Process Automation",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS340",
    "subject_name": "Cyber Security",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS359",
    "subject_name": "Quantum Computing",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS331",
    "subject_name": "3D Printing and Design",
    "credits": 3,
    "category": "PE"
},

# ==============================
# 2021 Regulation CSE Professional Electives - Batch 7
# Vertical VII - Artificial Intelligence and Machine Learning
# (Unique Subjects Only)
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS350",
    "subject_name": "Knowledge Engineering",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS364",
    "subject_name": "Soft Computing",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS357",
    "subject_name": "Optimization Techniques",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS348",
    "subject_name": "Game Theory",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS337",
    "subject_name": "Cognitive Science",
    "credits": 3,
    "category": "PE"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CCS345",
    "subject_name": "Ethics And AI",
    "credits": 3,
    "category": "PE"
},

# ==============================
# 2021 Regulation CSE Mandatory Courses - I
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3081",
    "subject_name": "Introduction to Women and Gender Studies",
    "credits": 0,
    "category": "MC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3082",
    "subject_name": "Elements of Literature",
    "credits": 0,
    "category": "MC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3083",
    "subject_name": "Film Appreciation",
    "credits": 0,
    "category": "MC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3084",
    "subject_name": "Disaster Risk Reduction and Management",
    "credits": 0,
    "category": "MC"
},

# ==============================
# 2021 Regulation CSE Mandatory Courses - II
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3085",
    "subject_name": "Well Being with Traditional Practices - Yoga, Ayurveda and Siddha",
    "credits": 0,
    "category": "MC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3086",
    "subject_name": "History of Science and Technology in India",
    "credits": 0,
    "category": "MC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3087",
    "subject_name": "Political and Economic Thought for a Humane Society",
    "credits": 0,
    "category": "MC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3088",
    "subject_name": "State, Nation Building and Politics in India",
    "credits": 0,
    "category": "MC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3089",
    "subject_name": "Industrial Safety",
    "credits": 0,
    "category": "MC"
},

# ==================================================================================
# 2021 Regulation CSE - Naan Mudhalvan (Verified Courses) Still Many have to add
# ==================================================================================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "NM1001",
    "subject_name": "4G/5G Communications Network",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "NM1013",
    "subject_name": "Industrial IoT & Industry 4.0",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "NM1020",
    "subject_name": "UI / UX Design",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "NM1022",
    "subject_name": "Experience Based Project Learning",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB3001",
    "subject_name": "Naalayathiran – IBM Skills Build",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8011",
    "subject_name": "Industry 4.0",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8015",
    "subject_name": "Cyber Security",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8021",
    "subject_name": "Networking Essentials",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8026",
    "subject_name": "Robotic Process Automation Development",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8033",
    "subject_name": "Cisco Certified Network Associate - I (CCNA-I)",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8047",
    "subject_name": "Red Hat (Linux)",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8048",
    "subject_name": "ChatGPT",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8050",
    "subject_name": "DevOps",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8051",
    "subject_name": "Full Stack Development with Java",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8062",
    "subject_name": "Electric Vehicle Technology and Manufacturing",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8065",
    "subject_name": "Drone Basics, Design, Assembly, Test",
    "credits": 2,
    "category": "NM"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "SB8067",
    "subject_name": "Salesforce Developer",
    "credits": 2,
    "category": "NM"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "NM1015",
    "subject_name": "<Official Subject Name>",
    "credits": 2,
    "category": "NM"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "NM1117",
    "subject_name": "Full Stack with Java",
    "credits": 2,
    "category": "NM"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "NM1074",
    "subject_name": "Data Science",
    "credits": 2,
    "category": "NM"
},

# ==============================
# 2021 Regulation CSE - Mandatory Courses II
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3085",
    "subject_name": "Well Being with Traditional Practices - Yoga, Ayurveda and Siddha",
    "credits": 0,
    "category": "MC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3086",
    "subject_name": "History of Science and Technology in India",
    "credits": 0,
    "category": "MC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3087",
    "subject_name": "Political and Economic Thought for a Humane Society",
    "credits": 0,
    "category": "MC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3088",
    "subject_name": "State, Nation Building and Politics in India",
    "credits": 0,
    "category": "MC"
},
{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MX3089",
    "subject_name": "Industrial Safety",
    "credits": 0,
    "category": "MC"
},


# ==============================
# 2021 Regulation CSE Elective - Management Courses
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "GE3751",
    "subject_name": "Principles of Management",
    "credits": 3,
    "category": "HSMC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "GE3752",
    "subject_name": "Total Quality Management",
    "credits": 3,
    "category": "HSMC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "GE3753",
    "subject_name": "Engineering Economics and Financial Accounting",
    "credits": 3,
    "category": "HSMC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "GE3754",
    "subject_name": "Human Resource Management",
    "credits": 3,
    "category": "HSMC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "GE3755",
    "subject_name": "Knowledge Management",
    "credits": 3,
    "category": "HSMC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "GE3792",
    "subject_name": "Industrial Management",
    "credits": 3,
    "category": "HSMC"
},

# ==============================
# 2021 Regulation CSE Open Electives - II
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OIE352",
    "subject_name": "Resource Management Techniques",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMG351",
    "subject_name": "Fintech Regulation",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OFD351",
    "subject_name": "Holistic Nutrition",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "AI3021",
    "subject_name": "IT in Agricultural System",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEI352",
    "subject_name": "Introduction to Control Engineering",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OPY351",
    "subject_name": "Pharmaceutical Nanotechnology",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OAE351",
    "subject_name": "Aviation Management",
    "credits": 3,
    "category": "OEC"
},


# ==============================
# 2021 Regulation CSE Open Electives - I
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OAS351",
    "subject_name": "Space Science",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OIE351",
    "subject_name": "Introduction to Industrial Engineering",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OBT351",
    "subject_name": "Food, Nutrition and Health",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OCE351",
    "subject_name": "Environment and Social Impact Assessment",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEE351",
    "subject_name": "Renewable Energy System",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEI351",
    "subject_name": "Introduction to Industrial Instrumentation and Control",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMA351",
    "subject_name": "Graph Theory",
    "credits": 3,
    "category": "OEC"
},


# ==============================
# 2021 Regulation CSE Open Electives - III
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OHS351",
    "subject_name": "English for Competitive Examinations",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMG352",
    "subject_name": "NGOs and Sustainable Development",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMG353",
    "subject_name": "Democracy and Good Governance",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CME365",
    "subject_name": "Renewable Energy Technologies",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OME354",
    "subject_name": "Applied Design Thinking",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MF3003",
    "subject_name": "Reverse Engineering",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OPR351",
    "subject_name": "Sustainable Manufacturing",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "AU3791",
    "subject_name": "Electric and Hybrid Vehicles",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OAS352",
    "subject_name": "Space Engineering",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OIM351",
    "subject_name": "Industrial Management",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OIE354",
    "subject_name": "Quality Engineering",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OSF351",
    "subject_name": "Fire Safety Engineering",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OML351",
    "subject_name": "Introduction to Non-destructive Testing",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMR351",
    "subject_name": "Mechatronics",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "ORA351",
    "subject_name": "Foundation of Robotics",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OAE352",
    "subject_name": "Fundamentals of Aeronautical Engineering",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OGI351",
    "subject_name": "Remote Sensing Concepts",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OAI351",
    "subject_name": "Urban Agriculture",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEN351",
    "subject_name": "Drinking Water Supply and Treatment",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEE352",
    "subject_name": "Electric Vehicle Technology",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEI353",
    "subject_name": "Introduction to PLC Programming",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OCH351",
    "subject_name": "Nano Technology",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OCH352",
    "subject_name": "Functional Materials",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OFD352",
    "subject_name": "Traditional Indian Foods",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OFD353",
    "subject_name": "Introduction to Food Processing",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OPY352",
    "subject_name": "IPR for Pharma Industry",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OTT351",
    "subject_name": "Basics of Textile Finishing",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OTT352",
    "subject_name": "Industrial Engineering for Garment Industry",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OTT353",
    "subject_name": "Basics of Textile Manufacture",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OPE351",
    "subject_name": "Introduction to Petroleum Refining and Petrochemicals",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CPE334",
    "subject_name": "Energy Conservation and Management",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OPT351",
    "subject_name": "Basics of Plastics Processing",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEC351",
    "subject_name": "Signals and Systems",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEC352",
    "subject_name": "Fundamentals of Electronic Devices and Circuits",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CBM348",
    "subject_name": "Foundation Skills in Integrated Product Development",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CBM333",
    "subject_name": "Assistive Technology",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMA352",
    "subject_name": "Operations Research",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMA353",
    "subject_name": "Algebra and Number Theory",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMA354",
    "subject_name": "Linear Algebra",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OCE353",
    "subject_name": "Lean Concepts, Tools and Practices",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OBT352",
    "subject_name": "Basics of Microbial Technology",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OBT353",
    "subject_name": "Basics of Biomolecules",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OBT354",
    "subject_name": "Fundamentals of Cell and Molecular Biology",
    "credits": 3,
    "category": "OEC"
},

# ==============================
# 2021 Regulation CSE Open Electives - IV
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OHS352",
    "subject_name": "Project Report Writing",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMA355",
    "subject_name": "Advanced Numerical Methods",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMA356",
    "subject_name": "Random Processes",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMA357",
    "subject_name": "Queuing and Reliability Modelling",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMG354",
    "subject_name": "Production and Operations Management for Entrepreneurs",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMG355",
    "subject_name": "Multivariate Data Analysis",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OME352",
    "subject_name": "Additive Manufacturing",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CME343",
    "subject_name": "New Product Development",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OME355",
    "subject_name": "Industrial Design & Rapid Prototyping Techniques",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MF3010",
    "subject_name": "Micro and Precision Engineering",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMF354",
    "subject_name": "Cost Management of Engineering Projects",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "AU3002",
    "subject_name": "Batteries and Management System",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "AU3008",
    "subject_name": "Sensors and Actuators",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OAS353",
    "subject_name": "Space Vehicles",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OIM352",
    "subject_name": "Management Science",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OIM353",
    "subject_name": "Production Planning and Control",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OIE353",
    "subject_name": "Operations Management",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OSF352",
    "subject_name": "Industrial Hygiene",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OSF353",
    "subject_name": "Chemical Process Safety",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OML352",
    "subject_name": "Electrical, Electronic and Magnetic Materials",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OML353",
    "subject_name": "Nanomaterials and Applications",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMR352",
    "subject_name": "Hydraulics and Pneumatics",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMR353",
    "subject_name": "Sensors",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "ORA352",
    "subject_name": "Concepts in Mobile Robots",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "MV3501",
    "subject_name": "Marine Propulsion",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMV351",
    "subject_name": "Marine Merchant Vessels",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OMV352",
    "subject_name": "Elements of Marine Engineering",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CRA332",
    "subject_name": "Drone Technologies",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OGI352",
    "subject_name": "Geographical Information System",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OAI352",
    "subject_name": "Agriculture Entrepreneurship Development",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEN352",
    "subject_name": "Biodiversity Conservation",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEE353",
    "subject_name": "Introduction to Control Systems",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEI354",
    "subject_name": "Introduction to Industrial Automation Systems",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OCH353",
    "subject_name": "Energy Technology",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OCH354",
    "subject_name": "Surface Science",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OFD354",
    "subject_name": "Fundamentals of Food Engineering",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OFD355",
    "subject_name": "Food Safety and Quality Regulations",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OPY353",
    "subject_name": "Nutraceuticals",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OTT354",
    "subject_name": "Basics of Dyeing and Printing",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "FT3201",
    "subject_name": "Fibre Science",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OTT355",
    "subject_name": "Garment Manufacturing Technology",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OPE353",
    "subject_name": "Industrial Safety",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OPE354",
    "subject_name": "Unit Operations in Petro Chemical Industries",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OPT352",
    "subject_name": "Plastic Materials for Engineers",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OPT353",
    "subject_name": "Properties and Testing of Plastics",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OEC353",
    "subject_name": "VLSI Design",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CBM370",
    "subject_name": "Wearable Devices",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CBM356",
    "subject_name": "Medical Informatics",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OCE354",
    "subject_name": "Basics of Integrated Water Resources Management",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OBT355",
    "subject_name": "Biotechnology for Waste Management",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OBT356",
    "subject_name": "Lifestyle Diseases",
    "credits": 3,
    "category": "OEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "OBT357",
    "subject_name": "Biotechnology in Health Care",
    "credits": 3,
    "category": "OEC"
},

# ==============================
# 2021 Regulation CSE Minor Degree - Vertical 1
# Fintech and Block Chain
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG331",
    "subject_name": "Financial Management",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG332",
    "subject_name": "Fundamentals of Investment",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG333",
    "subject_name": "Banking, Financial Services and Insurance",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG334",
    "subject_name": "Introduction to Blockchain and its Applications",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG335",
    "subject_name": "Fintech Personal Finance and Payments",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG336",
    "subject_name": "Introduction to Fintech",
    "credits": 3,
    "category": "PEC"
},

# ==============================
# 2021 Regulation CSE Minor Degree - Vertical 2
# Entrepreneurship
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG337",
    "subject_name": "Foundations of Entrepreneurship",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG338",
    "subject_name": "Team Building & Leadership Management for Business",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG339",
    "subject_name": "Creativity & Innovation in Entrepreneurship",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG340",
    "subject_name": "Principles of Marketing Management For Business",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG341",
    "subject_name": "Human Resource Management for Entrepreneurs",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG342",
    "subject_name": "Financing New Business Ventures",
    "credits": 3,
    "category": "PEC"
},

# ==============================
# 2021 Regulation CSE Minor Degree - Vertical 3
# Public Administration
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG343",
    "subject_name": "Principles of Public Administration",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG344",
    "subject_name": "Constitution of India",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG345",
    "subject_name": "Public Personnel Administration",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG346",
    "subject_name": "Administrative Theories",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG347",
    "subject_name": "Indian Administrative System",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG348",
    "subject_name": "Public Policy Administration",
    "credits": 3,
    "category": "PEC"
},
# ==============================
# 2021 Regulation CSE Minor Degree - Vertical 4
# Business Data Analytics
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG349",
    "subject_name": "Statistics for Management",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG350",
    "subject_name": "Datamining For Business Intelligence",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG351",
    "subject_name": "Human Resource Analytics",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG352",
    "subject_name": "Marketing and Social Media Web Analytics",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG353",
    "subject_name": "Operation and Supply Chain Analytics",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CMG354",
    "subject_name": "Financial Analytics",
    "credits": 3,
    "category": "PEC"
},# ==============================
# 2021 Regulation CSE Minor Degree - Vertical 5
# Environment and Sustainability
# ==============================

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CES331",
    "subject_name": "Sustainable infrastructure Development",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CES332",
    "subject_name": "Sustainable Agriculture and Environmental Management",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CES333",
    "subject_name": "Sustainable Bio Materials",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CES334",
    "subject_name": "Materials for Energy Sustainability",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CES335",
    "subject_name": "Green Technology",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CES336",
    "subject_name": "Environmental Quality Monitoring and Analysis",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CES337",
    "subject_name": "Integrated Energy Planning for Sustainable Development",
    "credits": 3,
    "category": "PEC"
},

{
    "department": "CSE",
    "regulation": 2021,
    "semester": 0,
    "subject_code": "CES338",
    "subject_name": "Energy Efficiency for Sustainable Development",
    "credits": 3,
    "category": "PEC"
},
]

with app.app_context():

    existing_subjects = {
        subject.subject_code
        for subject in Subject.query.filter_by(
            department="CSE",
            regulation=2021
        ).all()
    }

    for item in subjects:
        if item["subject_code"] not in existing_subjects:
            db.session.add(Subject(**item))
            existing_subjects.add(item["subject_code"])

    db.session.commit()

print("Database populated successfully.\nTotal subjects in the database:", len(existing_subjects))