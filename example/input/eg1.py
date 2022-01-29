from datetime import datetime as dt
import math
from math import sqrt, sin


class Eg1:
    def __init__(self, name):
        """Create Eg1 object

        Args:
            name ([str]): Give object a name
        """
        self.name = name

    def get_name(self):
        """Get name of object

        Returns:
            [str]: Name of object
        """
        return self.name


class Eg11(Eg1):
    def get_name(self):
        """Get name of object

        Returns:
            [str]: Name of object
        """
        return "Extended" + self.name