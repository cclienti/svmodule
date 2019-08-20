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

"""Test AST classes."""

import os
import unittest

from svmodule.moddict import ModDict

from . import test_printers_inputs as inputs


class TestPastAsInstance(unittest.TestCase):
    """Test class svmodule Printers."""

    def test_parser_0(self):
        """Test parser with TEST_MODULE_0"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)
        stores = moddict.stores()

        self.assertEqual(eval(stores), TEST_MODULE_0_REF)

    def test_parser_1(self):
        """Test parser with TEST_MODULE_1"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_1)
        stores = moddict.stores()

        self.assertEqual(eval(stores), TEST_MODULE_1_REF)

    def test_parser_2(self):
        """Test parser with TEST_MODULE_2"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_2)
        stores = moddict.stores()

        self.assertEqual(eval(stores), TEST_MODULE_2_REF)

    def test_parser_3(self):
        """Test parser with TEST_MODULE_3"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_3)
        stores = moddict.stores()
        print(stores)
        self.assertEqual(eval(stores), TEST_MODULE_3_REF)

    def test_parser_4(self):
        """Test parser with TEST_MODULE_4"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_4)
        stores = moddict.stores()

        self.assertEqual(eval(stores), TEST_MODULE_4_REF)

    def test_load_store(self):
        """Test parser 'load' and 'store' methods"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        filename = '__test_load_store.txt'

        moddict.store(filename)
        moddict2 = ModDict()
        moddict2.load(filename)

        self.assertEqual(eval(moddict2.stores()), TEST_MODULE_0_REF)

        os.remove(filename)

    def test_loads_stores(self):
        """Test parser 'loads' and 'stores' methods"""
        moddict = ModDict()
        moddict.parse(inputs.TEST_MODULE_0)

        stores = moddict.stores()
        moddict2 = ModDict()
        moddict2.loads(stores)

        self.assertEqual(stores, moddict2.stores())



TEST_MODULE_0_REF = {
    'name': 'alu_dsp',
    'import': [],
    'ports': [{'interface': False, 'type': '', 'direction': 'input', 'name': 'clk',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'enable',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'is_signed',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'enacc',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'sub_nadd',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'selacc',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'resetrs0',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'rs0',
               'packed': '[31:0]', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'rs1',
               'packed': '[31:0]', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'imm',
               'packed': '[31:0]', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'mulmux',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'selop0',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'selop1',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'selshift',
               'packed': '[1:0]', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'cmode',
               'packed': '[1:0]', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'opcode1',
               'packed': '[2:0]', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'input', 'name': 'opcode2',
               'packed': '[2:0]', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'output', 'name': 'out_en',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': '', 'direction': 'output', 'name': 'out',
               'packed': '[31:0]', 'unpacked': ''}],
    'parameters': [{'type': '', 'name': 'add_extra_instr', 'value': '1',
                    'packed': '', 'unpacked': ''},
                   {'type': '', 'name': 'add_select_instr', 'value': '1',
                    'packed': '', 'unpacked': ''},
                   {'type': 'string', 'name': 'add_select_instr', 'value': '"M144k,auto"',
                    'packed': '', 'unpacked': ''},
                   {'type': '', 'name': 'shorten_pipeline', 'value': '0',
                    'packed': '', 'unpacked': ''}]
}


TEST_MODULE_1_REF = {
    'name': 'mymod',
    'import': [],
    'ports': [{'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'reset_n',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'clock',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'test',
               'packed': '[$clog2(GEN3_WIDTH+1)-1:0]', 'unpacked': ''},
              {'interface': False, 'type': 'pkg::typedef', 'direction': 'input', 'name': 'clock2',
               'packed': '', 'unpacked': ''},
              {'interface': True, 'type': 'myinterface', 'direction': 'master', 'name': 'm_master',
               'packed': '', 'unpacked': ''},
              {'interface': True, 'type': 'myinterface', 'direction': 'slave', 'name': 's_slave',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'output', 'name': 'm_big_array',
               'packed': '[28:0][$clog2(GEN1):0]', 'unpacked': '[1:0][2:0]'},
              {'interface': False, 'type': 'logic', 'direction': 'output', 'name': 'm_simple_array',
               'packed': '[15:0]', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'output', 'name': 'm_simple_array3',
               'packed': '[15:0]', 'unpacked': ''}],
    'parameters': [{'type': '', 'name': 'GEN1', 'value': '48', 'packed': '', 'unpacked': ''},
                   {'type': '', 'name': 'GEN2', 'value': '45', 'packed': '', 'unpacked': ''},
                   {'type': '', 'name': 'GEN3_WIDTH', 'value': '$clog2(VALUE)', 'packed': '', 'unpacked': ''},
                   {'type': '', 'name': 'DEFAULT_VAL_A', 'value': "32'b0", 'packed': '[31:0]', 'unpacked': ''},
                   {'type': 'int', 'name': 'DEFAULT_VAL_B', 'value': "32'b0", 'packed': '[31:0]', 'unpacked': ''},
                   {'type': '', 'name': 'DEFAULT_VAL_C', 'value': '', 'packed': '[31:0]', 'unpacked': '[1:0]'}]
}


TEST_MODULE_2_REF = {
    'name': 'testmod',
    'import': [],
    'ports': [{'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'srst',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'clk',
               'packed': '', 'unpacked': ''},
              {'interface': True, 'type': 'myinterface', 'direction': 'slave', 'name': 'itf1',
               'packed': '', 'unpacked': ''},
              {'interface': True, 'type': 'myinterface', 'direction': 'master', 'name': 'itf2',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'insig1',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'insig2',
               'packed': '[31:0]', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'insig3',
               'packed': '[10:0]', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'insig4',
               'packed': '[7:0]', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'output', 'name': 'outsig1',
               'packed': '[47:0]', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'output', 'name': 'outsig2',
               'packed': '[15:0]', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'another_srst',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'another_clock',
               'packed': '', 'unpacked': ''},
              {'interface': True, 'type': 'otherinterface', 'direction': 'slave', 'name': 'oitf',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'output', 'name': 'outsig3',
               'packed': '', 'unpacked': ''}],
    'parameters': []
}


TEST_MODULE_3_REF = {
    'name': 'testmod2',
    'import': [],
    'ports': [{'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'srst',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'clk',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'another_srst',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'another_clock',
               'packed': '', 'unpacked': ''},
              {'interface': True, 'type': 'otherinterface', 'direction': 'slave', 'name': 'oitf',
               'packed': '', 'unpacked': '[2:0]'},
              {'interface': False, 'type': 'logic', 'direction': 'output', 'name': 'outsig3',
               'packed': '', 'unpacked': '[1:0]'}],
    'parameters': []
}


TEST_MODULE_4_REF = {
    'name': 'testmod3',
    'import': ['pkg1::test', 'pkg2::test2', 'pkg3::*'],
    'ports': [{'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'srst',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'clk',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'another_srst',
               'packed': '', 'unpacked': ''},
              {'interface': False, 'type': 'logic', 'direction': 'input', 'name': 'another_clock',
               'packed': '', 'unpacked': ''},
              {'interface': True, 'type': 'otherinterface', 'direction': 'slave', 'name': 'oitf',
               'packed': '', 'unpacked': '[2:0]'},
              {'interface': False, 'type': 'logic', 'direction': 'output', 'name': 'outsig3',
               'packed': '', 'unpacked': '[1:0]'}],
    'parameters': []
}


if __name__ == '__main__':
    unittest.main()
