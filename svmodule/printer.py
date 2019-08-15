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

from .moddict import ModDict

from .printers import PrinterBase


class Printer(object):
    """Base printer class, it aims to be inherited to implement specific
    printers. See module printers.
    """

    def __init__(self, moddict, indentSize = 3):
        self.moddict = moddict
        self.isize = indentSize

    def __getitem__(self, key):
        # explore PrinterBase subclasses
        for cls in PrinterBase.__subclasses__():
            if cls.__name__ == key:
                return cls(self.moddict.parsedModule, self.isize).getstr()
        return 'PrinterNotFound'



def test(teststr):
    moddict1 = ModDict()
    moddict1.parse(teststr)
    first = Printer(moddict1)

    moddict2 = ModDict()
    moddict2.parse(first['Module'])
    second = Printer(moddict2)

    if first['Module'] == second['Module']:
        print('Module test: \tok')
    else:
        print('Module test: \tko!')

    if first['Instance'] == second['Instance']:
        print('Instance test: \tok')
    else:
        print('Instance test: \tko!')

    if first['Signals'] == second['Signals']:
        print('Signals test: \tok')
    else:
        print('Signals test: \tko!')

    if first['Parameters'] == second['Parameters']:
        print('Params test: \tok')
    else:
        print('Params test: \tko!')

    return


def main():
    from test import teststrings
    for s in teststrings:
        print("\n---> test using:\n")
        print(s + "\n")
        test(s)
        print("\n")


    moddict = ModDict()
    moddict.parse(teststrings[2])
    moddict.store("/tmp/toto")

    moddict2 = ModDict()
    moddict.load("/tmp/toto")
    print(teststrings[2])
    x = Printer(moddict2)

    # print(x['ModuleName'])
    # print(x['Parameters'])
    # print(x['Instance'])
    print(x['Module'])
    # print(x['Signals'])
    # print(x['InitWire'])
    # print(x['InitLatch'])
    # print(x['DocTable'])

    # moddict2.reverse()
    # print(x['DocTable'])


if __name__ == "__main__":
    main()
