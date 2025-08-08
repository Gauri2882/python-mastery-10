' Project: Language Translator Tool '

from googletrans import Translator
import pyttsx3
import tkinter as tk

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# initialize translator
translator = Translator()

def translate():
    text = input_text.get("1.0", tk.END).strip()
    target_lang = target_lang_var.get()
    if text:
        translated_text = translator.translate(text, dest = target_lang)
        output_text.config(state = "normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text.text)
        output_text.config(state = "disabled")
        speak(translated_text.text)

# create GUI window
root = tk.Tk()
root.title("Language Translator Tool")
root.geometry("400x400")

# input text area
input_text = tk.Text(root, height= 5, width= 40)
input_text.pack(pady= 10)

# label
label = tk.Label(root, text = "Choose target language from dropdown below")
label.pack(pady= 5)

# target langauge dropdown
target_lang_var = tk.StringVar(root)
target_lang_var.set("es") # default spanish

# language dropdown
lang_dropdown = tk.OptionMenu(root, target_lang_var, "es", "fr", "de", "zh", "ar", "ru")
lang_dropdown.pack()

# translate button
translate_button = tk.Button(root, text = "Translate", command= translate)
translate_button.pack(pady= 5)

# output text area
output_text = tk.Text(root, height= 5, width= 40, state= "disabled")
output_text.pack(pady= 10)

# run the application
root.mainloop()