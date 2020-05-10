import function as f
import tkinter as tk
#successfully commited

def encrypter(message, key):
    output_text.delete('1.0', tk.END)
    forward = 0
    backward = len(message) - 1
    for i in message:
        for j in key:
            val1, val2 = 0, 0
            bin_val = f.dec_to_bin_8bit(ord(i))

            if bin_val[0] == '1':
                val1 += 8
            if bin_val[1] == '1':
                val1 += 4
            if bin_val[2] == '1':
                val1 += 2
            if bin_val[3] == '1':
                val1 += 1

            if bin_val[4] == '1':
                val2 += 8
            if bin_val[5] == '1':
                val2 += 4
            if bin_val[6] == '1':
                val2 += 2
            if bin_val[7] == '1':
                val2 += 1

            i = chr(ord(j) ^ f.bin_to_dec(f.permutation(f.two_char_to_bin(f.substitution(val1), f.substitution(val2)))))

        if ord(i) < 33:
            k = ord(i) + 256
            i = chr(k)

        if 126 < ord(i) < 161:
            k = ord(i) + 162
            i = chr(k)
        message = message[:forward] + i + message[:backward]
        forward += 1
        backward -= 1
    label['text'] = 'Encrypted\nMessage'
    output_text.insert(1.0, message)


def decrypt(message, key):
    output_text.delete('1.0', tk.END)
    forward = 0
    backward = len(message) - 1
    for i in message:
        pos = len(key) - 1
        if 256 <= ord(i) <= 288:
            k = ord(i) - 256
            i = chr(k)

        if 289 <= ord(i) <= 322:
            k = ord(i) - 162
            i = chr(k)

        for j in key:
            binary = f.reverse_permutation(f.dec_to_bin_8bit(ord(i) ^ ord(key[pos])))
            i = chr(f.bin_to_dec(f.dec_to_bin_4bit(f.reverse_substitution(f.bin_to_dec_4bit(binary[0:4]))) + f.dec_to_bin_4bit(
                f.reverse_substitution(f.bin_to_dec_4bit(binary[4:8])))))
            pos -= 1
        message = message[:forward] + i + message[:backward]
        forward += 1
        backward -= 1
    label['text'] = 'Decrypted\nMessage'
    output_text.insert(1.0, message)


root = tk.Tk()

canvas = tk.Canvas(root, height=250, width=600)
head_label = tk.Label(canvas, text='Message Encrypter', font=('verdana', 20))
message_label = tk.Label(canvas, text='Message: ', font=('verdana', 15))
key_label = tk.Label(canvas, text='Key: ', font=('verdana', 15))
message_entry = tk.Entry(canvas, width=55, font=('verdana', 15))
key_entry = tk.Entry(canvas, width=55, font=('verdana', 15))
output_label = tk.Label(canvas, text='OutPut ↓', font=('verdana', 15))
label = tk.Label(canvas, text='Encrypted\nMessage', font=('verdana', 15))
output_text = tk.Text(canvas, height=1, width=55, borderwidth=1, font=('verdana', 15))
encrypt_button = tk.Button(canvas, text='Encrypt', font=('verdana', 15), command=lambda: encrypter(message_entry.get(), key_entry.get()))
decrypt_button = tk.Button(canvas, text='Decrypt', font=('verdana', 15), command=lambda: decrypt(message_entry.get(), key_entry.get()))


canvas.pack()
head_label.place(y=1, relx=0.4)
message_label.place(x=3, y=50, anchor='w')
key_label.place(x=3, y=80, anchor='w')
message_entry.place(x=150, y=40)
key_entry.place(x=150, y=70)
output_label.place(y=125, relx=0.45)
label.place(x=3, y=170, anchor='w')
output_text.place(x=150, y=160)
encrypt_button.place(x=350, y=200)
decrypt_button.place(x=450, y=200)

root.mainloop()

