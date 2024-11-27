import tkinter as tk
from tkinter import messagebox, filedialog

def generate_resume():
    # Collect user inputs
    name = name_var.get()
    email = email_var.get()
    phone = phone_var.get()
    skills = skills_text.get("1.0", "end").strip()
    experience = experience_text.get("1.0", "end").strip()
    education = education_text.get("1.0", "end").strip()

    if not name or not email or not phone:
        messagebox.showerror("Error", "Please fill in all required fields!")
        return

    # Format resume
    resume_content = f"""
    Resume
    =======
    Name: {name}
    Email: {email}
    Phone: {phone}

    Skills:
    {skills}

    Experience:
    {experience}

    Education:
    {education}
    """
    
    # Save resume to a file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(resume_content)
        messagebox.showinfo("Success", "Resume saved successfully!")

# Tkinter GUI setup
root = tk.Tk()
root.title("Resume Builder")
root.geometry("500x600")

# Input Fields
name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()

tk.Label(root, text="Name:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, pady=5, padx=5)

tk.Label(root, text="Email:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
tk.Entry(root, textvariable=email_var).grid(row=1, column=1, pady=5, padx=5)

tk.Label(root, text="Phone:").grid(row=2, column=0, pady=5, padx=5, sticky="w")
tk.Entry(root, textvariable=phone_var).grid(row=2, column=1, pady=5, padx=5)

tk.Label(root, text="Skills:").grid(row=3, column=0, pady=5, padx=5, sticky="nw")
skills_text = tk.Text(root, height=5, width=30)
skills_text.grid(row=3, column=1, pady=5, padx=5)

tk.Label(root, text="Experience:").grid(row=4, column=0, pady=5, padx=5, sticky="nw")
experience_text = tk.Text(root, height=5, width=30)
experience_text.grid(row=4, column=1, pady=5, padx=5)

tk.Label(root, text="Education:").grid(row=5, column=0, pady=5, padx=5, sticky="nw")
education_text = tk.Text(root, height=5, width=30)
education_text.grid(row=5, column=1, pady=5, padx=5)

# Buttons
tk.Button(root, text="Generate Resume", command=generate_resume).grid(row=6, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
