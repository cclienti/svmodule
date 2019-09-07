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


class ClockingBlock(PrinterBase):
    """
    Returns the clocking block
    """
    clock_patterns = ('clock', 'clk')

    reset_patterns = (('sreset_n', ''),
                      ('sresetn', ''),
                      ('srst_n', ''),
                      ('srstn', ''),
                      ('sreset', ''),
                      ('srst', ''),
                      ('reset_n', 'negedge'),
                      ('resetn', 'negedge'),
                      ('rst_n', 'negedge'),
                      ('rstn', 'negedge'),
                      ('reset', 'posedge'),
                      ('rst', 'posedge'))

    def search_input_clock(self):
        """
        Search for a clock in the port list.
        Returns the clock name
        """

        for port in self.pmod['ports']:
            if port['direction'] == 'input':
                for clk_name in self.clock_patterns:
                    if clk_name in port['name'].lower():
                        return port['name']

        return None

    def search_input_reset(self):
        """
        Search for a reset in the port list.
        Returns ('negedge' | 'posedge', | ''), reset_name
        """

        for port in self.pmod['ports']:
            if port['direction'] == 'input':
                for rst_name, edge_value in self.reset_patterns:
                    if rst_name in port['name'].lower():
                        return (edge_value, port['name'])

        return (None, None)

    def getstr(self):
        """Return clockingblock string."""
        idt = ' ' * self.isize

        clockname = self.search_input_clock()
        resetname = self.search_input_reset()

        strval = idt + 'default clocking cb '
        if clockname is None:
            strval += '@(posedge INSERT_CLOCK_HERE);\n'
        else:
            strval += '@(posedge ' + clockname + ');\n'

        for port in self.pmod['ports']:
            if clockname == port['name'] and port['direction'] == 'input':
                pass
            elif resetname[1] == port['name'] and port['direction'] == 'input':
                strval += 2 * idt + 'output ' + resetname[0] + ' ' + resetname[1] + ';\n'
            else:
                if port['direction'] == 'input':
                    strval += 2 * idt + 'output ' + port['name'] + ';\n'
                elif port['direction'] == 'output':
                    strval += 2 * idt + 'input ' + port['name'] + ';\n'
                else:
                    # TODO it's not valid to add an interface.
                    # We must list all the interface's members and assign them accordingly.
                    strval += 2 * idt + '//' + port['direction'] + ' ' + port['name'] + ';\n'

        strval += idt + 'endclocking\n'

        return strval
