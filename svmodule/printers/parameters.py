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


class Parameters(PrinterBase):
    """Returns a string with the list of parameter initialized as
    localparam with the module values. If there is no parameters,
    it returns an empty string.
    """

    def getstr(self):

        idt = ' ' * self.isize

        strval = ''

        for p in self.pmod['parameters']:
            strval += idt + 'localparam'

            if p['type'] != '':
                strval += ' ' + p['type']

            if p['packed'] != '':
                strval += ' ' + p['packed']

            strval += ' ' + p['name']

            if p['value'] != '':
                strval += ' = ' + p['value']

            strval += ';\n'

        return vertical_align_string(strval, align_char = '=', nbspaces = 0)
