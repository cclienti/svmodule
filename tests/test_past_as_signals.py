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


class TestPastAsSignals(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_signals_0(self):
        """Test past as signals with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indent_size=2)
        signals = printer['Signals']

        self.assertEqual('\n' + signals, TEST_MODULE_0_REF)

    def test_past_as_signals_1(self):
        """Test past as signals with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indent_size=2)
        signals = printer['Signals']

        print(signals)
        self.assertEqual('\n' + signals, TEST_MODULE_1_REF)

    def test_past_as_signals_2(self):
        """Test past as signals with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indent_size=2)
        signals = printer['Signals']

        print(signals)
        self.assertEqual('\n' + signals, TEST_MODULE_2_REF)

    def test_past_as_signals_3(self):
        """Test past as signals with TEST_MODULE_3"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_3)

        printer = Printer(moddict, indent_size=2)
        signals = printer['Signals']

        self.assertEqual('\n' + signals, TEST_MODULE_3_REF)

    def test_past_as_signals_4(self):
        """Test past as signals with TEST_MODULE_4"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_4)

        printer = Printer(moddict, indent_size=2)
        signals = printer['Signals']

        self.assertEqual('\n' + signals, TEST_MODULE_4_REF)


TEST_MODULE_0_REF = ("""
  reg clk;
  reg enable;
  reg is_signed;
  reg enacc;
  reg sub_nadd;
  reg selacc;
  reg resetrs0;
  reg [31:0] rs0 [31:0];
  reg [31:0] rs1 [31:0];
  reg [31:0] imm [31:0];
  reg mulmux;
  reg selop0;
  reg selop1;
  reg [1:0] selshift [1:0];
  reg [1:0] cmode [1:0];
  reg [2:0] opcode1 [2:0];
  reg [2:0] opcode2 [2:0];
  wire out_en;
  wire [31:0] out [31:0];
""")


TEST_MODULE_1_REF = ("""
  reg reset_n;
  reg clock;
  reg [$clog2(GEN3_WIDTH+1)-1:0] test [$clog2(GEN3_WIDTH+1)-1:0];
  reg clock2;
  wire [28:0][$clog2(GEN1):0] m_big_array [28:0][$clog2(GEN1):0][1:0][2:0];
  wire [15:0] m_simple_array [15:0];
  wire [15:0] m_simple_array3 [15:0];
""")


TEST_MODULE_2_REF = ("""
  reg srst;
  reg clk;
  reg insig1;
  reg [31:0] insig2 [31:0];
  reg [10:0] insig3 [10:0];
  reg [7:0] insig4 [7:0];
  wire [47:0] outsig1 [47:0];
  wire [15:0] outsig2 [15:0];
  reg another_srst;
  reg another_clock;
  wire outsig3;
""")


TEST_MODULE_3_REF = ("""
  reg srst;
  reg clk;
  reg another_srst;
  reg another_clock;
  wire outsig3[1:0];
""")


TEST_MODULE_4_REF = ("""
  reg srst;
  reg clk;
  reg another_srst;
  reg another_clock;
  wire outsig3[1:0];
""")


if __name__ == '__main__':
    unittest.main()
