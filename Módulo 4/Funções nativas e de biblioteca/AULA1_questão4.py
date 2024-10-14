from datetime import datetime

hoje = datetime.now()

data = hoje.strftime("%D/%m/%Y")
hora = hoje.strftime("%H:%M")

print("Data:", data)
print("Hora:", hora)