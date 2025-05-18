# 🧑‍💼 Employee Compensation Forecasting Application

## 📌 Table of Contents

- [Objective](#-objective)
- [Tools & Technologies](#️-tools--technologies)
- [Dataset](#-dataset)
- [User Stories](#-user-stories)
- [Getting Started](#-getting-started)
  - [Prerequisites](#-prerequisites)
  - [Setup Instructions](#-setup-instructions)
  


## 📌 Objective

Design and build a basic Employee Compensation Forecasting Application for HR and business stakeholders. This Proof of Concept (PoC) demonstrates real-world HR analytics features, including compensation simulations and workforce distribution analysis.


## 🛠️ Tools & Technologies

- **Backend Database**: SQL Server (or any relational database)
- **Programming Language**: Python
- **Framework**: Flask
- **Frontend**: HTML, CSS, JavaScript (Optional)
- **Libraries**: `pandas`, `flask`, 

## 📂 Dataset

- Excel file containing sample employee data.
- Fields include: Employee Name, Role, Location, Experience, Compensation, Status.

## ✅ User Stories

1. **Filter and Display Active Employees by Role**:  
   - Filter by role, view average compensation by location, bar chart of compensation, toggle active/inactive.

2. **Group Employees by Years of Experience**:  
   - View count by experience ranges, group by location/role.

3. **Simulate Compensation Increments**:  
   - Input global increment and view updated compensation.

4. **Download Filtered Employee Data**:  
   - Export filtered data as CSV, reflecting any increments applied.

## 🚀 Getting Started

### Prerequisites

- Python installed on your system.
- SQL Server (or chosen relational database) set up.
- Required Python libraries installed:

  ```bash
  pip install -r flask pandas Flask-CORS

## Setup Instructions

1. Database setup
   - Install MYSQL software and create a root password
   - go to the location of the file and open terminal ![Screenshot (683)](https://github.com/user-attachments/assets/8db70d5b-1e13-4cd5-a868-6087d78ee0d9)


2. VSC Setup 
   
   - Open your project folder in VSC
   - Open the terminal inside VSC
   - Run your Flask application with the command
   -       python app.py

![Screenshot 2025-05-18 171050](https://github.com/user-attachments/assets/d5c14b92-9250-4966-ade8-10378ce828eb)
   
3. Running the Application
   - The Flask server will start on http://localhost:5000/ by default
   - open the frontend in your browser to interact
  
4. Uploading Employee Data via Postman
   - over the VSC install Postman as the extension and enter the URL
   - Send a POST request to:
   -     http://localhost:5000/upload/employee_data
   - Under the Body tab, select body, file upload and upload the Excel file containing employee data
	 
5. Using the Application
   
   -Use the UI or API endpoints to
   - Filter employees
   - View compensation charts
   - Simulate increments
   - Download filtered/exported CSV files
![Screenshot 2025-05-18 175908](https://github.com/user-attachments/assets/6dfa0f4e-7dcd-4ced-af70-ff72eb587e3d)


  


