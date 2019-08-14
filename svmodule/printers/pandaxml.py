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
from .port_range import get_range


class PandaXml(PrinterBase):
    template = """
    <cell>
      <name>{module_name}</name>
      <operation operation_name="{module_name}" bounded="0"/>
      <circuit>
        <component_o id="{module_name}">
          <description>{module_name} IP</description>
          <copyright>foo</copyright>
          <authors>foo</authors>
          <license>foo</license>
          <structural_type_descriptor id_type="{module_name}"/>

{ports}
          <NP_functionality LIBRARY="{module_name}"
                            VERILOG_FILE_PROVIDED="{module_name}.v"/>
        </component_o>
      </circuit>
    </cell>
    """

    @staticmethod
    def port_declaration(port):
        port_name = port['name']
        port_dir = 'IN' if port['direction'] == 'input' else 'OUT'

        if port['packed'] != '':
            port_width = len(get_range(port['packed']))
            port_type = 'UINT'
        else:
            port_width = 1
            port_type = 'BOOL'

        port_str = '          <port_o id="%s" dir="%s"' % (port_name, port_dir)
        if 'clock' in port_name:
            port_str += ' is_clock="1">\n'
        else:
            port_str += '>\n'

        port_str += '            <structural_type_descriptor type="%s" size="%s"/>\n' % (port_type, port_width)
        port_str += '          </port_o>\n'

        return port_str

    def getstr(self):
        strval = PandaXml.template.replace('{module_name}', self.pmod['name'])

        ports_str = ''
        for p in self.pmod['ports']:
            ports_str += PandaXml.port_declaration(p)

        strval = strval.replace('{ports}', ports_str)

        return strval
