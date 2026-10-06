secret_number = "22"
guess = ""

while guess != secret_number:
    guess = input("Mera secret number guess karo (1 se 10):")

    if guess == secret_number:
       print("Mubarak ho Gagan bhai ! Aap jeet gaye !")
    else:
       print("Galti ! Fir se koshish kar.")
