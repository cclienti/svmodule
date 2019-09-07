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


class TestPastAsInitLatch(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_initlatch_0(self):
        """Test past as initlatch with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indent_size=2)
        initlatch = printer['InitLatch']

        self.assertEqual('\n' + initlatch, TEST_MODULE_0_REF)

    def test_past_as_initlatch_1(self):
        """Test past as initlatch with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indent_size=2)
        initlatch = printer['InitLatch']

        self.assertEqual('\n' + initlatch, TEST_MODULE_1_REF)

    def test_past_as_initlatch_2(self):
        """Test past as initlatch with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indent_size=2)
        initlatch = printer['InitLatch']

        self.assertEqual('\n' + initlatch, TEST_MODULE_2_REF)

    def test_past_as_initlatch_3(self):
        """Test past as initlatch with TEST_MODULE_3"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_3)

        printer = Printer(moddict, indent_size=2)
        initlatch = printer['InitLatch']

        self.assertEqual('\n' + initlatch, TEST_MODULE_3_REF)

    def test_past_as_initlatch_4(self):
        """Test past as initlatch with TEST_MODULE_4"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_4)

        printer = Printer(moddict, indent_size=2)
        initlatch = printer['InitLatch']

        self.assertEqual('\n' + initlatch, TEST_MODULE_4_REF)


TEST_MODULE_0_REF = ("""
    clk       <= 1'b0;
    enable    <= 1'b0;
    is_signed <= 1'b0;
    enacc     <= 1'b0;
    sub_nadd  <= 1'b0;
    selacc    <= 1'b0;
    resetrs0  <= 1'b0;
    rs0       <= '0;
    rs1       <= '0;
    imm       <= '0;
    mulmux    <= 1'b0;
    selop0    <= 1'b0;
    selop1    <= 1'b0;
    selshift  <= '0;
    cmode     <= '0;
    opcode1   <= '0;
    opcode2   <= '0;
""")


TEST_MODULE_1_REF = ("""
    reset_n <= 1'b0;
    clock   <= 1'b0;
    test    <= '0;
    clock2  <= 1'b0;
""")


TEST_MODULE_2_REF = ("""
    srst          <= 1'b0;
    clk           <= 1'b0;
    insig1        <= 1'b0;
    insig2        <= '0;
    insig3        <= '0;
    insig4        <= '0;
    another_srst  <= 1'b0;
    another_clock <= 1'b0;
""")


TEST_MODULE_3_REF = ("""
    srst          <= 1'b0;
    clk           <= 1'b0;
    another_srst  <= 1'b0;
    another_clock <= 1'b0;
""")


TEST_MODULE_4_REF = ("""
    srst          <= 1'b0;
    clk           <= 1'b0;
    another_srst  <= 1'b0;
    another_clock <= 1'b0;
""")


if __name__ == '__main__':
    unittest.main()
