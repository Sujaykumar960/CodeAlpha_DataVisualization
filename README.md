# 📊 Data Visualization Project – CodeAlpha Internship Task 2

This is a Python-based interactive data visualization tool built as part of my CodeAlpha internship. It allows users to load Excel data, apply filters to specific columns, and generate various types of charts (bar, line, pie, area) using `matplotlib`.

---

## 💡 Features
- 📥 Load any `.xlsx` Excel file
- 🎯 Filter rows based on user-selected column values
- 📊 Generate grouped charts using:
  - Bar / Column
  - Line
  - Pie
  - Area
- 👨‍💻 Works interactively via terminal input
- ✅ Easy to use and extend for new datasets

---

## 🛠 Technologies Used
- Python 3.x
- pandas
- matplotlib
- openpyxl (for reading Excel files)

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sujaykumar960/CodeAlpha_DataVisualization.git
cd CodeAlpha_DataVisualization

2️⃣ Install Required Libraries : 
pip install pandas matplotlib openpyxl

3️⃣ Run the Script :
python DataVisualization.py

4️⃣ Follow the Interactive Prompts :
-> Enter Excel file path
-> Choose columns to filter
-> Select chart type (bar, line, pie, area)
->Choose X-axis and Y-axis for the graph

📁 Sample Dataset Preview of first 5 rows : 
| Student ID | Name    | Age | Gender | Department | Semester | GPA  | Attendance (%) |
| ---------- | ------- | --- | ------ | ---------- | -------- | ---- | -------------- |
| S1001      | Anamika | 18  | Female | ME         | 5        | 9.88 | 78.1           |
| S1002      | Rahul   | 17  | Male   | CSE        | 2        | 5.22 | 62.1           |
| S1003      | Sakshi  | 17  | Female | CSE        | 1        | 8.19 | 94.2           |
| S1004      | Aniket  | 17  | Male   | ME         | 1        | 8.37 | 71.1           |
| S1005      | Anidrew | 21  | Male   | CE         | 3        | 8.42 | 81.4           |

🧪 Sample Output (Multiple Examples)

🔹 Example 1: GPA by Student Name (Filtered by Gender = Female)
Console Input:
Bar Chart Output:

🔹 Example 2: GPA by Student ID (Filtered by Department + Semester)
Filtered Departments: CSE, CE, ECE
Filtered Semesters: 5, 2, 1, 3, 7
Console Input:
Bar Chart Output:


📌 Pro Tips
Ensure your Excel file has valid headers :
-> You can use any column as filter criteria.
-> You can use categorical or numeric columns as X-axis.
-> Y-axis must be a numeric column (like GPA or Attendance).

🔗 GitHub Repository
👉 https://github.com/Sujaykumar960/CodeAlpha_DataVisualization

🙌 Acknowledgement
-> This project is built as part of the CodeAlpha Internship Program – Task 2 (Data Visualization).

⭐ Feedback & Contributions
Feel free to fork this repo, suggest improvements, or raise issues.
I’d love to connect with more developers and learners! 🚀

