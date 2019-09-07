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


class TestPastAsModule(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_module_0(self):
        """Test past as module with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indent_size=3)
        module = printer['Module']

        self.assertEqual('\n' + module, TEST_MODULE_0_REF)

    def test_past_as_module_1(self):
        """Test past as module with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indent_size=3)
        module = printer['Module']

        self.assertEqual('\n' + module, TEST_MODULE_1_REF)

    def test_past_as_module_2(self):
        """Test past as module with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indent_size=3)
        module = printer['Module']

        self.assertEqual('\n' + module, TEST_MODULE_2_REF)

    def test_past_as_module_3(self):
        """Test past as module with TEST_MODULE_3"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_3)

        printer = Printer(moddict, indent_size=3)
        module = printer['Module']

        self.assertEqual('\n' + module, TEST_MODULE_3_REF)

    def test_past_as_module_4(self):
        """Test past as module with TEST_MODULE_4"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_4)

        printer = Printer(moddict, indent_size=3)
        module = printer['Module']

        self.assertEqual('\n' + module, TEST_MODULE_4_REF)


TEST_MODULE_0_REF = ("""
module alu_dsp
#(
   parameter add_extra_instr         = 1,
   parameter add_select_instr        = 1,
   parameter string add_select_instr = "M144k,auto",
   parameter shorten_pipeline        = 0
)
(
   input   clk,
   input   enable,
   input   is_signed,
   input   enacc,
   input   sub_nadd,
   input   selacc,
   input   resetrs0,
   input  [31:0] rs0,
   input  [31:0] rs1,
   input  [31:0] imm,
   input   mulmux,
   input   selop0,
   input   selop1,
   input  [1:0] selshift,
   input  [1:0] cmode,
   input  [2:0] opcode1,
   input  [2:0] opcode2,
   output   out_en,
   output  [31:0] out
);
""")


TEST_MODULE_1_REF = ("""
module mymod
#(
   parameter GEN1                      = 48,
   parameter GEN2                      = 45,
   parameter GEN3_WIDTH                = $clog2(VALUE),
   parameter [31:0] DEFAULT_VAL_A      = 32'b0,
   parameter int [31:0] DEFAULT_VAL_B  = 32'b0,
   parameter [31:0] DEFAULT_VAL_C [1:0]
)
(
   input logic  reset_n,
   input logic  clock,
   input logic [$clog2(GEN3_WIDTH+1)-1:0] test,
   input pkg::typedef  clock2,
   myinterface.master  m_master,
   myinterface.slave  s_slave,
   output logic [28:0][$clog2(GEN1):0] m_big_array[1:0][2:0],
   output logic [15:0] m_simple_array,
   output logic [15:0] m_simple_array3
);
""")


TEST_MODULE_2_REF = ("""
module testmod
(
   input logic  srst,
   input logic  clk,
   myinterface.slave  itf1,
   myinterface.master  itf2,
   input logic  insig1,
   input logic [31:0] insig2,
   input logic [10:0] insig3,
   input logic [7:0] insig4,
   output logic [47:0] outsig1,
   output logic [15:0] outsig2,
   input logic  another_srst,
   input logic  another_clock,
   otherinterface.slave  oitf,
   output logic  outsig3
);
""")


TEST_MODULE_3_REF = ("""
module testmod2
(
   input logic  srst,
   input logic  clk,
   input logic  another_srst,
   input logic  another_clock,
   otherinterface.slave  oitf[2:0],
   output logic  outsig3[1:0]
);
""")


TEST_MODULE_4_REF = ("""
module testmod3
   import pkg1::test,
          pkg2::test2,
          pkg3::*;
(
   input logic  srst,
   input logic  clk,
   input logic  another_srst,
   input logic  another_clock,
   otherinterface.slave  oitf[2:0],
   output logic  outsig3[1:0]
);
""")


if __name__ == '__main__':
    unittest.main()
