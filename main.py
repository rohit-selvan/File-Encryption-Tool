import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

class FileEncryptionTool(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Encryption & Decryption Tool")
        self.geometry("600x400")
        self.configure(bg="#e8f4f8")  # Light blue background
        self.key = Fernet.generate_key()  # Generate a new encryption key
        self.cipher = Fernet(self.key)
        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self, text="File Encryption & Decryption Tool", font=("Verdana", 20, "bold"), bg="#e8f4f8", fg="#2c3e50").pack(pady=20)
        
        # Encrypt Button
        tk.Button(self, text="Encrypt File", command=self.encrypt_file, font=("Verdana", 14), bg="#3498db", fg="white", width=15).pack(pady=10)
        
        # Decrypt Button
        tk.Button(self, text="Decrypt File", command=self.decrypt_file, font=("Verdana", 14), bg="#2ecc71", fg="white", width=15).pack(pady=10)
        
        # Display Encryption Key
        tk.Button(self, text="Show Encryption Key", command=self.show_key, font=("Verdana", 12), bg="#f39c12", fg="white", width=20).pack(pady=10)
    
    def encrypt_file(self):
        file_path = filedialog.askopenfilename(title="Select File to Encrypt")
        if not file_path:
            return
        try:
            with open(file_path, "rb") as file:
                file_data = file.read()
            encrypted_data = self.cipher.encrypt(file_data)
            with open(file_path + ".enc", "wb") as file:
                file.write(encrypted_data)
            messagebox.showinfo("Success", f"File encrypted successfully!\nEncrypted file: {file_path}.enc")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def decrypt_file(self):
        file_path = filedialog.askopenfilename(title="Select File to Decrypt", filetypes=[("Encrypted Files", "*.enc")])
        if not file_path:
            return
        try:
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = self.cipher.decrypt(encrypted_data)
            original_file_path = file_path.replace(".enc", "_decrypted")
            with open(original_file_path, "wb") as file:
                file.write(decrypted_data)
            messagebox.showinfo("Success", f"File decrypted successfully!\nDecrypted file: {original_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def show_key(self):
        messagebox.showinfo("Encryption Key", f"Your encryption key is:\n{self.key.decode()}")

if __name__ == "__main__":
    app = FileEncryptionTool()
    app.mainloop()
