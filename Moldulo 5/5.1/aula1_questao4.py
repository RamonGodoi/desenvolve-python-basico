from datetime import datetime

data_hora=datetime.now()

data=data_hora.strftime("%d/%m/%Y")
hora=data_hora.strftime("%H:%M")

print(f"Data: {data}")
print(f"Hora: {hora}")