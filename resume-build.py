import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF


def generate_resume():
    # Collect data from fields
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = text_address.get("1.0", tk.END).strip()
    education = text_education.get("1.0", tk.END).strip()
    experience = text_experience.get("1.0", tk.END).strip()
    skills = text_skills.get("1.0", tk.END).strip()

    if not name or not email or not phone:
        messagebox.showwarning("Missing Information", "Name, Email, and Phone are mandatory!")
        return

    # Create a PDF resume
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add content to the PDF
    pdf.cell(200, 10, txt="Resume", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt="Address:", ln=True)
    pdf.multi_cell(0, 10, txt=address)
    pdf.ln(5)
    pdf.cell(200, 10, txt="Education:", ln=True)
    pdf.multi_cell(0, 10, txt=education)
    pdf.ln(5)
    pdf.cell(200, 10, txt="Experience:", ln=True)
    pdf.multi_cell(0, 10, txt=experience)
    pdf.ln(5)
    pdf.cell(200, 10, txt="Skills:", ln=True)
    pdf.multi_cell(0, 10, txt=skills)

    # Save the PDF
    pdf_file = f"{name.replace(' ', '_')}_Resume.pdf"
    pdf.output(pdf_file)
    messagebox.showinfo("Success", f"Resume saved as {pdf_file}")


# GUI Design
root = tk.Tk()
root.title("Resume Builder")
root.geometry("400x600")

# Labels and Entry widgets
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=50)
entry_name.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root, width=50)
entry_email.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root, width=50)
entry_phone.pack()

tk.Label(root, text="Address:").pack()
text_address = tk.Text(root, width=50, height=4)
text_address.pack()

tk.Label(root, text="Education:").pack()
text_education = tk.Text(root, width=50, height=4)
text_education.pack()

tk.Label(root, text="Experience:").pack()
text_experience = tk.Text(root, width=50, height=4)
text_experience.pack()

tk.Label(root, text="Skills:").pack()
text_skills = tk.Text(root, width=50, height=4)
text_skills.pack()

# Generate Resume Button
btn_generate = tk.Button(root, text="Generate Resume", command=generate_resume)
btn_generate.pack(pady=10)

root.mainloop()
