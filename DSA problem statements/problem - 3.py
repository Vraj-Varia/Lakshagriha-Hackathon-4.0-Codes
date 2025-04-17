import tkinter as tk
from tkinter import messagebox
import string

ENGLISH_WORDS = {
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for',
    'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by',
    'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one',
    'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about',
    'who', 'get', 'which', 'go', 'me', 'can', 'just', 'now', 'your', 'like',
    'no', 'then', 'how', 'other', 'when', 'could', 'our', 'more', 'than', 'them',
    'was', 'is', 'am', 'are', 'were', 'been', 'has', 'had', 'did', 'some', 'any',
    'read', 'mystery', 'ashes', 'dust', 'can', 'you', 'what', 'this'
}

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def break_caesar_cipher(ciphertext):
    best_shift = 0
    max_real_words = 0
    best_decryption = ""

    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        words = decrypted.lower().translate(str.maketrans('', '', string.punctuation)).split()
        real_words = sum(1 for word in words if word in ENGLISH_WORDS)
        if real_words > max_real_words:
            max_real_words = real_words
            best_shift = shift
            best_decryption = decrypted

    certainty = (max_real_words / len(best_decryption.split())) * 100 if best_decryption else 0
    return best_shift, round(certainty, 2), best_decryption

def perform_action():
    option = option_var.get()
    text = input_text.get("1.0", tk.END).strip()
    shift = shift_var.get()
    if not text:
        messagebox.showerror("Error", "Please enter some text.")
        return

    if option == "Encrypt":
        result = caesar_encrypt(text, shift)
    elif option == "Decrypt":
        result = caesar_decrypt(text, shift)
    else:
        shift, confidence, result = break_caesar_cipher(text)
        result = f"Shift: {shift}\nConfidence: {confidence}%\nDecrypted: {result}"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher GUI")
root.geometry("600x400")

option_var = tk.StringVar(value="Encrypt")
shift_var = tk.IntVar(value=0)

frame = tk.Frame(root)
frame.pack(pady=10)

options = ["Encrypt", "Decrypt", "Break Cipher"]
tk.OptionMenu(frame, option_var, *options).pack(side=tk.LEFT, padx=10)
tk.Label(frame, text="Shift:").pack(side=tk.LEFT)
tk.Entry(frame, textvariable=shift_var, width=5).pack(side=tk.LEFT)

tk.Label(root, text="Input Text:").pack()
input_text = tk.Text(root, height=5)
input_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

tk.Button(root, text="Run", command=perform_action).pack(pady=10)

tk.Label(root, text="Output:").pack()
output_text = tk.Text(root, height=5)
output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

root.mainloop()