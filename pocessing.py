# %% [markdown]
# # Разведочный анализ данных. Исследование и визуализация данных.

# %% [markdown]
# ## 1) Текстовое описание набора данных

# %% [markdown]
# # Импорт библиотек
# Импортируем библиотеки с помощью команды import. Как правило, все команды import размещают в первой ячейке ноутбука, но мы в этом примере будем подключать все библиотеки последовательно, по мере их использования.
# 
# 

# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline 
sns.set(style="ticks")

# %%
def load_data():
  data = pd.read_excel('./data/dataset.xlsx')
  return data

# %%
def basic_specs(data):
  print(data.head())

# %%
def main():
  data = load_data()
  basic_specs(data)

# %%
if __name__ == '__main__':
  main()
