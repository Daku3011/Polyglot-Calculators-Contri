import tkinter as tk
from tkinter import messagebox

# This is a simple cooking converter app for Awesome-Calculators project on GitHub.
# It converts between various cooking units like cups, tablespoons, grams, etc.
class Converter:
    def __init__(self, root):
        self.root = root
        root.title("Cooking Converter")
        # Window minimum size (makes sure everything fits)
        root.minsize(200, 170)

        # These are the units and how many mL or g they are worth
        self.units = {
            "Milliliters (mL)": 1,
            "Liters (L)": 1000,
            "Grams (g)": 1,
            "Kilograms (kg)": 1000,
            "Teaspoons (tsp)": 4.93,
            "Tablespoons (tbsp)": 14.79,
            "Fluid Ounces (fl oz)": 29.57,
            "Cups (c)": 236.59,
            "Pints (pt)": 473.18,
            "Quarts (qt)": 946.35,
            "Gallons (gal)": 3785.41,
            "Ounces (oz)": 28.35,
            "Pounds (lb)": 453.59
        }

        # Make a list of unit names
        self.unit_names = list(self.units.keys())

        # Entry for value
        tk.Label(root, text="Value:").grid(row=0, column=0)
        self.value_entry = tk.Entry(root)
        self.value_entry.grid(row=0, column=1)

        # Dropdown for from unit
        tk.Label(root, text="From:").grid(row=1, column=0)
        self.from_var = tk.StringVar(root)
        self.from_var.set(self.unit_names[0])
        self.from_menu = tk.OptionMenu(root, self.from_var, *self.unit_names)
        self.from_menu.grid(row=1, column=1)

        # Dropdown for to unit
        tk.Label(root, text="To:").grid(row=2, column=0)
        self.to_var = tk.StringVar(root)
        self.to_var.set(self.unit_names[1])
        self.to_menu = tk.OptionMenu(root, self.to_var, *self.unit_names)
        self.to_menu.grid(row=2, column=1)

        # Button to convert
        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=2)

        # Label to show result
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=4, column=0, columnspan=2)

    def convert(self):
        # Try to get the value and units, show error if invalid.
        try:
            value = float(self.value_entry.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()
            # Get the rates
            from_rate = self.units[from_unit]
            to_rate = self.units[to_unit]
            # Convert to base (mL or g), then to target
            base = value * from_rate
            result = base / to_rate
            self.result_label.config(text=f"Result: {result:.4f} {to_unit}")
        except Exception:
            messagebox.showerror("Error", "Please enter a number and select units.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Converter(root)
    root.mainloop()
