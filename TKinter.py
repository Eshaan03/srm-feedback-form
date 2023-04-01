import tkinter as tk
import re

# Define regular expressions for email and password validation
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PASSWORD_REGEX = r'^[a-zA-Z0-9._%+-]{2,}$'

# Define a function to handle form submission
def submit_form():
    email = email_entry.get()
    password = password_entry.get()
    num_subjects = num_subjects_entry.get()
    num_lab_subjects = num_lab_subjects_entry.get()

    # Validate input values
    errors = []
    if not re.match(EMAIL_REGEX, email):
        errors.append("Invalid email address")
    if not re.match(PASSWORD_REGEX, password):
        errors.append("Invalid password")
    if not num_subjects.isdigit() or int(num_subjects) < 0:
        errors.append("Number of subjects must be a positive integer")
    if not num_lab_subjects.isdigit() or int(num_lab_subjects) < 0:
        errors.append("Number of lab subjects must be a positive integer")

    # Show error messages or do something with the input values
    if errors:
        error_label.config(text="\n".join(errors))
    else:
        error_label.config(text="")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Number of subjects: {num_subjects}")
        print(f"Number of lab subjects: {num_lab_subjects}")

# Create a new Tkinter window
root = tk.Tk()
root.title("Input Form")
root.configure(bg="#f2f2f2")

# Create a label and entry for email id
email_label = tk.Label(root, text="Email:", bg="#f2f2f2", fg="#666666", font=("Helvetica", 12))
email_label.grid(row=0, column=0, padx=10, pady=10)
email_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
email_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a label and entry for password
password_label = tk.Label(root, text="Password:", bg="#f2f2f2", fg="#666666", font=("Helvetica", 12))
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*", width=30, font=("Helvetica", 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a label and entry for number theory of subjects
num_subjects_label = tk.Label(root, text="Number of Theory subjects:", bg="#f2f2f2", fg="#666666", font=("Helvetica", 12))
num_subjects_label.grid(row=2, column=0, padx=10, pady=10)
num_subjects_entry = tk.Entry(root, width=5, font=("Helvetica", 12))
num_subjects_entry.grid(row=2, column=1, padx=10, pady=10)
num_subjects_entry.config(validate="key", validatecommand=(root.register(lambda s: s.isdigit()), '%S'))

# Create a label and entry for number of lab subjects
num_lab_subjects_label = tk.Label(root, text="Number of lab subjects:", bg="#f2f2f2", fg="#666666", font=("Helvetica", 12))
num_lab_subjects_label.grid(row=3, column=0, padx=10, pady=10)
num_lab_subjects_entry = tk.Entry(root, width=5, font=("Helvetica", 12))
num_lab_subjects_entry.grid(row=3, column=1, padx=10, pady=10)
num_lab_subjects_entry.config(validate="key", validatecommand=(root.register(lambda s: s.isdigit()), '%S'))

# Create a button to submit the form

submit_button = tk.Button(root, text="Submit", bg="#4CAF50", fg="white", font=("Helvetica", 12), command=submit_form)
submit_button.grid(row=4, column=1, padx=10, pady=20)

# Create a label to show error messages
error_label = tk.Label(root, text="", fg="red", font=("Helvetica", 12))
error_label.grid(row=5, column=1, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
