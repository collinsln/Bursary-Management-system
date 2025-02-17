#from app import db
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy import Enum

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    __Tablename__='user'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    id_no = db.Column(db.Integer, nullable=False)

class StudentDetails(db.Model):
    __tablename__ = 'studentdetails'  
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    contact_phone_number = db.Column(db.String(20), nullable=False)
    photo_url = db.Column(db.String(500))
    gender = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    place_of_birth = db.Column(db.String(100), nullable=False)
    village = db.Column(db.String(100), nullable=False)
    ward = db.Column(db.String(100), nullable=False)
    constituency = db.Column(db.String(100), nullable=False)
    institution_name = db.Column(db.String(100), nullable=False)
    institution_code = db.Column(db.String(100), nullable=False)
    campus = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    mode_of_study = db.Column(db.String(100), nullable=False)
    expected_completion_year = db.Column(db.Date, nullable=False)
    # experimental additions
    verified = db.Column(db.Boolean, default=False)
    approved = db.Column(db.Boolean, default=False)
    needy_score = db.Column(db.Integer)


class ParentGuardian(db.Model):
    __Tablename__='parentguardian'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    student_id = db.Column(UUID(as_uuid=True), db.ForeignKey('studentdetails.id'), nullable=False)
    parent = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    main_income_source = db.Column(db.String(100), nullable=False)
    other_income_source = db.Column(db.String(100))
    employed = db.Column(Enum('yes', 'no', 'retired', name='employementstatus'), nullable=False)

class EducationFundingHistory(db.Model):
    __Tablename__='educationfundinghistory'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    student_id = db.Column(UUID(as_uuid=True), db.ForeignKey('studentdetails.id'), nullable=False)
    institution_type = db.Column(db.String(100), nullable=False)
    institution_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    funding_source = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(500))

class Siblings(db.Model):
    __Tablename__='siblings'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    student_id = db.Column(UUID(as_uuid=True), db.ForeignKey('studentdetails.id'), nullable=False)
    relationship = db.Column(db.String(100), nullable=False)
    institution = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(100), nullable=False)
    total_annual_fees = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Float, nullable=False)

class Bursary(db.Model):
    __Tablename__='bursary'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    fund_amount = db.Column(db.Float, nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.String(500))
    #expermental additions
    awarded = db.Column(db.Boolean, default=False)
    rejected = db.Column(db.Boolean, default=False)


class Beneficiary(db.Model):
    __Tablename__='beneficiary'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    student_id = db.Column(UUID(as_uuid=True), db.ForeignKey('studentdetails.id'), nullable=False)
    bursary_id = db.Column(UUID(as_uuid=True), db.ForeignKey('bursary.id'), nullable=False)
    amount_allocated = db.Column(db.Float, nullable=False)
    date_allocated = db.Column(db.Date, nullable=False)
    disbursed = db.Column(db.Boolean, nullable=False)
    date_disbursed = db.Column(db.Date)

class DeclarationDocuments(db.Model):
    __Tablename__='declarationdocuments'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    student_id = db.Column(UUID(as_uuid=True), db.ForeignKey('studentdetails.id'), nullable=False)
    individual_declaration = db.Column(db.String(500), nullable=False)
    parent_declaration = db.Column(db.String(500), nullable=False)
    religious_leader_declaration = db.Column(db.String(500), nullable=False)
    local_authority_declaration = db.Column(db.String(500), nullable=False)
