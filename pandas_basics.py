import pandas as pd

data = {"Ad": ["Ali", "Ayşe"], "Yaş": [25, 30]}
df = pd.DataFrame(data)  # Pandas veri çerçevesi oluşturur
print(df)

#Eğer pandas'ı import etmezsen, DataFrame gibi araçları kullanamazsın ve yine NameError alırsın.

import pandas as pd

# Bir veri tablosu (DataFrame) oluştur
data = {
    "Ad": ["Ali", "Ayşe", "Mehmet", "Fatma"],
    "Yaş": [25, 30, 22, 28],
    "Meslek": ["Mühendis", "Doktor", "Avukat", "Öğretmen"]
}
df = pd.DataFrame(data)

# Yaşı 25'ten büyük olan kişileri filtrele
filtered_df = df[df["Yaş"] > 25]

# Yeni bir sütun ekle: Maaş (tahmini değerlerle)
df["Maaş"] = [5000, 7000, 4000, 6000]

print("Orijinal Veri Tablosu:")
print(df)
print("\nYaşı 25'ten büyük olanlar:")
print(filtered_df)
