import bs4, requests
import os

class Parser:
	def __init__(self, url, num_sim = 80):
		self.url = url
		self.num_sim = num_sim

	def parse(self):
		body = requests.get(url)
		soup = bs4.BeautifulSoup(body.text, "html.parser")
		self.all_p = soup.find_all("p")

	def split_text(self):
		text = ""
		for x in self.all_p:
			text = text + x.get_text() + '\n'
		self.list_text = []
		self.list_text += text.split()

	def create_file(self):
		root_path = "D:/"
		new_list = self.url.split('/')
		new_list.pop(0)
		new_list.pop(0)
		new_list.pop(len(new_list)-1)
		a = new_list.pop(len(new_list)-1)
		for folder in new_list:
			try:
				os.mkdir(os.path.join(root_path,folder))
				root_path = root_path + folder + '/'
			except FileExistsError:
				os.path.join(root_path, folder)
				root_path = root_path + folder+ '/'
		os.chdir(root_path)
		self.file = open("{0}.txt".format(a),"w")

	def parses_text(self):
		strokes = ""
		for x in self.list_text:
			if len(strokes) < self.num_sim and len(strokes) + len(x) < self.num_sim:
				strokes = strokes + x + " "
			else:
				self.file.write(strokes + '\n')
				strokes = x + " "
		self.file.write(strokes + '\n')


def uses_parse(obj):
	obj.parse()
	obj.split_text()
	obj.create_file()
	obj.parses_text()

max_symbol = 80
url = input("Your url:")
more_sym = input("Want more symbols(now 80)? 1-Yes/0-No \n")
if more_sym == '1':
	max_symbol = input("Now:")

new_obj = Parser(url, int(max_symbol))
uses_parse(new_obj)




