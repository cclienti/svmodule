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


class Signals(PrinterBase):
    """Returns ports of module as declaration of signals.
    """

    def getstr(self):

        idt = ' ' * self.isize

        strval = ''

        for p in self.pmod['ports']:
            if p['interface'] is True:
                continue

            strval += idt

            # if p['type'] == '':
            #     if p['direction'] == 'output':
            #         strval += 'wire'
            #     else:
            #         strval += 'reg'
            # elif p['type'] == 'wire':
            #     strval += 'reg'
            # elif p['type'] == 'reg':
            #     strval += 'wire'
            # else:
            #     strval += p['type']

            if p['direction'] == 'output':
                strval += 'wire'
            else:
                strval += 'reg'

            if p['packed'] != '':
                strval += ' ' + p['packed']

            strval += ' ' + p['name']

            if p['packed'] != '':
                strval += ' ' + p['packed']

            strval += '' + p['unpacked']
            strval += ';\n'

        return strval
