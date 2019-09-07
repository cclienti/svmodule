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

"""Wavedisp printer."""

from .printerbase import PrinterBase
from .port_range import get_range


class Wavedisp(PrinterBase):
    """Wavedisp printer."""

    def getstr(self):
        """Return the generated string."""

        idt = ' ' * self.isize

        strval = '\n'.join(['# -*- python -*-',
                            '# To include in {0}_tb.wave.py:',
                            '"""Wavedisp file for module {0}."""',
                            '',
                            'from wavedisp.ast import Hierarchy',
                            'from wavedisp.ast import Group',
                            'from wavedisp.ast import Block',
                            'from wavedisp.ast import Disp',
                            'from wavedisp.ast import Divider',
                            '',
                            '',
                            'def generator():',
                            idt + '"""Generator for module {0}."""',
                            '']).format(self.pmod['name'])

        strval += idt + 'blk = Block()\n'

        for prn in self.pmod['ports']:
            rng = get_range(prn['unpacked'])

            if rng is None:
                if prn['unpacked'] != '':
                    strval += idt + 'for idx in range(X): # Update range value\n'
                    strval += 2 * idt + 'blk.add(Disp(\'{}[idx]\'))\n'.format(prn['name'])
                else:
                    strval += idt + 'blk.add(Disp(\'{}\'))\n'.format(prn['name'])
            else:
                for idx in rng:
                    strval += idt + 'blk.add(Disp(\'{}[{}]\'))\n'.format(prn['name'], idx)

        strval += idt + 'return blk\n'

        strval += '\n\n'

        strval += '\n'.join(['# -*- python -*-',
                             '# To include in {0}_tb.wave.py:',
                             '"""Wavedisp file for module {0}_tb."""',
                             '',
                             'from wavedisp.ast import Hierarchy',
                             'from wavedisp.ast import Group',
                             'from wavedisp.ast import Block',
                             'from wavedisp.ast import Disp',
                             'from wavedisp.ast import Divider',
                             '',
                             '',
                             'def generator():',
                             idt + '"""Generator for module {0}_tb."""',
                             idt + 'testbench = Hierarchy(\'{0}_tb\')',
                             idt + 'inst = testbench.add(Hierarchy(\'{0}\'))',
                             idt + 'inst.include(\'{0}.wave.py\')',
                             idt + 'return testbench',
                             '']).format(self.pmod['name'])

        return strval
