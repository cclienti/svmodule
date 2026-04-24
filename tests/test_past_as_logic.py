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


class TestPastAsLogic(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_logic_0(self):
        """Test past as logic with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indent_size=2)
        logic = printer['Logic']

        self.assertEqual('\n' + logic, TEST_MODULE_0_REF)

    def test_past_as_logic_1(self):
        """Test past as logic with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indent_size=2)
        logic = printer['Logic']

        self.assertEqual('\n' + logic, TEST_MODULE_1_REF)

    def test_past_as_logic_2(self):
        """Test past as logic with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indent_size=2)
        logic = printer['Logic']

        self.assertEqual('\n' + logic, TEST_MODULE_2_REF)

    def test_past_as_logic_3(self):
        """Test past as logic with TEST_MODULE_3"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_3)

        printer = Printer(moddict, indent_size=2)
        logic = printer['Logic']

        self.assertEqual('\n' + logic, TEST_MODULE_3_REF)

    def test_past_as_logic_4(self):
        """Test past as logic with TEST_MODULE_4"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_4)

        printer = Printer(moddict, indent_size=2)
        logic = printer['Logic']

        self.assertEqual('\n' + logic, TEST_MODULE_4_REF)



    def test_past_as_logic_no_type_default_none(self):
        """Ports with no explicit type are skipped when default_type is None (backward compat)."""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_6)

        printer = Printer(moddict, indent_size=2)
        logic = printer['Logic']

        self.assertEqual(logic, '')

    def test_past_as_logic_no_type_default_logic(self):
        """Ports with no explicit type fall back to 'logic' when default_type='logic'."""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_6)

        printer = Printer(moddict, indent_size=2, default_type='logic')
        logic = printer['Logic']

        self.assertEqual('\n' + logic, TEST_MODULE_6_LOGIC_REF)

    def test_past_as_logic_no_type_default_wire(self):
        """Ports with no explicit type fall back to 'wire' when default_type='wire'."""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_6)

        printer = Printer(moddict, indent_size=2, default_type='wire')
        logic = printer['Logic']

        self.assertEqual('\n' + logic, TEST_MODULE_6_WIRE_REF)

    def test_past_as_logic_explicit_type_takes_priority(self):
        """Explicit port types are preserved even when default_type is set."""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indent_size=2, default_type='wire')
        logic = printer['Logic']

        # TEST_MODULE_1 has explicit 'logic' and 'pkg::typedef' types — they must not
        # be overridden by default_type='wire'
        self.assertEqual('\n' + logic, TEST_MODULE_1_REF)
TEST_MODULE_0_REF = ("""
""")


TEST_MODULE_1_REF = ("""
  logic  reset_n;
  logic  clock;
  logic [$clog2(GEN3_WIDTH+1)-1:0] test;
  pkg::typedef  clock2;
  myinterface  m_master();
  myinterface  s_slave();
  logic [28:0][$clog2(GEN1):0] m_big_array[1:0][2:0];
  logic [15:0] m_simple_array;
  logic [15:0] m_simple_array3;
""")


TEST_MODULE_2_REF = ("""
  logic  srst;
  logic  clk;
  myinterface  itf1();
  myinterface  itf2();
  logic  insig1;
  logic [31:0] insig2;
  logic [10:0] insig3;
  logic [7:0] insig4;
  logic [47:0] outsig1;
  logic [15:0] outsig2;
  logic  another_srst;
  logic  another_clock;
  otherinterface  oitf();
  logic  outsig3;
""")


TEST_MODULE_3_REF = ("""
  logic  srst;
  logic  clk;
  logic  another_srst;
  logic  another_clock;
  otherinterface  oitf[2:0]();
  logic  outsig3[1:0];
""")


TEST_MODULE_4_REF = ("""
  logic  srst;
  logic  clk;
  logic  another_srst;
  logic  another_clock;
  otherinterface  oitf[2:0]();
  logic  outsig3[1:0];
""")



TEST_MODULE_6_LOGIC_REF = ("""
  logic  clk;
  logic  reset_n;
  logic  other_out;
  logic [DIN_WIDTH-1:0] binin;
  logic [DOUT_WIDTH-1:0] thermout;
""")


TEST_MODULE_6_WIRE_REF = ("""
  wire  clk;
  wire  reset_n;
  wire  other_out;
  wire [DIN_WIDTH-1:0] binin;
  wire [DOUT_WIDTH-1:0] thermout;
""")

if __name__ == '__main__':
    unittest.main()

