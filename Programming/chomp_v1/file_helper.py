import json


class FileHelper:
	@staticmethod
	def save(data, path):
		with open(path, 'w') as f:
			json.dump(data, f)

	@staticmethod
	def load():
		with open('strings.json') as f:
			data = json.load(f)
			return data
