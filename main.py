from collections import namedtuple

# sale
class sale():
	request_list = namedtuple('list', 'Quantity Price')

	def __init__(self):
		self.sale_list = {}
		self.last_request_id = 0

	def add(self, quantity, price):
		request_id = self.last_request_id
		self.sale_list[request_id] = self.request_list(quantity, price)
		self.last_request_id += 1
		return request_id

	def get(self, request_id):
		return self.sale_list.get(int(request_id), 'Заявок с таким id нет')

	def delete(self, request_id):
		del self.sale_list[request_id]

	def view(self):
		clean_sale_list = []
		for key in self.sale_list:
			clean_sale_list.append(self.sale_list[key])

		return clean_sale_list

# buy
class buy():
	request_list = namedtuple('list', 'Quantity Price')

	def __init__(self):
		self.buy_list = {}
		self.last_request_id = 0

	def add(self, quantity, price):
		request_id = self.last_request_id
		self.buy_list[request_id] = self.request_list(quantity, price)
		self.last_request_id += 1
		return request_id

	def get(self, request_id):
		return self.buy_list.get(request_id)

	def delete(self, request_id):
		return self.buy_list.pop(request_id)

	def view(self):
		clean_buy_list = []
		for key in self.buy_list:
			clean_buy_list.append(self.buy_list[key])

		return clean_buy_list
