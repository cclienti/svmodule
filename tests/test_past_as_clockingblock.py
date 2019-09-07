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


class TestPastAsClockingBlock(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_clockingblock_0(self):
        """Test past as clockingblock with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indent_size=2)
        clockingblock = printer['ClockingBlock']

        self.assertEqual('\n' + clockingblock, TEST_MODULE_0_REF)

    def test_past_as_clockingblock_1(self):
        """Test past as clockingblock with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indent_size=2)
        clockingblock = printer['ClockingBlock']

        self.assertEqual('\n' + clockingblock, TEST_MODULE_1_REF)

    def test_past_as_clockingblock_2(self):
        """Test past as clockingblock with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indent_size=2)
        clockingblock = printer['ClockingBlock']

        self.assertEqual('\n' + clockingblock, TEST_MODULE_2_REF)


TEST_MODULE_0_REF = ("""
  default clocking cb @(posedge clk);
    output enable;
    output is_signed;
    output enacc;
    output sub_nadd;
    output selacc;
    output posedge resetrs0;
    output rs0;
    output rs1;
    output imm;
    output mulmux;
    output selop0;
    output selop1;
    output selshift;
    output cmode;
    output opcode1;
    output opcode2;
    input out_en;
    input out;
  endclocking
""")


TEST_MODULE_1_REF = ("""
  default clocking cb @(posedge clock);
    output negedge reset_n;
    output test;
    output clock2;
    //master m_master;
    //slave s_slave;
    input m_big_array;
    input m_simple_array;
    input m_simple_array3;
  endclocking
""")


TEST_MODULE_2_REF = ("""
  default clocking cb @(posedge clk);
    output  srst;
    //slave itf1;
    //master itf2;
    output insig1;
    output insig2;
    output insig3;
    output insig4;
    input outsig1;
    input outsig2;
    output another_srst;
    output another_clock;
    //slave oitf;
    input outsig3;
  endclocking
""")


if __name__ == '__main__':
    unittest.main()
