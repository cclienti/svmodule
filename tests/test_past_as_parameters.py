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


class TestPastAsParameters(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_parameters_0(self):
        """Test past as parameters with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indent_size=2)
        parameters = printer['Parameters']

        self.assertEqual('\n' + parameters, TEST_MODULE_0_REF)

    def test_past_as_parameters_1(self):
        """Test past as parameters with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indent_size=2)
        parameters = printer['Parameters']

        self.assertEqual('\n' + parameters, TEST_MODULE_1_REF)

    def test_past_as_parameters_2(self):
        """Test past as parameters with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indent_size=2)
        parameters = printer['Parameters']

        self.assertEqual('\n' + parameters, TEST_MODULE_2_REF)


TEST_MODULE_0_REF = ("""
  localparam add_extra_instr         = 1;
  localparam add_select_instr        = 1;
  localparam string add_select_instr = "M144k,auto";
  localparam shorten_pipeline        = 0;
""")


TEST_MODULE_1_REF = ("""
  localparam GEN1                     = 48;
  localparam GEN2                     = 45;
  localparam GEN3_WIDTH               = $clog2(VALUE);
  localparam [31:0] DEFAULT_VAL_A     = 32'b0;
  localparam int [31:0] DEFAULT_VAL_B = 32'b0;
  localparam [31:0] DEFAULT_VAL_C;
""")


TEST_MODULE_2_REF = ("""
""")


if __name__ == '__main__':
    unittest.main()
