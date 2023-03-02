import tkinter as tk
from tkinter import filedialog
import PyPDF2

point=">>> "

class PdfMergerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Botnen PDF Merger")
        self.master.geometry("350x400")
        
        
        self.add_label = tk.Label(self.master, text="Botnen PDF-merger")
        self.add_label.pack(side = tk.BOTTOM)
        

        # Create listbox to hold selected PDFs
        self.pdf_listbox = tk.Listbox(self.master, height=10, width=50)
        self.pdf_listbox.pack(pady=10)

        # Create buttons to add and remove PDFs from list
        self.add_button = tk.Button(self.master, text="Add PDF", command=self.add_pdf)
        self.add_button.pack(side=tk.LEFT, padx=10)
        self.remove_button = tk.Button(self.master, text="Remove PDF", command=self.remove_pdf)
        self.remove_button.pack(side=tk.LEFT)
       
        # Create entry widget for the output file name
        self.filename_entry = tk.Entry(self.master, width=30)
        self.filename_entry.pack(pady=10)

        # Create button to merge PDFs and save as new file
        self.merge_button = tk.Button(self.master, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=10)

    def add_pdf(self):
        # Ask user to select a PDF file
        filename = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if filename:
            # Add the filename to the listbox
            self.pdf_listbox.insert(tk.END, filename)

    def remove_pdf(self):
        # Remove selected PDF from the listbox
        selected_index = self.pdf_listbox.curselection()
        if selected_index:
            self.pdf_listbox.delete(selected_index)

    def merge_pdfs(self):
        # Get the output filename from the entry widget
        output_filename = self.filename_entry.get()

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Loop through the PDFs in the listbox and add them to the writer
        for i in range(self.pdf_listbox.size()):
            filename = self.pdf_listbox.get(i)
            pdf_reader = PyPDF2.PdfReader(open(filename, "rb"))
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

        # Write the merged PDF to a file
        with open(output_filename, "wb") as outfile:
            pdf_writer.write(outfile)

        # Clear the listbox and entry widget
        self.pdf_listbox.delete(0, tk.END)
        self.filename_entry.delete(0, tk.END)
        self.add_label = tk.Label(self.master, text="Succsess!")
        self.add_label.pack(side=tk.RIGHT, padx=10)
        print(f"{point}File created...\n{point}Filename: {output_filename}\n{point}Success!!!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PdfMergerApp(root)
    root.mainloop()
