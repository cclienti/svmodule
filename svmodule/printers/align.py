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


def vertical_align_string(strval, separator='\n', align_char='(', nbspaces=1):
    """Return an aligned version of strval string. The vertical
    alignment is made using an "align_char" accross lines separated by
    "separator".
    """

    # split the string into list of string using separator
    strlist = strval.split(separator)

    # split each string in the previous list into list of string using
    # align_char => tokenlist is a list of list
    tokenlist = []
    for s in strlist:
        tokenlist.append(s.split(align_char))

    # Look the longest string in each column
    lendic = {}
    for row in range(len(tokenlist)):
        for col in range(len(tokenlist[row])):
            if col not in lendic:
                lendic[col] = 0

            lendic[col] = max(lendic[col], len(tokenlist[row][col]))

    # Align regarding previous results except last col
    for row in range(len(tokenlist)):
        lencol = len(tokenlist[row])

        if lencol <= 1:
            continue

        for col in range(lencol-1):
            x = tokenlist[row][col]
            x += ' ' * (lendic[col] - len(x)+nbspaces)
            tokenlist[row][col] = x

    # Build the string
    aligned = align_char.join(tokenlist[0])
    for row in tokenlist[1:]:
        aligned += '\n' + align_char.join(row)

    return aligned


def main():
    strtest = """      .clk(clk),
      .enable(enable)(),
      .is_signed(is_signed)(),
      .enacc(enacc),
      .sub_nadd(sub_nadd),
      .selacc(selacc),
      .resetrs0(resetrs0),
      .rs0(rs0),
      .rs1(rs1),
      .imm(imm),
      .mulmux(mulmux),
      .selop0(selop0),
      .selop1(selop1),
      .selshift(selshift),
      .cmode(cmode),
      .opcode1(opcode1),
      .opcode2(opcode2),
      .out_en(out_en),
      .out(out)"""

    print(vertical_align_string(strtest, align_char='(', nbspaces=1))

if __name__ == "__main__":
    main()
