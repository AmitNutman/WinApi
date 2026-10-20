#עמית נוטמן ועמית נברוצקי
#https://github.com/AmitNutman/WinApi


import win32gui


def window_enum_callback(id,extra):
    """
    Function that checks which windows are open
    :param id: name\handle of the current window
    :param extra: extra param that the callback has
    """
    # checks if the client can see it - if the window is defined as visible
    if win32gui.IsWindowVisible(id):
        # get name of the open window
        name = win32gui.GetWindowText(id)
        # prints only the names that have text
        if name:
            print(name)


if __name__ == "__main__":

    # starts scan on all windows: calls to window_enum_callback for every window
    win32gui.EnumWindows(window_enum_callback,None) #doesnt work without none, extra variable

