#!/usr/bin/env python3
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

import sys
import os
import tempfile
import argparse

from .printer import Printer
from .moddict import ModDict


def load_moddict(dump_file):
    """Return a ModDict from temporary file.
    """

    moddict = ModDict()
    moddict.load(dump_file)

    return moddict


def copy_module(file_name, dump_file):
    """Open the file 'file_name' and parse it to a temporary file."""

    try:
        file_desc = open(file_name, 'r')
    except IOError:
        print('cannot open', file_name)

    moddict = ModDict()
    moddict.parse(str(file_desc.read()))
    moddict.store(dump_file)


def reverse_module(dump_file):
    """Reverse directions of the module."""

    moddict = load_moddict(dump_file)
    moddict.reverse()
    moddict.store(dump_file)


def paste_as_module(dump_file, indent_size):
    """Paste as a SystemVerilog module."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['Module'])


def paste_as_packages(dump_file, indent_size):
    """Paste as a SystemVerilog packages import."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['ImportList'])


def paste_as_instance(dump_file, indent_size):
    """Paste as a SystemVerilog instance."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['Instance'])


def paste_as_clockingblock(dump_file, indent_size):
    """Paste as a SystemVerilog Clocking Block."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['ClockingBlock'])


def paste_as_parameters(dump_file, indent_size):
    """Paste as SystemVerilog localparams."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['Parameters'])


def paste_as_signals(dump_file, indent_size):
    """Paste as SystemVerilog signals."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['Signals'])


def paste_as_logic(dump_file, indent_size):
    """Paste as SystemVerilog logic."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['Logic'])


def paste_as_init_latch(dump_file, indent_size):
    """Paste as SystemVerilog latch initialization."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['InitLatch'])


def paste_as_init_wire(dump_file, indent_size):
    """Paste as SystemVerilog wire initialization."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['InitWire'])


def paste_as_doc_table(dump_file, indent_size):
    """Paste as Sphynx table."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['DocTable'])


def paste_as_yaml(dump_file, indent_size):
    """Paste as YAML."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['Yaml'])


def paste_as_pandaxml(dump_file, indent_size):
    """Paste as YAML."""

    p = Printer(load_moddict(dump_file), indent_size)
    print(p['PandaXml'])


def main():
    default_dump = tempfile.gettempdir() + '/svmodule-dump'

    description = 'Smart Copy & Paste of [System]Verilog files'
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-z', '--indent-size', type=int, default=4, help='Paste as PandaXML')

    parser.add_argument('-d', '--dump', metavar='filename', type=str,
                        default=default_dump, help='parsed module file')

    group = parser.add_mutually_exclusive_group()

    group.add_argument('-c', '--copy', metavar='filename', type=str,
                       help='(System)Verilog file')

    group.add_argument('-r', '--reverse', action='store_true', default=False,
                       help='Reverse inputs and outputs')

    group.add_argument('-m', '--paste-as-module', action='store_true', default=False,
                       help='Paste as module')

    group.add_argument('-g', '--paste-as-packages', action='store_true', default=False,
                       help='Paste as packages')

    group.add_argument('-i', '--paste-as-instance', action='store_true', default=False,
                       help='Paste as instance')

    group.add_argument('-b', '--paste-as-clockingblock', action='store_true', default=False,
                       help='Paste as clocking block')

    group.add_argument('-p', '--paste-as-parameters', action='store_true', default=False,
                       help='Paste as parameters')

    group.add_argument('-s', '--paste-as-signals', action='store_true', default=False,
                       help='Paste as signals')

    group.add_argument('-o', '--paste-as-logic', action='store_true', default=False,
                       help='Paste as logic')

    group.add_argument('-l', '--paste-as-init-latch', action='store_true', default=False,
                       help='Paste as latch initialization')

    group.add_argument('-w', '--paste-as-init-wire', action='store_true', default=False,
                       help='Paste as wire initialization')

    group.add_argument('-t', '--paste-as-doc-table', action='store_true', default=False,
                       help='Paste as Sphinx Table')

    group.add_argument('-y', '--paste-as-yaml', action='store_true', default=False,
                       help='Paste as YAML')

    group.add_argument('-x', '--paste-as-pandaxml', action='store_true', default=False,
                       help='Paste as PandaXML')

    args = parser.parse_args()

    if args.copy is not None:
        copy_module(args.copy, args.dump)

    elif args.reverse is True:
        reverse_module(args.dump)

    elif args.paste_as_module is True:
        paste_as_module(args.dump, args.indent_size)

    elif args.paste_as_packages is True:
        paste_as_packages(args.dump, args.indent_size)

    elif args.paste_as_instance is True:
        paste_as_instance(args.dump, args.indent_size)

    elif args.paste_as_clockingblock is True:
        paste_as_clockingblock(args.dump, args.indent_size)

    elif args.paste_as_parameters is True:
        paste_as_parameters(args.dump, args.indent_size)

    elif args.paste_as_signals is True:
        paste_as_signals(args.dump, args.indent_size)

    elif args.paste_as_logic is True:
        paste_as_logic(args.dump, args.indent_size)

    elif args.paste_as_init_latch is True:
        paste_as_init_latch(args.dump, args.indent_size)

    elif args.paste_as_init_wire is True:
        paste_as_init_wire(args.dump, args.indent_size)

    elif args.paste_as_doc_table is True:
        paste_as_doc_table(args.dump, args.indent_size)

    elif args.paste_as_yaml is True:
        paste_as_yaml(args.dump, args.indent_size)

    elif args.paste_as_pandaxml is True:
        paste_as_pandaxml(args.dump, args.indent_size)

    else:
        parser.print_help()
