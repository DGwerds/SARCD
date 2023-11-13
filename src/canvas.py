from tkinter import *
from tkinter.ttk import *
from src.canvas_tools import CanvasTools
from PIL import Image, ImageTk
import pydicom as dcm
import os
import sys
import random


class AutoScrollbar(Scrollbar):
	""" A scrollbar that hides itself if it's not needed.
		Works only if you use the grid geometry manager """

	def set(self, lo, hi):
		if float(lo) <= 0.0 and float(hi) >= 1.0:
			self.grid_remove()
		else:
			self.grid()
			Scrollbar.set(self, lo, hi)


def load_dicom_files(folder_path):
	# print(type(self))
	slice_number: int = 0
	img_paths: list[str] = [os.path.join(folder_path, file)
	                        for file in os.listdir(folder_path) if file.lower().endswith(".dcm")]

	dicoms_data = [dcm.dcmread(img) for img in img_paths]
	pixel_array = dicoms_data[slice_number].pixel_array
	photo = Image.fromarray(pixel_array)
	return photo


class ImageViewer(Frame):
	def __init__(self, root_window, path):
		super().__init__(master=root_window, style='ImageViewer.TFrame')
		Style().configure(style='ImageViewer.TFrame', background='gray')

		vbar = AutoScrollbar(self, orient='vertical')
		hbar = AutoScrollbar(self, orient='horizontal')
		vbar.grid(row=0, column=1, sticky='ns')
		hbar.grid(row=1, column=0, sticky='we')

		# Create canvas and put image on it
		self.canvas = Canvas(self, highlightthickness=0,
		                     xscrollcommand=hbar.set, yscrollcommand=vbar.set, background='black')
		self.canvas.grid(row=0, column=0, sticky='nsew')

		self.rowconfigure(index=0, weight=1)
		self.columnconfigure(index=0, weight=1)
		self.rowconfigure(index=1, weight=0)
		self.columnconfigure(index=1, weight=0)

		self.canvas_tools = CanvasTools(self)
		# Bind events to the Canvas
		self.canvas.bind(sequence='<Configure>', func=self.show_image)
		self.canvas.bind(sequence='<ButtonPress-1>', func=self.canvas_tools.click)
		self.canvas.bind(sequence='<B1-Motion>', func=self.canvas_tools.drag)

		match sys.platform:
			case 'win32' | 'win64' | 'darwin':
				self.canvas.bind(sequence='<MouseWheel>', func=self.canvas_tools.wheel)
			case 'linux':
				self.canvas.bind(sequence='<Button-5>', func=self.canvas_tools.wheel)
				self.canvas.bind(sequence='<Button-4>', func=self.canvas_tools.wheel)

		# self.image = Image.open(path)  # open image
		self.image = load_dicom_files(path)

		self.width, self.height = self.image.size
		self.imscale = 1.0  # scale for the canvaas image
		# Put image into container rectangle and use it to set proper coordinates to the image
		self.container = self.canvas.create_rectangle(0, 0, self.width, self.height, width=0)
		# Plot some optional random rectangles for the test purposes
		minsize, maxsize, number = 5, 40, 15
		for n in range(number):
			x0 = random.randint(0, self.width - maxsize)
			y0 = random.randint(0, self.height - maxsize)
			x1 = x0 + random.randint(minsize, maxsize)
			y1 = y0 + random.randint(minsize, maxsize)
			color = ('red', 'orange', 'yellow', 'green', 'blue')[random.randint(0, 4)]
			self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, activefill='black')
		self.show_image()

	def show_image(self, _event=None):
		""" Show image on the Canvas """
		bbox1 = self.canvas.bbox(self.container)  # get image area
		# Remove 1 pixel shift at the sides of the bbox1
		bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
		bbox2 = (self.canvas.canvasx(0),  # get visible area of the canvas
		         self.canvas.canvasy(0),
		         self.canvas.canvasx(self.canvas.winfo_width()),
		         self.canvas.canvasy(self.canvas.winfo_height()))
		bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]),  # get scroll region box
		        max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
		if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]:  # whole image in the visible area
			bbox[0] = bbox1[0]
			bbox[2] = bbox1[2]
		if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]:  # whole image in the visible area
			bbox[1] = bbox1[1]
			bbox[3] = bbox1[3]
		_aux: tuple[str | float, str | float, str | float, str | float] | tuple = tuple(bbox)
		self.canvas.configure(scrollregion=_aux)  # set scroll region
		x1 = max(bbox2[0] - bbox1[0], 0)  # get coordinates (x1,y1,x2,y2) of the image tile
		y1 = max(bbox2[1] - bbox1[1], 0)
		x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
		y2 = min(bbox2[3], bbox1[3]) - bbox1[1]
		if int(x2 - x1) > 0 and int(y2 - y1) > 0:  # show image if it in the visible area
			x = min(int(x2 / self.imscale), self.width)  # sometimes it is larger on 1 pixel...
			y = min(int(y2 / self.imscale), self.height)  # ...and sometimes not
			image = self.image.crop((int(x1 / self.imscale), int(y1 / self.imscale), x, y))
			imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1))))
			imageid = self.canvas.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
			                                   anchor='nw', image=imagetk)
			self.canvas.lower(imageid)  # set image into background
			self.canvas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection
