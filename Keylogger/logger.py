from pynput import keyboard
from datetime import datetime

word_buffer = []
words = []
report_path = "report.txt"

def complete_word():
    if word_buffer:
        word = ''.join(word_buffer)
        words.append(word)
        word_buffer.clear()

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None and key.char.isalnum():
            word_buffer.append(key.char)
        elif key in [keyboard.Key.space, keyboard.Key.enter]:
            complete_word()
        elif key == keyboard.Key.backspace and word_buffer:
            word_buffer.pop()
    except:
        pass

def save_report():
    complete_word()
    with open(report_path, "w") as f:
        f.write("Words typed:\n")
        for word in words:
            f.write(word + "\n")
        f.write(f"\nTotal words: {len(words)}\nGenerated at: {datetime.now()}\n")

def start_logger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    print("Logging globally. Press Ctrl+C in this terminal to stop.")
    try:
        while listener.is_alive():
            listener.join(1)
    except KeyboardInterrupt:
        print("Stopping logger...")
    finally:
        save_report()
        print("Report saved.")

if __name__ == "__main__":
    start_logger()
