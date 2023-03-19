#Universel Document Page
import json
import os
import sys
import time
from tkinter import *
import xml.etree.ElementTree as xml
import tkinter as tk

#New Udp
class Udp:
	def __init__(self, file, rootwin:tk.Frame=Tk()):
		self.root=rootwin
		self.root.title("Udp Service")
		self.root.geometry("500x500")

		self.content=Label(self.root)
		self.content.pack()

		self.file=None

		self.saf_kod = open(file, "r", encoding="utf").read()
		self.code=xml.fromstring(self.saf_kod)

		if os.path.isfile(file):
			self.file=file
			self.execute()
		else:
			print("Error: File Not Found")

	def screen_sizes(self):
		return (winfo_screenheight, winfo_screenwidth)
	def execute(self):
		for elem in self.code.iter():
			if elem.tag == "config":
				if "set-win-size" in elem.attrib:
					self.root.geometry(elem.attrib["set-win-size"])
			if elem.tag == "title":
				self.root.title(elem.text)
			if elem.tag == "content":
				self.content.config(text=elem.text)
				if "font-size" in elem.attrib:
					self.content.config(font=(self.content["font"][0], elem.attrib["font-size"]))
				if "pack" in elem.attrib:
					try:
						self.content.pack(side=elem.attrib["pack"])
					except TclError:
						print(f"Error: Pack '{elem.attrib['pack']}' Not defined")
		self.root.mainloop()

