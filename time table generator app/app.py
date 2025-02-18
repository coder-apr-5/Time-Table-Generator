




import streamlit as st
from fpdf import FPDF

# Streamlit App UI
st.title("Class Timetable Generator")
st.write("Generate and manage class schedules effortlessly.")

# Input fields for timetable generation
teachers_input = st.text_input("Enter the names of teachers (comma-separated)")
subjects_input = st.text_input("Enter the subjects (comma-separated)")
slots_input = st.text_input("Enter the available slots (comma-separated)")

# Function to generate a simple timetable
def generate_timetable(teachers, subjects, slots):
    """
    Generate a basic timetable by assigning teachers to subjects and slots.
    """
    timetable = []
    for i in range(min(len(teachers), len(subjects), len(slots))):
        timetable.append(f"Slot: {slots[i]} | Subject: {subjects[i]} | Teacher: {teachers[i]}")
    
    if len(timetable) == 0:
        timetable.append("No timetable could be generated. Ensure there are enough teachers, subjects, and slots.")
    
    return "\n".join(timetable)

# Function to save timetable as PDF
def save_timetable_as_pdf(timetable, filename="timetable.pdf"):
    """
    Save the generated timetable as a PDF.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Class Timetable", ln=True, align="C")
    pdf.ln(10)  # Add some space
    
    for line in timetable.split("\n"):
        pdf.cell(200, 10, txt=line, ln=True)
    
    pdf.output(filename)
    return filename

# Generate timetable based on input
if st.button("Generate Timetable"):
    if teachers_input and subjects_input and slots_input:
        teachers = [t.strip() for t in teachers_input.split(",")]
        subjects = [s.strip() for s in subjects_input.split(",")]
        slots = [s.strip() for s in slots_input.split(",")]

        st.info("Generating timetable...")
        timetable = generate_timetable(teachers, subjects, slots)
        
        st.success("Timetable generated successfully!")
        st.text_area("Generated Timetable", timetable, height=300)

        # Option to download the timetable as a PDF
        if st.button("Download PDF"):
            pdf_file = save_timetable_as_pdf(timetable)
            with open(pdf_file, "rb") as file:
                st.download_button("Download Timetable PDF", file, file_name="timetable.pdf")
    else:
        st.warning("Please fill all fields to generate the timetable.")
