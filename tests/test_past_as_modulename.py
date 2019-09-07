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
# svmodulename is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with svmodulename.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2019 Christophe Clienti

"""Test Printer classes."""

import unittest

from svmodule.moddict import ModDict
from svmodule.printer import Printer

from . import test_printers_inputs as inputs


class TestPastAsModuleName(unittest.TestCase):
    """Test class svmodulename Printers."""

    def test_past_as_modulename_0(self):
        """Test past as modulename with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indent_size=2)
        modulename = printer['ModuleName']

        print(modulename)
        self.assertEqual(modulename, TEST_MODULE_0_REF)

    def test_past_as_modulename_1(self):
        """Test past as modulename with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indent_size=2)
        modulename = printer['ModuleName']

        print(modulename)
        self.assertEqual(modulename, TEST_MODULE_1_REF)

    def test_past_as_modulename_2(self):
        """Test past as modulename with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indent_size=2)
        modulename = printer['ModuleName']

        print(modulename)
        self.assertEqual(modulename, TEST_MODULE_2_REF)

    def test_past_as_modulename_3(self):
        """Test past as modulename with TEST_MODULE_3"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_3)

        printer = Printer(moddict, indent_size=2)
        modulename = printer['ModuleName']

        print(modulename)
        self.assertEqual(modulename, TEST_MODULE_3_REF)

    def test_past_as_modulename_4(self):
        """Test past as modulename with TEST_MODULE_4"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_4)

        printer = Printer(moddict, indent_size=2)
        modulename = printer['ModuleName']

        print(modulename)
        self.assertEqual(modulename, TEST_MODULE_4_REF)


TEST_MODULE_0_REF = ('alu_dsp')


TEST_MODULE_1_REF = ('mymod')


TEST_MODULE_2_REF = ('testmod')


TEST_MODULE_3_REF = ('testmod2')


TEST_MODULE_4_REF = ('testmod3')


if __name__ == '__main__':
    unittest.main()
