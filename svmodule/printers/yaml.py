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

from .port_range import get_range
from .printerbase import PrinterBase


class Yaml(PrinterBase):
    """Returns yaml."""

    def getstr(self):

        strval = ""

        for p in self.pmod["ports"]:
            if p["interface"] is False:
                display_type = "wave"
            else:
                display_type = "interface"

            rng = get_range(p["unpacked"])

            if rng is None:
                if p["unpacked"] != "":
                    loop_var = "{}_index".format(p["name"])
                    strval += "- repeat: range(1,10) # Update range value\n"
                    strval += f"  var: {loop_var}\n"
                    strval += "  elements:\n"
                    strval += "    - {{display: {}, names: '{}\\[$({})\\]'}}\n".format(
                        display_type, p["name"], loop_var
                    )
                else:
                    strval += "- {{display: {}, names: {}}}\n".format(display_type, p["name"])
            else:
                for i in rng:
                    strval += f"- {{display: {display_type}, names: '{p['name']}\\[{i}\\]'}}\n"

        strval += (
            "\n# To include in bench_{0}.yaml:\n"
            "- hierarchy: /bench_{0}\n"
            "  elements:\n"
            "    - hierarchy: {0}_inst\n"
            "      elements:\n"
            "        - !include {0}.yaml"
        ).format(self.pmod["name"])

        return strval
