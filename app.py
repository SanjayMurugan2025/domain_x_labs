import streamlit as st

# Title
st.title("📋 Student Registration Form")

# Initialize student list in session state
if "students" not in st.session_state:
    st.session_state.students = []

# Form inputs
st.subheader("Enter Student Details")

name = st.text_input("Student Name")
age = st.number_input("Student Age", min_value=1, max_value=150)
grade = st.selectbox("Grade/Class", ["6", "7", "8", "9", "10", "11", "12"])
school = st.text_input("School Name")

# Submit button
if st.button("Add Student"):
    if name and school:
        st.session_state.students.append({
            "Name": name,
            "Age": age,
            "Grade": grade,
            "School": school
        })
        st.success(f"Added {name} successfully!")
    else:
        st.error("Name and School are required!")

st.divider()

# Display student list if any
if st.session_state.students:
    st.subheader("📊 Registered Students")
    st.table(st.session_state.students)
else:
    st.info("No students registered yet.")
