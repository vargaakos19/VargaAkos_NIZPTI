import module as module
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Varga Ákos – Cost Manager")
        self.frame_input = tk.Frame(root)
        self.frame_input.pack(padx=10, pady=10, fill="x")
        tk.Label(self.frame_input, text="Category").grid(row=0, column=0, sticky="w")
        tk.Label(self.frame_input, text="Amount (Ft)").grid(row=0, column=1, sticky="w")
        tk.Label(self.frame_input, text="Comment").grid(row=0, column=2, sticky="w")
        self.entry_cat = tk.Entry(self.frame_input)
        self.entry_cat.grid(row=1, column=0, padx=5, pady=5)
        self.entry_am = tk.Entry(self.frame_input)
        self.entry_am.grid(row=1, column=1, padx=5, pady=5)
        self.entry_com = tk.Entry(self.frame_input)
        self.entry_com.grid(row=1, column=2, padx=5, pady=5)
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(padx=10, pady=(0,10), fill="x")
        self.btn_add = tk.Button(self.frame_buttons, text="New cost", command=self.addto)
        self.btn_add.pack(side="left", padx=5)
        self.btn_delete = tk.Button(self.frame_buttons, text="Delete", command=self.delete)
        self.btn_delete.pack(side="left", padx=5)
        self.btn_all = tk.Button(self.frame_buttons, text="Total cost", command=self.show_all)
        self.btn_all.pack(side="left", padx=5)
        self.btn_save = tk.Button(self.frame_buttons, text="Save to file", command=self.save)
        self.btn_save.pack(side="left", padx=5)
        self.listbox = tk.Listbox(root, width=90, height=12)
        self.listbox.pack(padx=10, pady=(0,10), fill="both", expand=True)
        self.listbox.bind("<Double-Button-1>", self.open)
        self.status = tk.Label(root, text="Empty list", anchor="w")
        self.status.pack(fill="x", padx=10, pady=(0,10))
        self.refresh_list()

    def addto(self):
        cat = self.entry_cat.get().strip()
        am = self.entry_am.get().strip()
        com = self.entry_com.get().strip()
        if not cat:
            messagebox.showwarning("Error", "You need to enter a valid category!")
            return
        try:
            module.new_cost(cat, float(am), com)
        except Exception:
            messagebox.showwarning("Error", "Invalid amount!")
            return
        self.entry_cat.delete(0, "end")
        self.entry_am.delete(0, "end")
        self.entry_com.delete(0, "end")
        self.refresh_list()
        self.status.config(text="New cost added successfully!")

    def delete(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Information", "There is no item selected!")
            return
        index = sel[0]
        ok = module.delete_index(index)
        if ok:
            self.refresh_list()
            self.status.config(text="Cost deleted successfully!")
        else:
            messagebox.showerror("Error", "Delete failed!")

    def show_all(self):
        am = module.all_amount()
        messagebox.showinfo("Information", f"Total cost: {int(am)} Ft")

    def save(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="costs.txt")
        if not file:
            return
        module.save(file)
        self.status.config(text=f"Save completed: {file}")

    def open(self, event):
        sel = self.listbox.curselection()
        if not sel:
            return
        index = sel[0]
        item = module.costs[index]
        messagebox.showinfo("Cost details", str(item))

    def refresh_list(self):
        self.listbox.delete(0, "end")
        for s in module.get_list_strings():
            self.listbox.insert("end", s)
        cnt = len(module.costs)
        self.status.config(text=f"{cnt} cost")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()