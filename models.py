from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    department = db.Column(db.String(20), nullable=False)
    regulation = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)

    subject_code = db.Column(db.String(20), nullable=False)
    subject_name = db.Column(db.String(200), nullable=False)

    credits = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(20), nullable=True)

    __table_args__ = (
        db.UniqueConstraint(
            "department",
            "regulation",
            "subject_code",
            name="unique_subject"
        ),

        db.Index(
            "idx_dept_reg_sem",
            "department",
            "regulation",
            "semester"
        ),

        db.Index(
            "idx_dept_reg_code",
            "department",
            "regulation",
            "subject_code"
        ),
    )

    def __repr__(self):
        return (
            f"<Subject("
            f"{self.department}, "
            f"{self.regulation}, "
            f"Sem-{self.semester}, "
            f"{self.subject_code})>"
        )