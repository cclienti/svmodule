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

    def __init__(self, moddict, indent_size=3):
        self.moddict = moddict
        self.isize = indent_size

    def __getitem__(self, key):
        """Explore PrinterBase subclasses."""

        for cls in PrinterBase.__subclasses__():
            if cls.__name__ == key:
                return cls(self.moddict.parsedModule, self.isize).getstr()

        return 'PrinterNotFound'
