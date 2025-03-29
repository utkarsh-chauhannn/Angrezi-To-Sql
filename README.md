## 🎯 **Angrezi-To-Sql**

**Angrezi-To-Sql** is a natural language to SQL converter that converts plain English queries into SQL commands and retrieves relevant results from a SQLite database.

---

## 📚 **Overview**

This project uses:
- **LangChain** with **LLaMA 3 (8B-8192)** model via **Groq API** to convert English queries to SQL.
- **Streamlit** for the frontend to allow users to interact with the database.
- **SQLite** as the database to store and query student information.

---

## 🚀 **Features**
- Converts natural language queries to SQL.
- Retrieves and displays results from the database.
- Provides error handling for invalid queries and database issues.

---

## 🛠️ **Tech Stack**
- **Python**: Backend logic and database interaction.
- **Streamlit**: Frontend to capture and display user queries and results.
- **SQLite**: Database to store student records.
- **LangChain** + **Groq API**: Converts English to SQL.

---

## 📄 **Project Structure**
/Angrezi-To-Sql
├── /app.py             # Main Streamlit application file
├── /database.py        # Script to create and populate the student database
├── /student.db         # SQLite database file containing student records
├── /README.md          # Documentation for the project
└── /requirements.txt   # List of required Python packages



