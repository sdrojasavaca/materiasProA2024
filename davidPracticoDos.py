userText = input("Ingrese un a eleccion texto: ")
userTextAmount, amountA, amountE, amountI, amountO, amountU, amountConsonant, amountVowels= 0
for i in userText:
    userTextAmount +=1
    if i == "a" or "A" or "e" or "E" or "i" or "I" or "o" or "O" or "u" or "U":
        amountVowels+=1
        if i == "a" or "A":
            amountA += 1
        elif i == "e" or "E":
            amountE += 1
        elif i == "i" or "I":
            amountI += 1
        elif i == "o" or "O":
            amountO += 1
        elif i == "u" or "U":
            amountU += 1
    else:
        amountConsonant +=1
if userTextAmount>1:
    if amountVowels >0 and amountConsonant>0:
        print (f"La cantidad de letras de su texto son: {userTextAmount},la cantidad de consonantes son {amountConsonant} y la cantidad de vocales son {amountVowels}, las cuales {amountA} son la letra: A, {amountE} son la letra: E, {amountI} son la letra: I, {amountO} son la letra: O y {amountU} son la letra: U.")
    elif amountConsonant>0 and amountVowels==0:
        print(f"Su texto tiene {userTextAmount} letras, {amountConsonant} y no tiene vocales")
    elif amountConsonant==0 and amountVowels>0:
        print (f"La cantidad de letras de su texto son: {userTextAmount},sin consonantes y la cantidad de vocales son {amountVowels}, las cuales {amountA} son la letra: A, {amountE} son la letra: E, {amountI} son la letra: I, {amountO} son la letra: O y {amountU} son la letra: U.")
    else:
        print (f"Su texto no tiene vocales ni consonantes")
else:
    print("su texto no tiene caracteres")