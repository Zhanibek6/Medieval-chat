import random
import re
import json


class Medieval:
	def __init__(self, data):
		self.data = data


	def printData(self):
		print(self.data)


	def translate(self, inp):
		outStr = inp.lower()

		outStr = self.single_words(outStr)

		outStr = self.prepend_and_append(outStr)

		outStr = self.change_tags(outStr)

		print(outStr)


	def single_words(self, inp):
		transl = inp

		data = self.data["single_replacements"]

		for item in data:
			transl = re.sub(rf"\b{item}\b", random.choice(data[item]), transl)
			#transl = transl.replace(f" {item} ", random.choice(data[item]))
		return transl


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
		
		
		randPrep = random.choice(prep)

		return randPrep.replace("\n", " ") + inp.replace("\n", " ") + appnd


	def punctuation(self, inp, ch):

		data = self.data["punctuation"]

		return random.choice(data[ch])


	def change_tags(self, inp):
		transl = inp
		data = self.data["change_tags"]
		for item in data:
			transl = transl.replace(item, random.choice(data[item]))

		return transl

def main():
	with open("dict.json", "r") as f:
		content = f.read()


	data = json.loads(content)
	med = Medieval(data)

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
	med.translate(text)


if __name__ == "__main__":
	main()

