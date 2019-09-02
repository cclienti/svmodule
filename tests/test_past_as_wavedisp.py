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


class TestPastAsWavedisp(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_past_as_wavedisp_0(self):
        """Test past as wavedisp with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        printer = Printer(moddict, indentSize=2)
        wavedisp = printer['Wavedisp']

        self.assertEqual('\n' + wavedisp, TEST_MODULE_0_REF)

    def test_past_as_wavedisp_1(self):
        """Test past as wavedisp with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)

        printer = Printer(moddict, indentSize=2)
        wavedisp = printer['Wavedisp']

        print(wavedisp)
        self.assertEqual('\n' + wavedisp, TEST_MODULE_1_REF)

    def test_past_as_wavedisp_2(self):
        """Test past as wavedisp with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)

        printer = Printer(moddict, indentSize=2)
        wavedisp = printer['Wavedisp']

        print(wavedisp)
        self.assertEqual('\n' + wavedisp, TEST_MODULE_2_REF)

    def test_past_as_wavedisp_3(self):
        """Test past as wavedisp with TEST_MODULE_3"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_3)

        printer = Printer(moddict, indentSize=2)
        wavedisp = printer['Wavedisp']

        self.assertEqual('\n' + wavedisp, TEST_MODULE_3_REF)

    def test_past_as_wavedisp_4(self):
        """Test past as wavedisp with TEST_MODULE_4"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_4)

        printer = Printer(moddict, indentSize=2)
        wavedisp = printer['Wavedisp']

        self.assertEqual('\n' + wavedisp, TEST_MODULE_4_REF)


TEST_MODULE_0_REF = ("""
# -*- python -*-
# To include in alu_dsp_tb.wave.py:

from wavedisp.ast import *


def generator():
   blk = Block()
   blk.add(Disp('clk'))
   blk.add(Disp('enable'))
   blk.add(Disp('is_signed'))
   blk.add(Disp('enacc'))
   blk.add(Disp('sub_nadd'))
   blk.add(Disp('selacc'))
   blk.add(Disp('resetrs0'))
   blk.add(Disp('rs0'))
   blk.add(Disp('rs1'))
   blk.add(Disp('imm'))
   blk.add(Disp('mulmux'))
   blk.add(Disp('selop0'))
   blk.add(Disp('selop1'))
   blk.add(Disp('selshift'))
   blk.add(Disp('cmode'))
   blk.add(Disp('opcode1'))
   blk.add(Disp('opcode2'))
   blk.add(Disp('out_en'))
   blk.add(Disp('out'))
   return blk


# -*- python -*-
# To include in alu_dsp_tb.wave.py:

from wavedisp.ast import *


def generator():
    testbench = Hierarchy('alu_dsp_tb')
    inst = testbench.add(Hierarchy('alu_dsp'))
    inst.include('alu_dsp.wave.py')
    return testbench
""")


TEST_MODULE_1_REF = ("""
# -*- python -*-
# To include in mymod_tb.wave.py:

from wavedisp.ast import *


def generator():
   blk = Block()
   blk.add(Disp('reset_n'))
   blk.add(Disp('clock'))
   blk.add(Disp('test'))
   blk.add(Disp('clock2'))
   blk.add(Disp('m_master'))
   blk.add(Disp('s_slave'))
   for idx in range(X): # Update range value
      blk.add(Disp('m_big_array[idx]'))
   blk.add(Disp('m_simple_array'))
   blk.add(Disp('m_simple_array3'))
   return blk


# -*- python -*-
# To include in mymod_tb.wave.py:

from wavedisp.ast import *


def generator():
    testbench = Hierarchy('mymod_tb')
    inst = testbench.add(Hierarchy('mymod'))
    inst.include('mymod.wave.py')
    return testbench
""")


TEST_MODULE_2_REF = ("""
# -*- python -*-
# To include in testmod_tb.wave.py:

from wavedisp.ast import *


def generator():
   blk = Block()
   blk.add(Disp('srst'))
   blk.add(Disp('clk'))
   blk.add(Disp('itf1'))
   blk.add(Disp('itf2'))
   blk.add(Disp('insig1'))
   blk.add(Disp('insig2'))
   blk.add(Disp('insig3'))
   blk.add(Disp('insig4'))
   blk.add(Disp('outsig1'))
   blk.add(Disp('outsig2'))
   blk.add(Disp('another_srst'))
   blk.add(Disp('another_clock'))
   blk.add(Disp('oitf'))
   blk.add(Disp('outsig3'))
   return blk


# -*- python -*-
# To include in testmod_tb.wave.py:

from wavedisp.ast import *


def generator():
    testbench = Hierarchy('testmod_tb')
    inst = testbench.add(Hierarchy('testmod'))
    inst.include('testmod.wave.py')
    return testbench
""")


TEST_MODULE_3_REF = ("""
# -*- python -*-
# To include in testmod2_tb.wave.py:

from wavedisp.ast import *


def generator():
   blk = Block()
   blk.add(Disp('srst'))
   blk.add(Disp('clk'))
   blk.add(Disp('another_srst'))
   blk.add(Disp('another_clock'))
   blk.add(Disp('oitf[0]'))
   blk.add(Disp('oitf[1]'))
   blk.add(Disp('oitf[2]'))
   blk.add(Disp('outsig3[0]'))
   blk.add(Disp('outsig3[1]'))
   return blk


# -*- python -*-
# To include in testmod2_tb.wave.py:

from wavedisp.ast import *


def generator():
    testbench = Hierarchy('testmod2_tb')
    inst = testbench.add(Hierarchy('testmod2'))
    inst.include('testmod2.wave.py')
    return testbench
""")


TEST_MODULE_4_REF = ("""
# -*- python -*-
# To include in testmod3_tb.wave.py:

from wavedisp.ast import *


def generator():
   blk = Block()
   blk.add(Disp('srst'))
   blk.add(Disp('clk'))
   blk.add(Disp('another_srst'))
   blk.add(Disp('another_clock'))
   blk.add(Disp('oitf[0]'))
   blk.add(Disp('oitf[1]'))
   blk.add(Disp('oitf[2]'))
   blk.add(Disp('outsig3[0]'))
   blk.add(Disp('outsig3[1]'))
   return blk


# -*- python -*-
# To include in testmod3_tb.wave.py:

from wavedisp.ast import *


def generator():
    testbench = Hierarchy('testmod3_tb')
    inst = testbench.add(Hierarchy('testmod3'))
    inst.include('testmod3.wave.py')
    return testbench
""")


if __name__ == '__main__':
    unittest.main()
