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


teststrings = [
    """module alu_dsp
  #(parameter add_extra_instr  = 1,  //use extra instructions (rotl, ...)
    parameter add_select_instr = 1,  //use select instructions
    parameter string add_select_instr = "M144k, auto",  //use select instructions
    parameter shorten_pipeline = 0)  //remove two cycles latency

   (input         clk, enable, is_signed,
    input         enacc, sub_nadd, selacc, resetrs0,
    input [31:0]  rs0, rs1, imm,
    input         mulmux, selop0, selop1,
    input [1:0]   selshift,
    input [1:0]   cmode,
    input [2:0]   opcode1, opcode2,
    output        out_en,
    output [31:0] out);""",

    """module alu_dsp  (input         clk, enable, is_signed,
    input         enacc, sub_nadd, selacc, resetrs0,
    input [31:0]  rs0, rs1, imm,
    input         mulmux, selop0, selop1,
    input [1:0]   selshift,
    input [1:0]   cmode,
    input [2:0]   opcode1, opcode2,
    output        out_en,
    output [31:0] out);""",

    """module mymod
#
(
   /* Multi line
    * comments
    */
   parameter GEN1= 48,
   parameter GEN2 = 45,
   parameter GEN3_WIDTH   = $clog2(VALUE),

   // COMMENTS
   // comment
   parameter [31:0] DEFAULT_VAL_A = 32'b0,
   parameter int [31:0] DEFAULT_VAL_B = 32'b0,
   parameter [31:0] DEFAULT_VAL_C [1:0]
)(
   // yet another comment
   input logic          reset_n,
   input logic          clock,
   input logic [$clog2(GEN3_WIDTH+1)-1:0]    test,
   /** test **/
   //yet another comment
   input pkg::typedef   clock2,
   /*
    test 1
   */
   // Rx ports
   myinterface.master     m_master,
   myinterface.slave      s_slave,
   output logic [28:0]  [$clog2(GEN1):0]m_big_array[1:0] [2:0],

   /*
     test 2
   */
   output logic [15:0]  m_simple_array,

   /* test 3
    */
   output logic [15:0]  m_simple_array3
);""",

    """module testmod(
   input logic          srst,
   input logic          clk,

   myinterface.slave    itf1, //comment1
   myinterface.master   itf2, //comment2
   input logic          insig1,
   input logic [31:0]   insig2,

   input logic [10:0]   insig3,
   input logic [7:0]    insig4,

   output logic [47:0]  outsig1,
   output logic [15:0]  outsig2,

   input logic          another_srst,
   input logic          another_clock,
   otherinterface.slave oitf,
   output logic         outsig3
  );""",


    """module testmod2(
   input logic          srst,
   input logic          clk,

   input logic          another_srst,
   input logic          another_clock,
   otherinterface.slave oitf [2:0],
   output logic         outsig3 [1:0]


);""",

    """module testmod3
  import pkg1::test, pkg2::test2, pkg3::* ;

( input logic          srst,
   input logic          clk,

   input logic          another_srst,
   input logic          another_clock,
   otherinterface.slave oitf [2:0],
   output logic         outsig3 [1:0]


);""",

]
