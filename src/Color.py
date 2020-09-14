""" A simple coloring, formating file """

class Styling():
    def __init__(self):
        self.colors = {
        "BLACK" : "\033[0;30m",
        "RED" : "\033[0;31m",
        "GREEN" : "\033[0;32m",
        "BROWN" : "\033[0;33m",
        "BLUE" : "\033[0;34m",
        "PURPLE" : "\033[0;35m",
        "CYAN" : "\033[0;36m",
        "LIGHT_GRAY" : "\033[0;37m",
        "DARK_GRAY" : "\033[1;30m",
        "LIGHT_RED" : "\033[1;31m",
        "LIGHT_GREEN" : "\033[1;32m",
        "YELLOW" : "\033[1;33m",
        "LIGHT_BLUE" : "\033[1;34m",
        "LIGHT_PURPLE" : "\033[1;35m",
        "LIGHT_CYAN" : "\033[1;36m",
        "LIGHT_WHITE" : "\033[1;37m"
        }

    def GetStyle(self, color):

        if color:
            return self.colors[color.upper()]


def GetColor(color=None):
    """Get a color code.

    Args:
        color (str, optional): The color you want to be returned. Defaults to None.

    Returns:
        str: Color Codes

    Colors:
        black
        red
        green
        brown
        blue
        purple
        cyan
        light_gray
        dark_gray
        light_red
        light_green
        yellow
        light_blue
        light_purple
        light_cyan
        light_white
    """ 
    StyleClass = Styling()
    return StyleClass.GetStyle(color)

