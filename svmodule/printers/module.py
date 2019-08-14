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


class Module(PrinterBase):
    """Returns the reformatted module string given in the
    constructor.
    """

    def getImportPackages(self, indentSize=3):
        """
        Returns a string with the list of package to import within
        the module decalration.
        """

        idt = ' ' * indentSize

        pkgs = self.pmod['import']
        nbpkgs = len(pkgs)

        strval = ''

        if nbpkgs != 0:
            strval = idt + 'import '
            for i in range(nbpkgs):
                strval += pkgs[i]

                if i == (nbpkgs-1):
                    strval += ';'
                else:
                    strval += ',\n' + idt + ' '*7

        return strval

    def getParameters(self, indentSize=3):
        """Returns a string with the list of parameters to be used in
        a module declaration. It will return an empty string if there
        is no parameters in the module.
       """
        idt = ' ' * indentSize

        params = self.pmod['parameters']
        nbparams = len(params)

        strval = ''

        if nbparams != 0:
            for i in range(nbparams):
                p = params[i]

                if p['type'] == '' and p['packed'] == '' and p['unpacked'] == '' and p['value'] == '': continue

                strval += idt
                strval += 'parameter'

                if p['type'] != '':
                    strval += ' ' + p['type']

                if p['packed'] != '':
                    strval += ' ' + p['packed']

                strval += ' ' + p['name']

                if p['unpacked'] != '':
                    strval += ' ' + p['unpacked']

                if p['value'] != '':
                    strval += ' = ' + p['value']

                if i != (nbparams-1):
                    strval += ',\n'

            strval = vertical_align_string(strval, align_char='=', nbspaces=0)

            strval = '#(\n' + strval
            strval += '\n)'

        return strval

    def getPorts(self, indentSize=3):
        """Returns a string with the list of ports to be used in a
        module declaration, if list is empty, it will return "();".
       """
        idt = ' ' * indentSize

        ports = self.pmod['ports']
        nbports = len(ports)

        strval = ''

        if nbports != 0:
            for i in range(nbports):
                p = ports[i]

                strval += idt

                if p['interface']:
                    strval += p['type'] + '.' + p['direction']
                else:
                    strval += p['direction'] + ' ' + p['type']

                strval += ' ' + p['packed'] + ' ' + p['name'] + p['unpacked']

                if i != (nbports-1):
                    strval += ',\n'

            strval = '(\n' + strval
            strval += '\n);'

        return strval

    def getstr(self, indentSize=3):
        modname = self.pmod['name']

        strval = 'module ' + modname + '\n'

        # Insert import of packages
        pkgs = self.getImportPackages(indentSize)
        if pkgs != '':
            strval += pkgs + '\n'

        # Insert parameters
        params = self.getParameters(indentSize)
        if params != '':
            strval += params + '\n'

        # Insert ports
        strval += self.getPorts(indentSize)
        strval += '\n'

        return strval
