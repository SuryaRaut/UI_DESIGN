# Sample Tkinter GUI
# Author: Shakir James


from functools import partial
from tkinter import StringVar, Tk, N, W, E, S
from tkinter import ttk

from ciphers import affine, caesar, transposition, vigenere

# interface: cipher.translate(key, message, mode)
CIPHERS = {
    'Caesar cipher': caesar,
    'Transposition cipher': transposition,
    'Affine cipher': affine,
    'Vigenere cipher':  vigenere
}


def translate(key, message, mode, cipher, translated):
    try:
        cipher_translate = CIPHERS[cipher.get()].translate
        text = cipher_translate(key.get(), message.get(), mode.get())
    except KeyError:
        text = 'Unknown cipher {}.'.format(cipher.get())
    except AttributeError:
        text = 'Cipher {} missing translate().'.format(cipher.get())
    translated.set('{}ed text:\n{}'.format(mode.get().title(), text))


def main():
    root = Tk()
    root.title('Ciphers')

    key = StringVar()
    message = StringVar()
    mode = StringVar()
    cipher = StringVar()
    translated = StringVar()
    command = partial(translate, key, message, mode, cipher, translated)

    mainframe = ttk.Frame(root, padding='3 3 12 12')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Message").grid(column=1, row=1, sticky=W)
    message_entry = ttk.Entry(mainframe, width=20, textvariable=message)
    message_entry.grid(column=1, row=2, sticky=(W, E))

    ttk.Label(mainframe, text="Key").grid(column=3, row=1, sticky=W)
    key_entry = ttk.Entry(mainframe, width=10, textvariable=key)
    key_entry.grid(column=3, row=2, sticky=(W, E))

    ttk.Label(mainframe, text="Cipher").grid(column=1, row=3, sticky=W)
    cipher_combo = ttk.Combobox(mainframe, width=16, textvariable=cipher)
    cipher_combo['values'] = (
        'Caesar cipher', 'Transposition cipher', 'Affine cipher',
        'Vigenere cipher'
    )
    cipher_combo.set('Caesar cipher')
    cipher_combo.grid(column=1, row=4, sticky=W)

    ttk.Label(mainframe, text="Mode").grid(column=3, row=3, sticky=W)
    encrypt_radio = ttk.Radiobutton(
        mainframe, text='Encrypt', variable=mode, value='encrypt',
    )
    encrypt_radio.grid(column=3, row=4, sticky=W)
    decrypt_radio = ttk.Radiobutton(
        mainframe, text='Decrypt', variable=mode, value='decrypt'
    )
    decrypt_radio.grid(column=4, row=4, sticky=W)
    mode.set('encrypt')

    # Button
    translate_button = ttk.Button(
        mainframe, text='Translate', command=command
    )
    translate_button.grid(column=1, row=5, sticky=W)

    transalted_label = ttk.Label(mainframe, textvariable=translated)
    transalted_label.grid(column=1, row=6, sticky=(W, E))

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    message_entry.focus()
    root.bind('<Return>', command)
    root.mainloop()

if __name__ == '__main__':
    main()
