frase = 'X-DSPAM-Confidence:0.8475'

dobledot = frase.find(":")
num = frase[dobledot+1:]
fnum = float(num)
print(fnum)