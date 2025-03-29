import os
import sqlite3
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def get_sql_query(user_query):
    groq_sys_prompt = ChatPromptTemplate.from_template("""
                    You are an expert in converting English questions to SQL query!
                    The SQL database has the name STUDENT and has the following columns - NAME, COURSE, 
                    SECTION and MARKS. For example, 
                    Example 1 - How many entries of records are present?, 
                        the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
                    Example 2 - Tell me all the students studying in Data Science COURSE?, 
                        the SQL command will be something like this SELECT * FROM STUDENT 
                        where COURSE="Data Science"; 
                    also the sql code should not have ``` in beginning or end and sql word in output.
                    Now convert the following question in English to a valid SQL Query: {user_query}. 
                    No preamble, only valid SQL please
                                                       """)
    model = "llama3-8b-8192"
    groq_api_key = os.environ.get("GROQ_API_KEY")

    if not groq_api_key:
        st.error("GROQ API key is missing. Please set it in your environment variables.")
        return None

    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name=model
    )

    chain = groq_sys_prompt | llm | StrOutputParser()
    response = chain.invoke({"user_query": user_query})
    return response


def return_sql_response(sql_query):
    database = os.path.join(os.path.dirname(__file__), "student.db")

    if not os.path.exists(database):
        st.error(f"Database file '{database}' not found. Please check the file path.")
        return []

    try:
        with sqlite3.connect(database) as conn:
            result = conn.execute(sql_query).fetchall()
            return result
    except Exception as e:
        st.error(f"Error executing SQL query: {e}")
        return []


def main():
    st.set_page_config(page_title="Text To SQL")
    st.header("Talk to your Database!")

    user_query = st.text_input("Input your question:")
    submit = st.button("Enter")

    if submit:
        if not user_query.strip():
            st.error("Please enter a valid question.")
            return

        sql_query = get_sql_query(user_query)

        if not sql_query:
            st.error("Failed to generate a valid SQL query. Please try again with a different question.")
            return

        st.write(f"Generated SQL Query: `{sql_query}`")

        retrieved_data = return_sql_response(sql_query)

        if retrieved_data:
            st.subheader(f"Results from the database for query: `{sql_query}`")
            st.dataframe(retrieved_data, use_container_width=True)
        else:
            st.warning("No data found or an error occurred while executing the query.")


if __name__ == '__main__':
    main()
