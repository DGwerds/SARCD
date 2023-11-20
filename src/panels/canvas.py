import os
from tkinter import *
from tkinter.ttk import *

import pydicom as dcm
from PIL import Image, ImageTk

import numpy as np


class AutoScrollbar(Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
            Scrollbar.set(self, lo, hi)


def window_image(img, window_center, window_width, intercept, slope, rescale=True):
    img = (img * slope + intercept)  # for translation adjustments given in the dicom file.
    img_min = window_center - window_width // 2  # minimum HU level
    img_max = window_center + window_width // 2  # maximum HU level
    img[img < img_min] = img_min  # set img_min for all HU levels less than minimum HU level
    img[img > img_max] = img_max  # set img_max for all HU levels higher than maximum HU level
    if rescale:
        img = (img - img_min) / (img_max - img_min) * 255.0
    return img


def get_first_of_dicom_field_as_int(x):
    # get x[0] as in int is x is a 'pydicom.multival.MultiValue', otherwise get int(x)
    if type(x) == dcm.multival.MultiValue:
        return int(x[0])
    else:
        return int(x)


def get_windowing(data):
    dicom_fields = [data[('0028', '1050')].value,  # window center
                    data[('0028', '1051')].value,  # window width
                    data[('0028', '1052')].value,  # intercept
                    data[('0028', '1053')].value]  # slope
    return [get_first_of_dicom_field_as_int(x) for x in dicom_fields]


class ImageViewer(Frame):
    def __init__(self, root_window, path):
        super().__init__(master=root_window, style='ImageViewer.TFrame')
        self.dicoms_data = None
        self.dicoms_image_fromarray = []
        self.slice_number: int = 0
        Style().configure(style='ImageViewer.TFrame', background='gray')

        vbar = AutoScrollbar(self, orient='vertical')
        hbar = AutoScrollbar(self, orient='horizontal')
        vbar.grid(row=0, column=1, sticky='ns')
        hbar.grid(row=1, column=0, sticky='we')

        # Create canvas and put image on it
        self.canvas = Canvas(self, highlightthickness=0,
                             xscrollcommand=hbar.set, yscrollcommand=vbar.set, background='lightgray')
        self.canvas.grid(row=0, column=0, sticky='nsew')

        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=0)
        self.columnconfigure(index=1, weight=0)

        # Bind events to the Canvas
        self.canvas.bind(sequence='<Configure>', func=self.show_image)
        self.canvas.bind(sequence='<Control-MouseWheel>', func=self.__next_dicom_image)
        self.canvas.bind(sequence='<Control-4>', func=self.__next_dicom_image)
        self.canvas.bind(sequence='<Control-5>', func=self.__previous_dicom_image)
        self.__filter = Image.LANCZOS  # could be: NEAREST, BILINEAR, BICUBIC and ANTIALIAS

        # bind mouse hover canvas
        # self.canvas.bind(sequence='<Enter>', func=self.__get_focus)

        if os.path.isdir(path):
            self.load_dicom_files(path)
        elif os.path.isfile(path):
            self.image = Image.open(path)

        self.width, self.height = self.image.size
        self.imscale = 1.0  # scale for the canvaas image
        # Put image into container rectangle and use it to set proper coordinates to the image
        self.container = self.canvas.create_rectangle(0, 0, self.width, self.height, width=0)
        self.show_image()

    def load_dicom_files(self, folder_path):
        self.slice_number: int = 0
        img_paths: list[str] = [os.path.join(folder_path, file)
                                for file in os.listdir(folder_path) if file.lower().endswith(".dcm")]

        img_paths.sort()
        self.dicoms_data = [dcm.dcmread(img) for img in img_paths]
        self.read_dicom_file(self.slice_number)

    def read_dicom_file(self, slice_number):
        if self.slice_number >= len(self.dicoms_image_fromarray):
            dicom_pixel_array = self.dicoms_data[slice_number].pixel_array
            image = dicom_pixel_array
            window_center, window_width, intercept, slope = get_windowing(self.dicoms_data[slice_number])
            output = window_image(image, window_center, window_width, intercept, slope, rescale=False)
            self.dicoms_image_fromarray.append(Image.fromarray(output))
            self.image = self.dicoms_image_fromarray[self.slice_number]
        else:
            self.image = self.dicoms_image_fromarray[self.slice_number]


    def __next_dicom_image(self, _event):
        if self.slice_number >= len(self.dicoms_data):
            return
        self.slice_number += 1
        self.read_dicom_file(self.slice_number)
        self.show_image()

    def __previous_dicom_image(self, _event):
        if self.slice_number <= 0:
            return
        self.slice_number -= 1
        self.read_dicom_file(self.slice_number)
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
            imagetk = ImageTk.PhotoImage(image.resize(size=(int(x2 - x1), int(y2 - y1))))
            imageid = self.canvas.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
                                               anchor='nw', image=imagetk)
            self.canvas.lower(imageid)  # set image into background
            self.canvas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection
