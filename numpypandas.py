import numpy as np  # NumPy kütüphanesini np olarak içe aktar
import pandas as pd  # Pandas kütüphanesini pd olarak içe aktar

# NumPy ile rastgele veri oluştur
np.random.seed(42)  # Rastgele sayıların tekrar üretilebilmesi için sabit bir tohum
yaş = np.random.randint(20, 40, 10)  # 20-40 arasında 10 rastgele yaş
maaş = np.random.randint(3000, 7000, 10)  # 3000-7000 arasında rastgele maaş

# Pandas ile DataFrame oluştur
data = pd.DataFrame({
    "Yaş": yaş,
    "Maaş": maaş
})

# Yaşı 30'dan büyük olanları filtrele
filtered_data = data[data["Yaş"] > 30]

# Ortalama maaşı hesapla
average_salary = np.mean(data["Maaş"])

print("Oluşturulan Veri Tablosu:")
print(data)
print("\nYaşı 30'dan büyük olanlar:")
print(filtered_data)
print("\nOrtalama Maaş:", average_salary)

#Son olarak, matplotlib ve seaborn ile görselleştirme yapalım.
import matplotlib.pyplot as plt
import seaborn as sns

# Veri çerçevesindeki maaşları yaşa göre görselleştir
sns.scatterplot(x="Yaş", y="Maaş", data=data)
plt.title("Yaş ve Maaş Arasındaki İlişki")
plt.xlabel("Yaş")
plt.ylabel("Maaş")
plt.show()
