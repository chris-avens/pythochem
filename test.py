import tkinter as tk
import main
import pandas as pd


class TkSetitSubclass(tk.__init__):
    def __init__(self, arg1, arg2):
        super().__init__(arg1, arg2)
        self._setit = None

    def method_setit(self):
        # Access the protected member directly
        self._setit = value


my_object = TkSetitSubclass(arg1, arg2)
my_object.method_setit()

# Read data from Excel file
data = pd.read_excel("Perry Tables.xlsx")  # ##

# Get list of unique quantities
quantities = data['Quantity'].unique()

# Create tkinter window
window = tk.Tk()

# Set window title
window.title("Unit Converter")

# Create label and dropdown menu for quantity
quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()
quantity_var = tk.StringVar(value=quantities[0])
quantity_dropdown = tk.OptionMenu(window, quantity_var, *quantities)
quantity_dropdown.pack()


# Define function to filter unit dropdowns based on selected quantity
def filter_units(*args):
    quantity = quantity_var.get()
    filtered_units = data[data['Quantity'] == quantity]['Customary or commonly used unit'].unique()
    initial_unit_dropdown['menu'].delete(0, 'end')
    for unit in filtered_units:
        initial_unit_dropdown['menu'].add_command(label=unit, command=tk._setit(initial_unit_var, unit))
    initial_unit_var.set(filtered_units[0])
    desired_unit_dropdown['menu'].delete(0, 'end')
    filtered_si_units = data[(data['Quantity'] == quantity) & (~data['SI unit'].isna())]['SI unit'].unique()
    filtered_alt_units = data[(data['Quantity'] == quantity) & (~data['Alternate SI unit'].isna())]['Alternate SI unit'].unique()
    filtered_units = list(set(filtered_si_units) | set(filtered_alt_units))
    for unit in filtered_units:
        desired_unit_dropdown['menu'].add_command(label=unit, command=tk._setit(desired_unit_var, unit))
    desired_unit_var.set(filtered_units[0])


# Create label and dropdown menu for initial unit
initial_unit_label = tk.Label(window, text="Initial Unit:")
initial_unit_label.pack()
initial_unit_var = tk.StringVar(value=data['Customary or commonly used unit'][0])
initial_unit_dropdown = tk.OptionMenu(window, initial_unit_var, *data['Customary or commonly used unit'].unique())
initial_unit_dropdown.pack()

# Create label and dropdown menu for desired unit
desired_unit_label = tk.Label(window, text="Desired Unit:")
desired_unit_label.pack()
desired_unit_var = tk.StringVar(value=data['SI unit'][0])
desired_unit_dropdown = tk.OptionMenu(window, desired_unit_var, *data['SI unit'].unique())
desired_unit_dropdown.pack()

# Create label and input box for magnitude
magnitude_label = tk.Label(window, text="Magnitude:")
magnitude_label.pack()
magnitude_var = tk.DoubleVar(value=0.0)
magnitude_entry = tk.Entry(window, textvariable=magnitude_var)
magnitude_entry.pack()


# Create button to perform unit conversion
convert_button = tk.Button(window,
                           text="Convert",
                           command=main.unit_convert(initial_unit=initial_unit_var.get(),
                                                     desired_unit=desired_unit_var.get(),
                                                     magnitude=magnitude_var.get()))
convert_button.pack()

# Create label to display result
result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var)
result_label.pack()

# Start tkinter event loop
window.mainloop()
