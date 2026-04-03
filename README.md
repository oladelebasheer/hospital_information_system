# 📘 Hospital Information System (HIS) – README

## 📌 Project Title

**Hospital Information System (HIS)**

---

## 📖 Description

The Hospital Information System (HIS) is a web-based application developed using Django. It is designed to manage hospital operations efficiently by digitizing patient records, medical history, billing, and reporting.

The system replaces manual record-keeping with a centralized database, improving data accessibility, accuracy, and security.

---

## 🎯 Objectives

* To automate hospital record management
* To improve patient data accessibility
* To reduce data redundancy and errors
* To enhance report generation and decision-making
* To ensure secure storage of medical information

---

## 🏥 Key Features

### 👤 Patient Management

* Register new patients
* View patient details
* Update patient information

### 👨‍⚕️ Doctor Management

* Add and manage doctors
* Assign doctors to patients

### 📋 Medical Records

* Create medical records
* View detailed patient history
* Edit and update records
* Delete records

### 💰 Billing System

* Generate bills
* Record payments
* Track payment status

### 📊 Reports

* Generate system reports
* View summaries of hospital activities

---

## 🛠️ Technologies Used

### Backend

* Python
* Django Framework

### Frontend

* HTML
* CSS
* Bootstrap

### Database

* PostgreSQL (or SQLite for development)

---

## 📂 Project Structure

```
hospital_information_system/
│
├── accounts/        # User authentication and roles
├── patients/        # Patient management
├── doctors/         # Doctor management
├── records/         # Medical records (CRUD)
├── billing/         # Billing and payments
├── reports/         # Reporting module
│
├── templates/       # HTML templates
│   └── records/
│       ├── record_list.html
│       ├── record_detail.html
│       ├── add_record.html
│       ├── edit_record.html
│       └── delete_record.html
│
├── static/          # CSS, JS, images
├── config/          # Project settings
├── manage.py
```

---

## ⚙️ Installation Guide

### Step 1: Clone the Project

```bash
git clone <repository-url>
cd hospital_information_system
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Environment

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure Database

Update your database settings in:

```python
config/settings.py
```

---

### Step 6: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 7: Create Superuser

```bash
python manage.py createsuperuser
```

---

### Step 8: Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Default Login

Use the superuser credentials you created to access the admin dashboard.

---

## 📸 System Modules Screens

* Login Page
* Dashboard
* Patient Registration
* Medical Records
* Billing Interface
* Reports

---

## ⚠️ Limitations

* Requires internet or local server
* Role-based permissions may need further enhancement
* Limited advanced analytics

---

## 🚀 Future Enhancements

* Integration with mobile app
* Advanced reporting with charts
* Appointment scheduling system
* SMS/Email notifications
* AI-based diagnosis support

---

## 📚 Author

**B. A. Yusuf**
Department of Computer Science

---

## 📄 License

This project is for academic and research purposes only.

---

## 🙏 Acknowledgements

Special thanks to lecturers, supervisors, and contributors who provided guidance and support during the development of this system.

---

## 💡 Final Note

This system demonstrates how modern web technologies can improve healthcare service delivery through automation, data integrity, and accessibility.


Just tell me.

