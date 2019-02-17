import csv
from random import randrange
import pandas as pd
import numpy as np
from collections import Counter

def getData():
	item = []
	search_history = ['shirt', 'watch', 'wallet', 'shoes', 'belt', 'rice', 'sugar', 'skirt', 'sandal', 'heals', 'handbag', 'bagpack', 'pillow', 'teddy', 'suitcase', 'mobiles', 'laptop', 'fridge', 'desk', 'soda', 'hat', 'bangles', 'earrings', 'necklace', 'ring', 'shampoo', 'dates', 'cashew', 'juice', 'lays', 'maggi', 'keyboard']
	item_names = []
	print(len(item_names))
	for i in range(50):
		number = randrange(1,32)
		item.append(number)
		item_names.append(search_history[number])
	#print(item)

	df = pd.DataFrame(columns=['Item', 'Item_names'])
	df['Item'] = item
	df['Item_names'] = item_names
	df.to_csv('dataset.csv', mode ='w', index=False)

	print(df.head) 

def calculate_frequency():
	df = pd.read_csv('dataset.csv')
	new_frequency= []
	new_names= []
	new_items= []
	#print(df)
	items = df['Item'].tolist()
	item_names = df['Item_names'].tolist()

	item_list = dict(zip(items, item_names))
	print(item_list)

	frequency = Counter(items)
	print(frequency)

	for item in item_list:
		new_items.append(item)
		new_names.append(item_list[item])
		new_frequency.append(frequency[item])

	df = pd.DataFrame(columns=['Item', 'Item_names', 'Frequency'])
	df['Item'] = new_items
	df['Item_names'] = new_names
	df['Frequency'] = new_frequency
	df.to_csv('person.csv', mode ='w', index=False)

getData()
calculate_frequency()
