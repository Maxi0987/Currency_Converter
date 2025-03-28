import tkinter as tk
from tkinter import ttk

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("500x400")
        self.root.minsize(300, 200)

        self.language = 'de'

        self.langbutton = tk.Button(root, text="Englisch", command=self.lang_change)
        self.langbutton.pack(pady=10)
        
        self.label = tk.Label(root, text="Wähle hier aus von welcher Währung du umrechnen willst:")
        self.label.pack(pady=10)

        self.askcombobox = ttk.Combobox(root, values=["EUR", "USD", "GBP", "JPY"])
        self.askcombobox.pack(pady=10)

        self.entry_label = tk.Label(root, text="Gib den Betrag ein:")
        self.entry_label.pack(pady=5)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        self.label2 = tk.Label(root, text="Wähle hier aus in welche Währung du umrechnen willst:")
        self.label2.pack(pady=10)

        self.askcombobox2 = ttk.Combobox(root, values=["EUR", "USD", "GBP", "JPY"])
        self.askcombobox2.pack(pady=10)

        self.button = tk.Button(root, text="Bestätigen", command=self.bestätigen)
        self.button.pack(pady=10)

        self.output_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.output_label.pack(pady=10)

    def lang_change(self):
        if self.language == 'de':
            self.language = 'en'
            self.langbutton.config(text="Deutsch")
        else:
            self.language = 'de'
            self.langbutton.config(text="Englisch")
        self.update_ui()

    def update_ui(self):
        if self.language == 'de':
            self.label.config(text="Wähle hier aus von welcher Währung du umrechnen willst:")
            self.entry_label.config(text="Gib den Betrag ein:")
            self.label2.config(text="Wähle hier aus in welche Währung du umrechnen willst:")
            self.button.config(text="Bestätigen")
            self.output_label.config(text="")
        else:
            self.label.config(text="Choose the currency to convert from:")
            self.entry_label.config(text="Enter amount:")
            self.label2.config(text="Choose the currency to convert to:")
            self.button.config(text="Confirm")
            self.output_label.config(text="")

    def bestätigen(self):
        try:
            betrag = float(self.entry.get())
        except ValueError:
            self.output_label.config(text="Bitte einen gültigen Betrag eingeben!" if self.language == 'de' else "Please enter a valid amount!")
            return

        waehrung1 = self.askcombobox.get()
        waehrung2 = self.askcombobox2.get()

        if waehrung1 == "EUR":
            betrag_in_euro = betrag
        elif waehrung1 == "USD":
            betrag_in_euro = betrag / 1.08
        elif waehrung1 == "GBP":
            betrag_in_euro = betrag / 0.83
        elif waehrung1 == "JPY":
            betrag_in_euro = betrag / 162.32
        else:
            self.output_label.config(text="Bitte eine gültige Währung auswählen!" if self.language == 'de' else "Please choose a valid currency!")
            return

        if waehrung2 == "EUR":
            ergebnis = betrag_in_euro
        elif waehrung2 == "USD":
            ergebnis = betrag_in_euro * 1.1
        elif waehrung2 == "GBP":
            ergebnis = betrag_in_euro * 0.83
        elif waehrung2 == "JPY":
            ergebnis = betrag_in_euro * 162.32
        else:
            self.output_label.config(text="Bitte eine gültige Zielwährung auswählen!" if self.language == 'de' else "Please choose a valid target currency!")
            return

        self.output_label.config(text=f"{betrag} {waehrung1} entsprechen {ergebnis:.2f} {waehrung2}" if self.language == 'de' else f"{betrag} {waehrung1} is {ergebnis:.2f} {waehrung2}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()
