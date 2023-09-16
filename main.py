from collections import namedtuple

# sorting function
def sorting(start_dictionary):
	dictionary = start_dictionary
	for lenght in range(1, len(dictionary)):
		for key in range(len(dictionary) - lenght):
			if dictionary[key][1] == None:
				break
			elif dictionary[key+1][1] == None:
				dictionary[key], dictionary[key+1] = dictionary[key+1], dictionary[key]
			elif dictionary[key][1] > dictionary[key+1][1]:
				dictionary[key], dictionary[key+1] = dictionary[key+1], dictionary[key]
	return dictionary
# sale
class sale():
	request_tuple = namedtuple('Request', 'Quantity Price')

	def __init__(self):
		self.sale_list = {}
		self.last_request_id = 0

	def get(self, request_id):
		return self.sale_list.get(int(request_id))

	def delete(self, request_id):
		del self.sale_list[int(request_id)]

	def view(self):
		checklist = sorting(self.sale_list)
		return [checklist[value] for value in checklist]

	def add(self, quantity, price):
		request_id = self.last_request_id
		if price == '' or price == 0:
			self.sale_list[request_id] = self.request_tuple(quantity, None)
		else:
			self.sale_list[request_id] = self.request_tuple(quantity, price)
		self.last_request_id += 1
		return request_id

# buy
class buy():
	request_tuple = namedtuple('Request', 'Quantity Price')

	def __init__(self):
		self.buy_list = {}
		self.last_request_id = 0

	def get(self, request_id):
		return self.buy_list.get(int(request_id))

	def delete(self, request_id):
		return self.buy_list.pop(int(request_id))

	def view(self):
		checklist = sorting(self.buy_list)
		return [checklist[value] for value in checklist]

	def add(self, quantity, price):
		request_id = self.last_request_id
		if price == '' or price == 0:
			self.buy_list[request_id] = self.request_tuple(quantity, None)
		else:
			self.buy_list[request_id] = self.request_tuple(quantity, price)
		self.last_request_id += 1
		return request_id