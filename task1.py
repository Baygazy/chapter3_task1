text = [i for i in input("Введите что хотите: ") if i.isalnum() and not i.isnumeric()]
big = [i for i in text if i.isupper()]
low = [i for i in text if i.islower()]
dlina_all = len(text)
dlina_big = len(big)
dlina_low = len(low)
procent_big = 100 / dlina_all * dlina_big
procent_low = 100 / dlina_all * dlina_low
print(round(procent_big, 2), "% Заглавные")
print(round(procent_low, 2), "% прописные")
