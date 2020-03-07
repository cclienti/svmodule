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

import re


class ParserHelper:
    @staticmethod
    def is_range(strval):
        """Returns True if the string is a SystemVerilog range.
        """
        if re.search(r'\[.*\]', strval) is not None:
            return True
        else:
            return False

    @staticmethod
    def is_interface(strval):
        """Returns True if the strval describes an interface with a
        module port definition.
        """

        if len(strval) == 0:
            return False

        x = re.split(r' ', strval)[0]

        if x == ("input"):
            return False
        elif x == "output":
            return False
        elif x == "inout":
            return False
        elif x == "ref":
            return False
        else:
            return True

    @staticmethod
    def get_arrays(strval):
        """Returns arrays range(s).
        """
        # add @ around ranges to split by space
        strval = re.sub(r'[ ]*\[', r'@[', strval)
        lval = re.split(r'@', strval)

        # iterates over lval to get each range
        strarrays = ''
        for l in lval:
            if ParserHelper.is_range(l):
                strarrays += l

        return strarrays

    @staticmethod
    def remove_arrays(strval):
        """Returns a string without range(s).
        """
        # add @ around ranges to split by space
        strval = re.sub(r'[ ]*\[', r'@[', strval)
        lval = re.split(r'@', strval)

        if type(lval) is None:
            return ''

        return lval[0]

    @staticmethod
    def get_name_and_type(strval):
        """Returns name and type of a string like:
             - "int [31:0] GEN [31:0]" =>
                   ('int [31:0]', 'GEN [31:0]')

             - "output logic name" =>
                   ('output logic', 'name')

             - "interface.slave name" =>
                   ('interface.slave', 'name')
         """
        x = re.split(' ', strval)

        p_name = ''
        for i in range(len(x)):
            v = x.pop()
            if ParserHelper.is_range(v):
                p_name = v + p_name
            else:
                x.append(v)
                break

        if len(x) != 0:
            p_name = x.pop() + p_name

        if len(x) != 0:
            p_type = ' '.join(x)
        else:
            p_type = ''

        return p_type, p_name

    @staticmethod
    def remove_multiline_comments(strval):
        state = 0
        strnew = ''
        L = len(strval)

        for i in range(L):
            if i < (L-1):
                if strval[i] == '/' and strval[i+1] == '*':
                    state = 1

            if i > 1:
                if strval[i-2] == '*' and strval[i-1] == '/':
                    state = 0

            if state == 0:
                strnew += strval[i]
        return strnew


class Parser:
    def parse_block(self, strval):
        i = 0
        k = 0

        condition = True

        while condition:
            if strval[i] == '(':
                k = k + 1
            elif strval[i] == ')':
                k = k - 1

            i = i + 1

            if k <= 0:
                condition = False

        return (strval[:i], strval[i:])

    def parse_import_list(self):
        """Returns a list of import packages"""
        return []

    def parse_parameters_list(self):
        """Returns a list of dictionnaries with parameter type,
        name and value.
        """

        # get Parameter block without parenthesis
        x = self.parameters_str[1:-1]

        # remove parameter
        x = re.sub(r'[ ]*parameter[ ]*', r'', x)

        # protect comma in quotes
        in_quotes_re = re.compile('("[^"]+")')
        x = in_quotes_re.sub(lambda match: match.group().replace(",", "\x00"), x)

        # Split parameters list
        params = re.split(',', x)

        parameters_list = []

        for p in params:
            # Restore comma in quotes
            x = re.sub("\x00", ",", p)

            # Extract param default value
            x = re.split('=', x)
            if len(x) > 1:
                p_value = x[1]
            else:
                p_value = ''

            x = x[0]

            # Extract type and name
            p_type, p_name = ParserHelper.get_name_and_type(x)

            p_packed_arrays = ParserHelper.get_arrays(p_type)
            p_unpacked_arrays = ParserHelper.get_arrays(p_name)

            p_type = ParserHelper.remove_arrays(p_type)
            p_name = ParserHelper.remove_arrays(p_name)

            if p_type == '' and p_name == '' and p_value == '':
                if p_packed_arrays == '' and p_unpacked_arrays == '':
                    continue

            parameters_list.append({'type': p_type,
                                    'name': p_name,
                                    'value': p_value,
                                    'packed': p_packed_arrays,
                                    'unpacked': p_unpacked_arrays})

        return parameters_list

    def parse_ports_list(self):
        """Returns a list of dictionnaries with port direction,
        is_interface, packed array range(s), unpacked array range(s),
        type and name.
        """
        # get Parameter block without parenthesis
        x = self.ports_str[1:-1]

        ports = re.split(',', x)
        ports_list = []
        p_type_prev = ''

        for p in ports:
            # Extract type and name
            p_type, p_name = ParserHelper.get_name_and_type(p)

            # if p_type is empty, it must be taken from the previous
            # port.
            if p_type == '':
                p_type = p_type_prev
            else:
                p_type_prev = p_type

            p_packed_arrays = ParserHelper.get_arrays(p_type)
            p_unpacked_arrays = ParserHelper.get_arrays(p_name)

            p_type = ParserHelper.remove_arrays(p_type)
            p_name = ParserHelper.remove_arrays(p_name)

            if ParserHelper.is_interface(p_type):
                p_is_insterface = True
                # extract the identifier after the dot* (within
                # interface port type)
                p_dir = re.sub(r'.*\.([a-zA-Z_][a-zA-Z_0-9]*).*',
                               r'\1',
                               p_type)

                # remove the dot and the following indentifier
                p_type = re.sub(r'(.*)\.[a-zA-Z_][a-zA-Z_0-9]*[ ]*(.*)',
                                r'\1 \2',
                                p_type)

                p_type = re.sub(r'[ ]*$', '', p_type)

            else:
                p_is_insterface = False
                # extract direction
                p_dir = re.sub(r'([a-zA-Z_][a-zA-Z_0-9]*)[ ]*.*', r'\1', p_type)
                # extract type
                p_type = re.sub(r'[a-zA-Z_][a-zA-Z_0-9]*[ ]*(.*)', r'\1', p_type)

            ports_list.append({'interface': p_is_insterface,
                               'type': p_type,
                               'direction': p_dir,
                               'name': p_name,
                               'packed': p_packed_arrays,
                               'unpacked': p_unpacked_arrays})

        return ports_list

    def __init__(self, module_string):
        # remove one line comments
        modstr = re.sub(r'//.*[\n\r]', r'', module_string)

        # flatten the string module
        modstr = re.sub(r'[ \n\r\t]+', r' ', modstr)

        # remove multiline comments
        # pattern = re.compile(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        #                      re.DOTALL | re.MULTILINE)
        # modstr = re.sub(pattern, r'', modstr)
        modstr = ParserHelper.remove_multiline_comments(modstr)

        # remove everithing before module
        modstr = re.sub(r'(^|.*[ ])module ', r'module ', modstr)

        # remove everithing after the end of the module declaration
        modstr = re.sub(r'\);.*$', r');', modstr)

        # prepare the string to be parsed
        modstr = re.sub(r'[ ]*=[ ]*', '=', modstr)
        modstr = re.sub(r'[ ]*\([ ]*', '(', modstr)
        modstr = re.sub(r'[ ]*\)[ ]*', ')', modstr)
        modstr = re.sub(r'[ ]*\[[ ]*', ' [', modstr)
        modstr = re.sub(r'[ ]*\][ ]*', '] ', modstr)
        modstr = re.sub(r'[ ]*,[ ]*', ',', modstr)
        modstr = re.sub(r'[ ]*;[ ]*', ';', modstr)
        modstr = re.sub(r'[ ]*\);', ');', modstr)
        modstr = re.sub(r'[ ]*\)\(', ')(', modstr)

        # parse moduleName
        searchres = re.search('(?<=module )[a-zA-Z_][a-zA-Z_0-9]*', modstr)
        self.moduleNameStr = searchres.group(0)

        # remove module + moduleName
        modstr = re.sub(r'module [a-zA-Z_][a-zA-Z_0-9]*[ ]*', '', modstr)

        # search and remove optional header import
        self.import_list = []
        searchres = re.search('(?<=import )[0-9a-zA-Z_,:\\*]*', modstr)
        if searchres is not None:
            self.import_list = re.split(',', searchres.group(0))
            modstr = re.sub(r'import [0-9a-zA-Z_,:\*]*;', '', modstr)

        # Check if there is parameters
        if modstr[0] == "#":
            # remove pound
            modstr = re.sub(r'#[ ]*', '', modstr)
            self.parameters_str, modstr = self.parse_block(modstr)

        else:
            self.parameters_str = ''

        # Retreive ports list
        self.ports_str, modstr = self.parse_block(modstr)

        # Check again if there is parameters
        if modstr[0] == "#" and self.parameters_str != '':
            # remove pound
            modstr = re.sub(r'#[ ]*', '', modstr)
            (self.parameters_str, modstr) = self.parse_block(modstr)

        self.parameters_list = self.parse_parameters_list()
        self.ports_list = self.parse_ports_list()

    def get_module_name(self):
        """Returns the module name.
        """
        return self.moduleNameStr

    def get_parameters_list(self):
        """Returns the parsed parameters list.
        """
        return self.parameters_list

    def get_ports_list(self):
        """Returns the parsed ports list.
        """
        return self.ports_list

    def get_import_list(self):
        """Returns the parsed import package list.
        """
        return self.import_list
