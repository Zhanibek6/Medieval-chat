import random
import re
import json


class Medieval:
	def __init__(self, data):
		self.data = data


	def printData(self):
		print(self.data)


	def translate(self, inp):
		result = inp.lower()

		result = self.single_words(result)

		result = self.prepend_and_append(result)

		result = self.change_tags(result)

		print(result)


	def single_words(self, inp):
		translation = inp

		data = self.data["single_replacements"]

		for item in data:
			translation = re.sub(rf"\b{item}\b", random.choice(data[item]), translation)
		return translation


	def prepend_and_append(self, inp):
		prep = self.data["prepended_words"]
		
		if "!" in inp:
			inp = inp.replace("!", "")
			appnd = self.punctuation(inp, "!")
		elif "?" in inp:
			inp = inp.replace("?", "")
			appnd = self.punctuation(inp, "?")
		else:
			appnd = self.data["appended_words"]
			appnd = " " + random.choice(appnd)
		
		
		randomPrep = random.choice(prep)

		return randomPrep.replace("\n", " ") + inp.replace("\n", " ") + appnd


	def punctuation(self, inp, ch):

		data = self.data["punctuation"]

		return random.choice(data[ch])


	def change_tags(self, inp):
		translation = inp
		data = self.data["change_tags"]
		for item in data:
			translation = translation.replace(item, random.choice(data[item]))

		return translation

def main():
	with open("dict.json", "r") as f:
		content = f.read()


	data = json.loads(content)
	medieval = Medieval(data)

	text = input("Enter your text: ")
	'''
	tests = [
		"I am testing this thing with a punctuation!",
		"Now I am testing it with another punctuation?",
		"Now here, it's just a text",
		"And some another text."
	]
	for text in tests:
	'''
	medieval.translate(text)


if __name__ == "__main__":
	main()

