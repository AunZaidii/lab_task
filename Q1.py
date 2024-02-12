import pyodbc
from tkinter import Tk, Label, Button, Listbox, Entry, Toplevel, messagebox

class DatabaseViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Viewer, Inserter, and Deleter")

        # Connect to MS Access database
        connection_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/hp/Documents/School Management System.accdb;'
        self.connection = pyodbc.connect(connection_str)
        self.cursor = self.connection.cursor()

        # GUI components
        self.label = Label(root, text="Employee Data", font=("Helvetica", 16))
        self.label.pack()

        # Listbox to display data
        self.listbox = Listbox(root, width=40, height=10, font=("Helvetica", 12))
        self.listbox.pack(pady=10)

        # Buttons
        self.insert_button = Button(root, text="Insert Data", command=self.show_insert_window, width=15, height=2)
        self.insert_button.pack(padx=10)

        self.delete_button = Button(root, text="Delete Data", command=self.show_delete_window, width=15, height=2)
        self.delete_button.pack(padx=10)

        # Display initial data
        self.display_data()

    def display_data(self):
        # Clear existing data
        self.listbox.delete(0, 'end')

        # Fetch data from the database
        self.cursor.execute("SELECT * FROM Employees")
        employees = self.cursor.fetchall()

        # Display data in the Listbox
        for employee in employees:
            self.listbox.insert('end', f"{employee.ID} | {employee.Name} | {employee.Salary}")

    def show_insert_window(self):
        insert_window = Toplevel(self.root)
        insert_window.title("Insert Data")

        # Entry fields
        id_label = Label(insert_window, text="ID:")
        id_label.grid(row=0, column=0, padx=10, pady=5)
        id_entry = Entry(insert_window)
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        name_label = Label(insert_window, text="Name:")
        name_label.grid(row=1, column=0, padx=10, pady=5)
        name_entry = Entry(insert_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        salary_label = Label(insert_window, text="Salary:")
        salary_label.grid(row=2, column=0, padx=10, pady=5)
        salary_entry = Entry(insert_window)
        salary_entry.grid(row=2, column=1, padx=10, pady=5)

        # Button to add data
        add_button = Button(insert_window, text="Add Data", command=lambda: self.add_data(id_entry.get(), name_entry.get(), salary_entry.get(), insert_window))
        add_button.grid(row=3, columnspan=2, pady=10)

    def add_data(self, id, name, salary, insert_window):
        try:
            # Insert data into the database
            query = f"INSERT INTO Employees (ID, Name, Salary) VALUES ({id}, '{name}', {salary})"
            self.cursor.execute(query)
            self.connection.commit()

            # Display updated data
            self.display_data()

            # Close the insert window
            insert_window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error adding data: {str(e)}")

    def show_delete_window(self):
        delete_window = Toplevel(self.root)
        delete_window.title("Delete Data")

        # Listbox to display names
        names_listbox = Listbox(delete_window, selectmode="single", width=40, height=10, font=("Helvetica", 12))
        names_listbox.pack(pady=10)

        # Fetch names from the database
        self.cursor.execute("SELECT Name FROM Employees")
        names = self.cursor.fetchall()

        # Display names in the Listbox
        for name in names:
            names_listbox.insert('end', name.Name)

        # Button to remove data
        remove_button = Button(delete_window, text="Remove Data", command=lambda: self.remove_data(names_listbox.get(names_listbox.curselection()), delete_window))
        remove_button.pack(pady=10)

    def remove_data(self, selected_name, delete_window):
        try:
            # Delete data from the database
            query = f"DELETE FROM Employees WHERE Name = '{selected_name[0]}'"
            self.cursor.execute(query)
            self.connection.commit()

            # Display updated data
            self.display_data()

            # Close the delete window
            delete_window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error removing data: {str(e)}")


if __name__ == "__main__":
    root = Tk()
    app = DatabaseViewer(root)
    root.mainloop()
