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
# Copyright (C) 2014-2019 Christophe Clienti

from .printerbase import PrinterBase


class Logic(PrinterBase):
    """Returns ports of module as declaration of signals.
    """

    def getstr(self):

        idt = ' ' * self.isize
        strval = ''

        for p in self.pmod['ports']:
            if p['type'] == '':
                continue

            strval += idt
            strval += p['type'] + ' ' + p['packed']
            strval += ' ' + p['name'] + p['unpacked']

            # In case of interface, we must add a '()'
            if p['interface'] is True:
                strval += '()'

            strval += ';\n'

        return strval
