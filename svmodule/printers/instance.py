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

from .printerbase import PrinterBase
from .align import vertical_align_string


class Instance(PrinterBase):
    """Returns the instance of the module.
    """

    def getParameters(self):
        """Returns a string with the list of parameters used within a
        module instance. If there is no parameters, it will return an
        empty string.
        """
        idt = ' ' * self.isize

        params = self.pmod['parameters']
        nbparams = len(params)

        strval = ''

        if nbparams != 0:
            for i in range(nbparams-1):
                p = params[i]
                strval += idt*2 + '.' + p['name'] + ' (' + p['name'] + '),\n'

            p = params[nbparams-1]
            strval += idt*2 + '.' + p['name'] + ' (' + p['name'] + ')'

            strval = vertical_align_string(strval, align_char='(', nbspaces=0)

            strval = idt + '#(\n' + strval
            strval += '\n' + idt + ')'

        return strval

    def getPorts(self):
        """Returns a string with the list of ports to be used in a
        module instance. If there is no ports, it will return only
        "();".
        """
        idt = ' ' * self.isize

        ports = self.pmod['ports']
        nbports = len(ports)

        strval = ''

        if nbports != 0:
            for i in range(nbports-1):
                p = ports[i]
                strval += idt*2 + '.' + p['name'] + ' (' + p['name'] + '),\n'

            p = ports[nbports-1]
            strval += idt*2 + '.' + p['name'] + ' (' + p['name'] + ')'

            strval = vertical_align_string(strval, align_char='(', nbspaces=0)

            strval = idt + '(\n' + strval
            strval += '\n' + idt + ');'

        return strval

    def getstr(self):
        idt = ' ' * self.isize

        modname = self.pmod['name']

        strval = idt + modname

        # Insert parameters
        params = self.getParameters()
        if params != '':
            strval += '\n' + params + '\n' + idt
        else:
            strval += ' '

        # Insert strval name
        strval += modname + '_inst\n'

        # Insert ports
        strval += self.getPorts()
        strval += '\n'

        return strval
