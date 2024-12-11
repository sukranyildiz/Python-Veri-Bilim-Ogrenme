#import numpy as np  # NumPy kütüphanesi projeye dahil edilir.
#Bu satır sayesinde artık numpy içindeki fonksiyonlara (örneğin, np.array()) erişebiliriz.  - array:sıralamak
#as Kullanımı as anahtar kelimesi, kütüphaneye kısa bir takma ad (alias) vermemizi sağlar.
#Bu komut, numpy kütüphanesini projeye np adıyla dahil eder. Artık numpy.array() yerine sadece np.array() yazabiliriz.
# Bu, yazımı kolaylaştırır ve kodu daha okunabilir hale getirir.
import numpy as np

array = np.array([1, 2, 3, 4])  # NumPy dizisi oluşturur
print(array)

#numpy olmadan bu işlemi yapmaya çalışırsak Python, NameError verecektir. Çünkü numpy işlevlerini tanımaz.

# NUMPY DE DİZİLER ÜZERİNDE İŞLEM YAPMA #

import numpy as np

# NumPy ile rastgele bir dizi (array) oluştur
array = np.array([1, 2, 3, 4, 5])

# Her elemana 2 ekle
array_plus_2 = array + 2

# Dizinin ortalamasını ve toplamını bul
average = np.mean(array)
total = np.sum(array)

# Diziyi ters çevir
reversed_array = array[::-1]

print("Orijinal Dizi:", array)
print("Her elemana 2 eklenmiş hali:", array_plus_2)
print("Ortalama:", average)
print("Toplam:", total)
print("Ters çevrilmiş dizi:", reversed_array)
