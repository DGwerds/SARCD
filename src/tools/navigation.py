from tkinter import IntVar

from .tool import Tool


class Navigation(Tool):
    def __init__(self, image_viewer):
        self.__image_viewer = image_viewer
        self.__canvas = self.__image_viewer.canvas
        self.__steps = IntVar(value=1)

    def left_click(self, event):
        pass

    def right_click(self, event):
        pass

    def drag(self, event):
        pass

    def wheel(self, event):
        """ Zoom with mouse wheel """
        if event.num == 5 or event.delta == -120:  # scroll down
            self.__previous_dicom_image(event)
        if event.num == 4 or event.delta == 120:  # scroll up
            self.__next_dicom_image(event)

    def __next_dicom_image(self, _event):
        steps = self.__steps.get()
        if self.__image_viewer.slice_number+steps >= len(self.__image_viewer.dicoms_data) - 1:
            return
        self.__image_viewer.slice_number += steps
        self.__image_viewer.read_dicom_file(self.__image_viewer.slice_number)
        self.__image_viewer.show_image()

    def __previous_dicom_image(self, _event):
        steps = self.__steps.get()
        if self.__image_viewer.slice_number-steps <= 0:
            return
        self.__image_viewer.slice_number -= steps
        self.__image_viewer.read_dicom_file(self.__image_viewer.slice_number)
        self.__image_viewer.show_image()

    def ctrl_wheel(self, event):
        self.wheel(event)
        pass

    def click_release(self, event):
        pass

    def get_description(self):
        return "Zoom tool description (work in progress)"

    def get_parameters(self):
        param = [{"type": "spinbox", "name": "Steps", "value": self.__steps, "max_value": 10,
                  "min_value": 1, "increment": 1}]
        return param

    # def update_parameters(self, **kwargs):
    #     for clave, valor in kwargs.items():
    #         setattr(self, clave, valor)
