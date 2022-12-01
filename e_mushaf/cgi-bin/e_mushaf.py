#!/usr/bin/python
import os, gettext, json


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
script_name = os.path.basename(__file__)

lang_translations = gettext.translation('base', localedir=base_dir + '/static/locales', languages=["ar"])
lang_translations.install()
_ = lang_translations.gettext

arabic = '۰١٢٣٤٥٦٧٨٩'
english = '0123456789'
translation_table = str.maketrans(english, arabic)

file = open(base_dir + '/static/data/Quran.json', 'r', encoding=" utf-8-sig")
json_data = json.load(file)
file.close()

html = """contents-type:text/html\r\n
<!DOCTYPE html>
<html dir='rtl' lang='ar'>
<head>
	<meta charset='utf-8'>
	<meta name="viewport" contents="width=device-width, initial-scale=1.0">
	<link rel="icon" type="image/x-icon" href="/static/image/favicon/favicon.ico">
	<link rel='stylesheet' href='/static/css/style.css'>
	<title>{0}</title>
</head>
<body>
	<div class="topnav">
		<a href="index.py">HOME</a>
		<a href="info.py" class="split">ABOUT</a>
	</div>
	<div>
		{1}
	<div>
</body>
</html>
""".replace("HOME", _("Index")).replace("ABOUT", _("About"))

hyperlink = "<a href='{0}'>{1}</a>"
paramslink = hyperlink.format("quran.py?id={0}&name={1}", "{1}")

title = _("E-mus'haf")
contents = _("E-mus'haf")

class HTMLTable:
	def __init__(self, *args):
		self.tr = "\n\t\t<tr>{}\n\t\t</tr>"
		th = "\n\t\t\t<th>{}</th>"
		self.tuple = ()
		for header in args:
			self.tuple = self.tuple + (th.format(header),)
		self.tuple = self.tr.format("".join(self.tuple))
		
	def add_row(self, *args):
		td_tuple = ()
		td = "\n\t\t\t<td>{}</td>"
		for cell in args:
			td_tuple = td_tuple + (td.format(cell),)
		self.tuple =  self.tuple  + self.tr.format("".join(td_tuple),)
		
	def show(self):
		table = "<table>{}\n\t\t</table>"
		return (table.format("".join(self.tuple)))


if script_name == "index.py":
	table = HTMLTable(_("No"), _("Surah"), _("Origin"), _("Number of ayat"),)
	
	for i in range(len(json_data)):
		translated_id = str(json_data[i]["id"]).translate(translation_table)
		origin = json_data[i]["type"]
		link = paramslink.format(i, json_data[i]["name"])
		translated_ayat = str(json_data[i]["array"][-1]["id"]).translate(translation_table)
		table.add_row(translated_id, link, origin, translated_ayat, )
		
	title = _("Index")
	contents = table.show()

elif script_name == "quran.py":
	args = os.getenv("QUERY_STRING").split('&')
	try:
		value = int(args[0].split('=')[1])
	except (IndexError, ValueError):
		value = 0

	if 0 <= value < 114:
		r = ()
		for i in range(value-1, value+2):
			if 0 <= i < 114:
				r = r +(paramslink.format(i, json_data[i]["name"]), )
			else:
				r = r +(" - - - ",)
		table = HTMLTable(_("Previous"), _("Current"), _("Next"))
		table.add_row(r[0], r[1], r[2])

		translated_ar = str(json_data[value]["ar"]).translate(translation_table)
		
		bismillah = "<br><h4>" + _("Bism allah alrahman alrahim")+ "</h4>" 
		surah = "<p class='page'>" + translated_ar + "</p><br>"

		title = _("Mus'haf") + " - " + _("surah") + " " + json_data[value]["name"]
		contents = table.show() + bismillah + surah

elif script_name == "info.py":
#	mail = "admen@example.com"
	source_code = hyperlink.format("/src", _("Source code of site"))
	quran_json_url = hyperlink.format("https://github.com/rn0x/Quran-Json", _("Holy Quran in JSON format"))
#	contact = hyperlink.format("mailto:" + mail, _("Contact us"))
	contents = "<p>"+source_code+"<br>"+quran_json_url+"</p>"
else:
	pass

print(html.format(title, ''.join(contents)))










