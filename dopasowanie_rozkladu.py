

import matplotlib
import matplotlib.pyplot as plt
import numpy as num
import scipy
import scipy.stats
import scipy.stats as stats



size = 100
x = scipy.arange(size)

# Generowanie danych
y = scipy.stats.beta.rvs(6, 2, size=size, random_state=40)*50

# Tworzenie histogramu
plt.figure(figsize=(20,10))
h = plt.hist(y, bins=range(101))

# Wybrane rrodzaje rozkładów
dist_names = ['alpha', 'beta', 'expon', 'norm']

for dist_name in dist_names:
    dist = getattr(scipy.stats, dist_name)
    param = dist.fit(y)
    pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1])*size
    plt.plot(pdf_fitted, label=dist_name)
    plt.xlim(0,100)
# Opis wykresu
plt.legend(loc='best')
plt.title("Histogram średniego czasu pracy bezawaryjnej")
plt.xlabel("Średni czas pracy bezawaryjnej")
plt.ylabel("Częstość")
plt.grid(True)
plt.show()
plt.savefig("wykres.png")