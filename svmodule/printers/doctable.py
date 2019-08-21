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


class DocTable(PrinterBase):
    """Returns a sphynx table with ports information.
    """

    def align_str_in_list(self, column):
        """Search for the longest string in the given list.

        It returns a tuple containing the string list with whitespaces
        to ensure that all string have the same length and the size+1
        of the longest string.
        """

        maxstr = len(max(column, key=len)) + 1

        l = []
        for strval in column:
            strval += ' ' * (maxstr - len(strval))
            l.append(strval)

        return (maxstr, l)

    def getparameters(self):
        if not self.pmod['parameters']:
            return ''

        param_name = ['Name']
        param_type = ['Type']
        param_value = ['Default value']

        for p in self.pmod['parameters']:
            param_name.append(p['name'])
            param_type.append(p['type'])
            param_value.append(p['value'])

        (len_name, param_name) = self.align_str_in_list(param_name)
        (len_type, param_type) = self.align_str_in_list(param_type)
        (len_value, param_value) = self.align_str_in_list(param_value)

        thickline = '='*len_name + '  '
        thickline += '='*len_type + '  '
        thickline += '='*len_value + '  '
        thickline += '='*40

        thinline = '-'*len_name + '  '
        thinline += '-'*len_type + '  '
        thinline += '-'*len_value + '  '
        thinline += '-'*40

        # Print title

        strval = thickline + '\n'
        strval += param_name[0] + '  '
        strval += param_type[0] + '  '
        strval += param_value[0] + '  '
        strval += 'Description\n'
        strval += thickline + '\n'

        for i in range(len(param_name)-1):
            strval += param_name[i+1] + '  '
            strval += param_type[i+1] + '  '
            strval += param_value[i+1] + '  ' + '\n'
            if i == len(param_name)-2:
                strval += thickline + '\n'
            else:
                strval += thinline + '\n'

        return strval + '\n'

    def getsignals(self):
        if not self.pmod['ports']:
            return ''

        # prepare tables columns
        signame = ['Name']
        sigdir = ['I/O type']
        sigrange = ['Range']

        for p in self.pmod['ports']:
            signame.append(p['name'])

            if p['interface'] is True:
                sigdir.append("%s.%s" % (p['type'], p['direction']))
            else:
                sigdir.append("%s %s" % (p['direction'], p['type']))

            if p['unpacked'] != '':
                sigrange.append(p['unpacked'])

            if p['packed'] != '':
                sigrange.append(p['packed'])
            else:
                if p['unpacked'] == '':
                    sigrange.append('1')

        (lenname, signame) = self.align_str_in_list(signame)
        (lendir, sigdir) = self.align_str_in_list(sigdir)
        (lenrange, sigrange) = self.align_str_in_list(sigrange)

        thickline = '='*lenname + '  '
        thickline += '='*lendir + '  '
        thickline += '='*lenrange + '  '
        thickline += '='*40

        thinline = '-'*lenname + '  '
        thinline += '-'*lendir + '  '
        thinline += '-'*lenrange + '  '
        thinline += '-'*40

        # Print title

        strval = thickline + '\n'
        strval += signame[0] + '  '
        strval += sigdir[0] + '  '
        strval += sigrange[0] + '  '
        strval += 'Description\n'
        strval += thickline + '\n'

        for i in range(len(signame)-1):
            strval += signame[i+1] + '  '
            strval += sigdir[i+1] + '  '
            strval += sigrange[i+1] + '  ' + '\n'
            if i == len(signame)-2:
                strval += thickline + '\n'
            else:
                strval += thinline + '\n'

        return strval

    def getstr(self):
        return self.getparameters() + self.getsignals()
