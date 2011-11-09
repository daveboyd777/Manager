#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**constants.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines **Manager** package default constants through the :class:`Constants` class.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import platform

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["Constants"]

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class Constants():
	"""
	This class provides **Manager** package default constants.
	"""

	applicationName = "Manager"
	"""Package Application name: '**Manager**' ( String )"""
	releaseVersion = "1.0.2"
	"""Package release version: '**1.0.2**' ( String )"""

	logger = "Manager_Logger"
	"""Package logger name: '**Manager_Logger**' ( String )"""
	verbosityLevel = 3
	"""Default logging verbosity level: '**3**' ( Integer )"""
	verbosityLabels = ("Critical", "Error", "Warning", "Info", "Debug")
	"""Logging verbosity labels: ('**Critical**', '**Error**', '**Warning**', '**Info**', '**Debug**') ( Tuple )"""
	loggingDefaultFormatter = "Default"
	"""Default logging formatter name: '**Default**' ( String )"""
	loggingSeparators = "*" * 96
	"""Logging separators: '*' * 96 ( String )"""

	encodingFormat = "utf-8"
	"""Default encoding format: '**utf-8**' ( String )"""
	encodingError = "ignore"
	"""Default encoding error behavior: '**ignore**' ( String )"""

	applicationDirectory = "Manager"
	"""Package Application directory: '**Manager**' ( String )"""
	if platform.system() == "Windows" or platform.system() == "Microsoft" or platform.system() == "Darwin":
		providerDirectory = "HDRLabs"
		"""Package provider directory: '**HDRLabs** on Windows / Darwin, **.HDRLabs** on Linux' ( String )"""
	elif platform.system() == "Linux":
		providerDirectory = ".HDRLabs"
		"""Package provider directory: '**HDRLabs** on Windows / Darwin, **.HDRLabs** on Linux' ( String )"""

	nullObject = "None"
	"""Default null object string: '**None**' ( String )"""
