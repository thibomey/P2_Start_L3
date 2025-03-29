import pikepdf
from tqdm import tqdm

passwords = []
for wachtwoord in open("woorden.txt"):
    passwords.append(wachtwoord.strip())

for i in tqdm(range(len (passwords))):
    try:
        pikepdf.open("INV-1007-protected.pdf", password= passwords[i])
        print("correct password is: ", passwords[i])
        break
    except pikepdf._core.PasswordError:
        continue
        #print("fout wachtwoord")