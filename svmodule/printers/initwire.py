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


class InitWire(PrinterBase):
    """Returns a string with the list of input ports initialized
    to zero using '=' token.
    """

    def getstr(self):
        idt = ' ' * self.isize

        strval = ''

        for p in self.pmod['ports']:
            if p['direction'] == 'input':
                strval += idt

                strval += 'assign '

                strval += p['name'] + ' = '

                if p['packed'] == '' and p['unpacked'] == '':
                    strval += '1\'b0'
                else:
                    strval += '\'0'

                strval += ";\n"

        return vertical_align_string(strval, align_char = '=', nbspaces = 0)
