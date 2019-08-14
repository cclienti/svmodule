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

from .parser import Parser


class ModDict(object):

    def __init__(self):
        self.parsedModule = {}

    def parse(self, str_to_parse):
        """Parse the str_to_parse string and fill an instance variable dict
        'parsedModule' with module name, list of parameters and list
        of ports.

        """
        parser = Parser(str_to_parse)
        self.parsedModule['name'] = parser.getModuleName()
        self.parsedModule['import'] = parser.getImportList()
        self.parsedModule['ports'] = parser.getPortsList()
        self.parsedModule['parameters'] = parser.getParametersList()

    def loads(self, strval):
        """Gets instance variables from a string.
        """

        self.parsedModule = eval(strval)

    def stores(self):
        """Returns a string filled with instance variables."""
        return str(self.parsedModule)

    def load(self, filename):
        """Load from file the values of instance variable."""

        f = open(filename, 'r')
        self.loads(f.read())
        f.close()

    def store(self, filename):
        """Store to file the values of instance variable."""

        f = open(filename, 'w')
        f.write(self.stores())
        f.close()

    def reverse(self):
        """Reverse Inputs and Outputs directions in ports.
        """

        for i in range(len(self.parsedModule['ports'])):
            port = self.parsedModule['ports'][i]

            if port['direction'] == 'input':
                port['direction'] = 'output'

            elif port['direction'] == 'output':
                port['direction'] = 'input'

            self.parsedModule['ports'][i] = port
