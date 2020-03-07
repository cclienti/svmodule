#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of svmodule. See the root README for further
# informations.
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
# Copyright (C) 2013-2019 Christophe Clienti
"""SVModule [System]Verilog Module Dictionary."""

from .parser import Parser


class ModDict:
    """Module dictionary that contains parsed elements."""

    def __init__(self):
        self.parsed_module = {}

    def parse(self, str_to_parse):
        """Parse the str_to_parse string and fill an instance variable dict
        'parsed_module' with module name, list of parameters and list
        of ports.

        """
        parser = Parser(str_to_parse)
        self.parsed_module['name'] = parser.get_module_name()
        self.parsed_module['import'] = parser.get_import_list()
        self.parsed_module['ports'] = parser.get_ports_list()
        self.parsed_module['parameters'] = parser.get_parameters_list()

    def loads(self, strval):
        """Gets instance variables from a string.
        """

        self.parsed_module = eval(strval)

    def stores(self):
        """Returns a string filled with instance variables."""
        return str(self.parsed_module)

    def load(self, filename):
        """Load from file the values of instance variable."""

        fdesc = open(filename, 'r')
        self.loads(fdesc.read())
        fdesc.close()

    def store(self, filename):
        """Store to file the values of instance variable."""

        fdesc = open(filename, 'w')
        fdesc.write(self.stores())
        fdesc.close()

    def reverse(self):
        """Reverse Inputs and Outputs directions in ports.
        """

        for i in range(len(self.parsed_module['ports'])):
            port = self.parsed_module['ports'][i]

            if port['direction'] == 'input':
                port['direction'] = 'output'

            elif port['direction'] == 'output':
                port['direction'] = 'input'

            self.parsed_module['ports'][i] = port
