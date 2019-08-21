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


class TestPastAsInitWire(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_initwire_0(self):
        """Test past as initwire with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indentSize=2)
        initwire = printer['InitWire']

        self.assertEqual('\n' + initwire, TEST_MODULE_0_REF)

    def test_past_as_initwire_1(self):
        """Test past as initwire with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indentSize=2)
        initwire = printer['InitWire']

        self.assertEqual('\n' + initwire, TEST_MODULE_1_REF)

    def test_past_as_initwire_2(self):
        """Test past as initwire with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indentSize=2)
        initwire = printer['InitWire']

        self.assertEqual('\n' + initwire, TEST_MODULE_2_REF)

    def test_past_as_initwire_3(self):
        """Test past as initwire with TEST_MODULE_3"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_3)

        printer = Printer(moddict, indentSize=2)
        initwire = printer['InitWire']

        self.assertEqual('\n' + initwire, TEST_MODULE_3_REF)

    def test_past_as_initwire_4(self):
        """Test past as initwire with TEST_MODULE_4"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_4)

        printer = Printer(moddict, indentSize=2)
        initwire = printer['InitWire']

        self.assertEqual('\n' + initwire, TEST_MODULE_4_REF)


TEST_MODULE_0_REF = ("""
  assign clk       = 1'b0;
  assign enable    = 1'b0;
  assign is_signed = 1'b0;
  assign enacc     = 1'b0;
  assign sub_nadd  = 1'b0;
  assign selacc    = 1'b0;
  assign resetrs0  = 1'b0;
  assign rs0       = '0;
  assign rs1       = '0;
  assign imm       = '0;
  assign mulmux    = 1'b0;
  assign selop0    = 1'b0;
  assign selop1    = 1'b0;
  assign selshift  = '0;
  assign cmode     = '0;
  assign opcode1   = '0;
  assign opcode2   = '0;
""")


TEST_MODULE_1_REF = ("""
  assign reset_n = 1'b0;
  assign clock   = 1'b0;
  assign test    = '0;
  assign clock2  = 1'b0;
""")


TEST_MODULE_2_REF = ("""
  assign srst          = 1'b0;
  assign clk           = 1'b0;
  assign insig1        = 1'b0;
  assign insig2        = '0;
  assign insig3        = '0;
  assign insig4        = '0;
  assign another_srst  = 1'b0;
  assign another_clock = 1'b0;
""")


TEST_MODULE_3_REF = ("""
  assign srst          = 1'b0;
  assign clk           = 1'b0;
  assign another_srst  = 1'b0;
  assign another_clock = 1'b0;
""")


TEST_MODULE_4_REF = ("""
  assign srst          = 1'b0;
  assign clk           = 1'b0;
  assign another_srst  = 1'b0;
  assign another_clock = 1'b0;
""")


if __name__ == '__main__':
    unittest.main()
