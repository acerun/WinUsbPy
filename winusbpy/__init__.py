import os
if os.name != 'nt':
	raise ImportError("WinUsbPy only works on Windows platform")
from .winusbpy import *
from .winusb import *
