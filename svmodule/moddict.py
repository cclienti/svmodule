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
"""SVModule [System]Verilog Module Dictionary."""

import json

from .parser import Parser


class ModDict:
    """Module dictionary that contains parsed elements."""

    def __init__(self):
        self.parsed_module = {}

    def parse(self, str_to_parse: str) -> None:
        """Parse str_to_parse and populate parsed_module with name,
        parameters, ports and import list.
        """
        parser = Parser(str_to_parse)
        self.parsed_module["name"] = parser.get_module_name()
        self.parsed_module["import"] = parser.get_import_list()
        self.parsed_module["ports"] = parser.get_ports_list()
        self.parsed_module["parameters"] = parser.get_parameters_list()

    def loads(self, strval: str) -> None:
        """Populate parsed_module from a JSON string."""
        self.parsed_module = json.loads(strval)

    def stores(self) -> str:
        """Return parsed_module serialised as a JSON string."""
        return json.dumps(self.parsed_module)

    def load(self, filename: str) -> None:
        """Load parsed_module from a JSON file."""
        with open(filename, encoding="utf-8") as fdesc:
            self.loads(fdesc.read())

    def store(self, filename: str) -> None:
        """Store parsed_module to a JSON file."""
        with open(filename, "w", encoding="utf-8") as fdesc:
            fdesc.write(self.stores())

    def reverse(self) -> None:
        """Reverse input/output directions in ports."""
        for i, port in enumerate(self.parsed_module["ports"]):
            if port["direction"] == "input":
                port["direction"] = "output"
            elif port["direction"] == "output":
                port["direction"] = "input"
            self.parsed_module["ports"][i] = port
