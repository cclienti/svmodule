# -*- coding: utf-8 -*-
#
# This file is part of svmodule. See the root README.md for further
# information.
#
# svmodule is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# svmodule is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with svmodule.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2019 Christophe Clienti

"""Test Printer classes."""

import unittest

from svmodule.moddict import ModDict
from svmodule.printer import Printer

from . import test_printers_inputs as inputs


class TestPastAsImportList(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_importlist_0(self):
        """Test past as importlist with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indentSize=2)
        importlist = printer['ImportList']
        print(importlist)

        self.assertEqual('\n' + importlist, TEST_MODULE_3_REF)

    def test_past_as_importlist_1(self):
        """Test past as importlist with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indentSize=2)
        importlist = printer['ImportList']
        print(importlist)
        self.assertEqual('\n' + importlist, TEST_MODULE_4_REF)


TEST_MODULE_3_REF = ("""
""")


TEST_MODULE_4_REF = ("""
""")


if __name__ == '__main__':
    unittest.main()
