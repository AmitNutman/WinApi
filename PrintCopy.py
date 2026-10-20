#עמית נוטמן ועמית נברוצקי

import time
import win32clipboard
import win32con


def get_clipboard_text():
    """
    open the clipboard read text and close it
    """
    text = None
    try:
        win32clipboard.OpenClipboard()

        #Check if clipboard has unicode text format - unicade allows to have hebrew and english
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
            #reads the text from clipboard as unicode format
            text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)

        win32clipboard.CloseClipboard()
    except Exception as e:
        print(e)

    return text #can also have nothing

if __name__ == "__main__":
    last_text = ""

    while True:
        # Fetch current text from clipboard
        current_text = get_clipboard_text()

        # Check if new text was copied
        if current_text and current_text != last_text:
            last_text = current_text
            print(current_text)

        # to keep thee clipboard available
        time.sleep(0.2)
