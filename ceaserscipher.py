def shift_cipher_encrypt(plaintext, shift):
  cipher_text = ""
  for char in plaintext:
    if ord(char) >= 97 and ord(char) <= 122:
      ascii_value = ord(char) + shift
      if ascii_value > 122:
        ascii_value -= 26
      cipher_text += chr(ascii_value)
    else:
        cipher_text += char

  return cipher_text

def shift_cipher_decrypt(cipher_text, shift):
  plaintext = ""
  for char in cipher_text:
    if ord(char) >= 97 and ord(char) <= 122:
      ascii_value = ord(char) - shift
      if ascii_value < 97:
        ascii_value += 26
      plaintext += chr(ascii_value)
    else:
        plaintext += char

  return plaintext
print("\n\n\n*****Welcome to the shift ceasers cipher program*****\n\n\n")
operation = input("Enter the operation: (e) for encrypt and (d) for decrypt ").lower()
text = input("Enter the text: ").lower()
shift = int(input("Enter the shift number: "))

if operation == "e":
 print(f" the ciper text is:  {shift_cipher_encrypt(text, shift)}")
elif operation == "d":
 print(f" the plain text is:  {shift_cipher_decrypt(text, shift)}")
else:
 print("Invalid operation")