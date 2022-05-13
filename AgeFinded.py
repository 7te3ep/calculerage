from datetime import datetime 

maintenant = datetime.now()
anne = maintenant.year
userAge = int(input('Quelle est ton anné de naissance ?'))
print("Ton age est : ",int(anne)-userAge, "ans")
