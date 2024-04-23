# Make an abstract class for tools
from abc import ABC, abstractmethod


class Tool(ABC):
    @abstractmethod
    def left_click(self, event):
        pass

    @abstractmethod
    def right_click(self, event):
        pass

    @abstractmethod
    def wheel(self, event):
        pass

    @abstractmethod
    def ctrl_wheel(self, event):
        pass

    @abstractmethod
    def drag(self, event):
        pass

    @abstractmethod
    def click_release(self, event):
        pass

    # @abstractmethod
    # def get_description(self):
    #     pass
    #
    # @abstractmethod
    # def get_parameters(self):
    #     pass
