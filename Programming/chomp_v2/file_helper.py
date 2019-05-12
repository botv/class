import json


class FileHelper:
	@staticmethod
	def save(data, path):
		with open(path, 'w') as f:
			json.dump(data, f)

	@staticmethod
	def load(path):
		with open(path, 'r') as f:
			data = json.load(f)
			return data
