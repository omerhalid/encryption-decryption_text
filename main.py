import tkinter as tk
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Use the key to create a Fernet cipher object
cipher = Fernet(key)

# Create the main window
window = tk.Tk()
window.title("Cryptographic Message Translator")

# Create a label and text entry field for the message
message_label = tk.Label(text="Message:")
message_entry = tk.Entry(width=50, font=("Arial", 12))


# Create a function to encrypt the message
def encrypt_message():
    # Read the message from the text entry field
    message = message_entry.get()

    # Convert the message to bytes
    message_bytes = message.encode()

    # Encrypt the message
    encrypted_message = cipher.encrypt(message_bytes)

    # Convert the encrypted message to a string
    encrypted_message_str = encrypted_message.decode()

    # Display the encrypted message in a text widget
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0", encrypted_message_str)


# Create a function to decrypt the message
def decrypt_message():
    # Read the message from the text entry field
    message = message_entry.get()

    # Convert the message to bytes
    message_bytes = message.encode()

    # Decrypt the message
    decrypted_message = cipher.decrypt(message_bytes)

    # Convert the decrypted message to a string
    decrypted_message_str = decrypted_message.decode()
    # Display the decrypted message in a text widget
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0", decrypted_message_str)

# Create buttons to encrypt and decrypt the message
encrypt_button = tk.Button(text="Encrypt", command=encrypt_message)
decrypt_button = tk.Button(text="Decrypt", command=decrypt_message)

# Create a text widget to display the result
result_text = tk.Text(width=80, height=10)

# Add the widgets to the window
message_label.pack()
message_entry.pack()
encrypt_button.pack()
decrypt_button.pack()
result_text.pack()

# Run the main loop
window.mainloop()
