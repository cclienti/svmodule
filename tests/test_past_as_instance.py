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


class TestPastAsInstance(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_instance_0(self):
        """Test past as instance with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indentSize=2)
        instance = printer['Instance']

        self.assertEqual('\n' + instance, TEST_MODULE_0_REF)

    def test_past_as_instance_1(self):
        """Test past as instance with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indentSize=2)
        instance = printer['Instance']

        self.assertEqual('\n' + instance, TEST_MODULE_1_REF)

    def test_past_as_instance_2(self):
        """Test past as instance with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indentSize=2)
        instance = printer['Instance']

        self.assertEqual('\n' + instance, TEST_MODULE_2_REF)

    def test_past_as_instance_3(self):
        """Test past as instance with TEST_MODULE_3"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_3)

        printer = Printer(moddict, indentSize=2)
        instance = printer['Instance']

        self.assertEqual('\n' + instance, TEST_MODULE_3_REF)

    def test_past_as_instance_4(self):
        """Test past as instance with TEST_MODULE_4"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_4)

        printer = Printer(moddict, indentSize=2)
        instance = printer['Instance']

        self.assertEqual('\n' + instance, TEST_MODULE_4_REF)


TEST_MODULE_0_REF = (
"""
  alu_dsp
  #(
    .add_extra_instr  (add_extra_instr),
    .add_select_instr (add_select_instr),
    .add_select_instr (add_select_instr),
    .shorten_pipeline (shorten_pipeline)
  )
  alu_dsp_inst
  (
    .clk       (clk),
    .enable    (enable),
    .is_signed (is_signed),
    .enacc     (enacc),
    .sub_nadd  (sub_nadd),
    .selacc    (selacc),
    .resetrs0  (resetrs0),
    .rs0       (rs0),
    .rs1       (rs1),
    .imm       (imm),
    .mulmux    (mulmux),
    .selop0    (selop0),
    .selop1    (selop1),
    .selshift  (selshift),
    .cmode     (cmode),
    .opcode1   (opcode1),
    .opcode2   (opcode2),
    .out_en    (out_en),
    .out       (out)
  );
""")


TEST_MODULE_1_REF = (
"""
  mymod
  #(
    .GEN1          (GEN1),
    .GEN2          (GEN2),
    .GEN3_WIDTH    (GEN3_WIDTH),
    .DEFAULT_VAL_A (DEFAULT_VAL_A),
    .DEFAULT_VAL_B (DEFAULT_VAL_B),
    .DEFAULT_VAL_C (DEFAULT_VAL_C)
  )
  mymod_inst
  (
    .reset_n         (reset_n),
    .clock           (clock),
    .test            (test),
    .clock2          (clock2),
    .m_master        (m_master),
    .s_slave         (s_slave),
    .m_big_array     (m_big_array),
    .m_simple_array  (m_simple_array),
    .m_simple_array3 (m_simple_array3)
  );
""")


TEST_MODULE_2_REF = (
"""
  testmod testmod_inst
  (
    .srst          (srst),
    .clk           (clk),
    .itf1          (itf1),
    .itf2          (itf2),
    .insig1        (insig1),
    .insig2        (insig2),
    .insig3        (insig3),
    .insig4        (insig4),
    .outsig1       (outsig1),
    .outsig2       (outsig2),
    .another_srst  (another_srst),
    .another_clock (another_clock),
    .oitf          (oitf),
    .outsig3       (outsig3)
  );
""")


TEST_MODULE_3_REF = (
"""
  testmod2 testmod2_inst
  (
    .srst          (srst),
    .clk           (clk),
    .another_srst  (another_srst),
    .another_clock (another_clock),
    .oitf          (oitf),
    .outsig3       (outsig3)
  );
""")


TEST_MODULE_4_REF = (
"""
  testmod3 testmod3_inst
  (
    .srst          (srst),
    .clk           (clk),
    .another_srst  (another_srst),
    .another_clock (another_clock),
    .oitf          (oitf),
    .outsig3       (outsig3)
  );
""")


if __name__ == '__main__':
    unittest.main()
