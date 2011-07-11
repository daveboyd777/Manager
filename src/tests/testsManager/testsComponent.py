#!/usr/bin/env python
# -*- coding: utf-8 -*-

#***********************************************************************************************
#
# Copyright (C) 2008 - 2011 - Thomas Mansencal - thomas.mansencal@gmail.com
#
#***********************************************************************************************
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#***********************************************************************************************
#
# The Following Code Is Protected By GNU GPL V3 Licence.
#
#***********************************************************************************************

"""
************************************************************************************************
***	testsComponent.py
***
***	Platform:
***		Windows, Linux, Mac Os X
***
***	Description:
***		Component Tests Module.
***
***	Others:
***
************************************************************************************************
"""

#***********************************************************************************************
#***	Python Begin
#***********************************************************************************************

#***********************************************************************************************
#***	External Imports
#***********************************************************************************************
import unittest

#***********************************************************************************************
#***	Internal Imports
#***********************************************************************************************
from manager.component import Component

#***********************************************************************************************
#***	Overall Variables
#***********************************************************************************************

#***********************************************************************************************
#***	Module Classes And Definitions
#***********************************************************************************************
class ComponentTestCase(unittest.TestCase):
	"""
	This Class Is The ComponentTestCase Class.
	"""

	def testRequiredAttributes(self):
		"""
		This Method Tests Presence Of Required Attributes.
		"""

		component = Component()
		requiredAttributes = ("name",
							"activated",
							"deactivatable")

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(component))

	def testRequiredMethods(self):
		"""
		This Method Tests Presence Of Required Methods.
		"""

		component = Component()
		requiredMethods = ("_activate",
						"_deactivate")

		for method in requiredMethods:
			self.assertIn(method, dir(component))

	def test_activate(self):
		"""
		This Method Tests The "Component" Class "_activate" Method.
		"""

		component = Component()
		component._activate()
		self.assertTrue(component.activated)

	def test_deactivate(self):
		"""
		This Method Tests The "Component" Class "_deactivate" Method.
		"""

		component = Component()
		component.activated = True
		component._deactivate()
		self.assertFalse(component.activated)

if __name__ == "__main__":
	import tests.utilities
	unittest.main()

#***********************************************************************************************
#***	Python End
#***********************************************************************************************