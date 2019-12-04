import function as f
import tkinter as tk


def encrypter(message, key):
    output.delete('1.0', tk.END)
    forward = 0
    backward = len(message) - 1
    for i in message:
        for j in key:
            val1, val2 = 0, 0
            binVal = f.decToBin_8bit(ord(i))

            if binVal[0] == '1':
                val1 += 8
            if binVal[1] == '1':
                val1 += 4
            if binVal[2] == '1':
                val1 += 2
            if binVal[3] == '1':
                val1 += 1

            if binVal[4] == '1':
                val2 += 8
            if binVal[5] == '1':
                val2 += 4
            if binVal[6] == '1':
                val2 += 2
            if binVal[7] == '1':
                val2 += 1

            i = chr(ord(j) ^ f.binToDec(f.permutation(f.TwoCharToBin(f.substitution(val1), f.substitution(val2)))))

        if ord(i) < 33:
            k = ord(i) + 256
            i = chr(k)

        if 126 < ord(i) < 161:
            k = ord(i) + 162
            i = chr(k)
        message = message[:forward] + i + message[:backward]
        forward += 1
        backward -= 1
    label['text'] = 'Encrypted Message'
    output.insert(1.0, message)


def decrypt(message, key):
    output.delete('1.0', tk.END)
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
            binary = f.reversePermutation(f.decToBin_8bit(ord(i) ^ ord(key[pos])))
            i = chr(f.binToDec(f.decToBin_4Bit(f.reverseSubstitution(f.binToDec_4Bit(binary[0:4]))) + f.decToBin_4Bit(
                f.reverseSubstitution(f.binToDec_4Bit(binary[4:8])))))
            pos -= 1
        message = message[:forward] + i + message[:backward]
        forward += 1
        backward -= 1
    label['text'] = 'Decrypted Message'
    output.insert(1.0, message)


root = tk.Tk()
canvas = tk.Canvas(root, height=250, width=600)

label1 = tk.Label(canvas, text='Message Encrypter')

messageLable = tk.Label(canvas, text='Message: ')
keyLabel = tk.Label(canvas, text='Key: ')

messageEntry = tk.Entry(canvas, width=55)
KeyEntry = tk.Entry(canvas, width=55)

label2 = tk.Label(canvas, text='OutPut ↓')

label = tk.Label(canvas, text='Encrypted Message')
output = tk.Text(canvas, height=1, width=55, borderwidth=1)


encryptButton = tk.Button(canvas, text='Encrypt', command=lambda: encrypter(messageEntry.get(), KeyEntry.get()))
decryptButton = tk.Button(canvas, text='Decrypt', command=lambda: decrypt(messageEntry.get(), KeyEntry.get()))


label1.place(y=1, relx=0.4)
messageLable.place(x=3, y=50, anchor='w')
keyLabel.place(x=3, y=80, anchor='w')

messageEntry.place(x=150, y=40)
KeyEntry.place(x=150, y=70)

label2.place(y=125, relx=0.45)

label.place(x=3, y=170, anchor='w')

output.place(x=150, y=160)

encryptButton.place(x=350, y=200)
decryptButton.place(x=450, y=200)

canvas.pack()
root.mainloop()

