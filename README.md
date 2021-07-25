# SVModule

## Introduction
SVModule is set of python scripts/classes to parse a [System]Verilog module declaration and paste it
as an instance, parameter definitions... It manages module imports, parameters, standard and
interface I/O ports.

The objective is to provide a similar behavior of the emacs VHDL mode but in the form of shell
commands. Then it is easy to wrap them into your preferred editor as macros or functions.

## License
SVModule is distributed under the GPLv3, the complete license description can be found
[here](http://www.gnu.org/licenses/gpl-3.0.html).

## Installation

Proceed as follow to install the package:

```
    $ pip3 install [--user] svmodule # --user for a local installation
```

## Playing with svmodp, the command line interface

1\. You must parse a \[System\]Verilog source code and generate the
internal representation in a temporary file (the default file is
\'/tmp/svmodule-dump\' under linux):

```
    $ svmodp -c myfile.v  # Note that the script will extract information of last module in the file.
```

2\. We can now play with the *paste-as* functions:

```
    $ svmodp -i  # Paste as instance
```

```
    logic_unit
    #(
      .add_extra_instr  (add_extra_instr),
      .add_select_instr (add_select_instr)
    )
    logic_unit_inst
    (
      .clk       (clk),
      .enable    (enable),
      .is_signed (is_signed),
      .opcode1   (opcode1),
      .opcode2   (opcode2),
      .cmode     (cmode),
      .op0       (op0),
      .op1       (op1),
      .out_en    (out_en),
      .out       (out)
    );
```

3\. Try the \'-h\' option to see the full list of *paste-as* functions:

```
usage: svmodp [-h] [-d filename] [-z INDENT_SIZE | -n] [-c filename | -r | -m | -g | -i | -b | -p | -s | -o | -l | -w | -t | -v]

Smart Copy & Paste of [System]Verilog files

optional arguments:
  -h, --help            show this help message and exit
  -d filename, --dump filename
                        parsed module file (default: /tmp/svmodule-dump)
  -z INDENT_SIZE, --indent-size INDENT_SIZE
                        set the indentation size (default: 4)
  -n, --indent-use-tab  use tab instead of tab for indentation (default: False)
  -c filename, --copy filename
                        (System)Verilog file (default: None)
  -r, --reverse         Reverse inputs and outputs (default: False)
  -m, --paste-as-module
                        Paste as module (default: False)
  -g, --paste-as-packages
                        Paste as packages (default: False)
  -i, --paste-as-instance
                        Paste as instance (default: False)
  -b, --paste-as-clockingblock
                        Paste as clocking block (default: False)
  -p, --paste-as-parameters
                        Paste as parameters (default: False)
  -s, --paste-as-signals
                        Paste as signals (default: False)
  -o, --paste-as-logic  Paste as logic (default: False)
  -l, --paste-as-init-latch
                        Paste as latch initialization (default: False)
  -w, --paste-as-init-wire
                        Paste as wire initialization (default: False)
  -t, --paste-as-doc-table
                        Paste as Sphinx Table (default: False)
  -v, --paste-as-wavedisp
                        Paste as Wavedisp generator (default: False)
```

## Integration with editors


In many code editors you can wrap command line interfaces as macros:

-   Firstly: extract the module definition by copying everything between
    the keyword *module* and the keyword *endmodule*, save it as a temp
    file and then call the command line interface to parse the code (-c
    option).
-   Secondly: grab the standard output of the command line interface
    executed with one of the *past-as* options and insert it in your
    editor.

### Emacs integration

Hereafter a sample of svmodule integration in Emacs.

```lisp
;; Manage SVModule
(defun svmodp-copy ()
  (interactive)
  (let (start-pos end-pos (case-fold-search t))
    (save-excursion
      (re-search-backward "module")
      (setq start-pos (point))
      (re-search-forward "endmodule")
      (setq end-pos (point))
      (message "region %d to %d" start-pos end-pos)
      (write-region start-pos end-pos "~/.svmodp-dump")))
  (shell-command "svmodp -c ~/.svmodp-dump -d ~/.svmodp-dump"))

(defun svmodp-command (command get-value)
  (let (instance)
    (message "verilog-indent-level=%d" verilog-indent-level)
    (setq value (shell-command-to-string
		 (format "svmodp -z %d -d ~/.svmodp-dump --%s" verilog-indent-level command)))
    (when get-value
	(insert value))))

(global-set-key (kbd "M-p M-w") 'svmodp-copy)
(global-set-key (kbd "M-p M-r") (lambda () (interactive) (svmodp-command "reverse" nil)))
(global-set-key (kbd "M-p M-m") (lambda () (interactive) (svmodp-command "paste-as-module" t)))
(global-set-key (kbd "M-p M-g") (lambda () (interactive) (svmodp-command "paste-as-packages" t)))
(global-set-key (kbd "M-p M-i") (lambda () (interactive) (svmodp-command "paste-as-instance" t)))
(global-set-key (kbd "M-p M-b") (lambda () (interactive) (svmodp-command "paste-as-clockingblock" t)))
(global-set-key (kbd "M-p M-c") (lambda () (interactive) (svmodp-command "paste-as-parameters" t)))
(global-set-key (kbd "M-p M-s") (lambda () (interactive) (svmodp-command "paste-as-signals" t)))
(global-set-key (kbd "M-p M-o") (lambda () (interactive) (svmodp-command "paste-as-logic" t)))
(global-set-key (kbd "M-p M-l") (lambda () (interactive) (svmodp-command "paste-as-init-latch" t)))
(global-set-key (kbd "M-p M-a") (lambda () (interactive) (svmodp-command "paste-as-init-wire" t)))
(global-set-key (kbd "M-p M-t") (lambda () (interactive) (svmodp-command "paste-as-doc-table" t)))
(global-set-key (kbd "M-p M-y") (lambda () (interactive) (svmodp-command "paste-as-wavedisp" t)))
```

## Using SVModule as a library

If your editor supports natively python3 or if you want to use svmodule
in your own project, you can just import svmodule and use directly the
API without temporary files

```python
    """Example of svmodule API use."""
    from svmodule.printer import Printer
    from svmodule.moddict import ModDict

    # Parse a file or a string.
    m = ModDict()
    m.parse(open('test.v').read())

    # Print information.
    p = Printer(m)
    print(p['Module'])          # Past as module
    print(p['Instance'])        # Past as instance
    print(p['ImportList'])      # Past as import list
    print(p['ClockingBlock'])   # Past as clocking block
    print(p['Parameters'])      # Past as parameters
    print(p['Signals'])         # Past as signals
    print(p['Logic'])           # Past as logic
    print(p['InitLatch'])       # Past as init latch
    print(p['InitWire'])        # Past as init wire
    print(p['DocTable'])        # Past as doc table

    # You can also revert the direction of I/O.
    m.reverse()
    print(p['DocTable'])
```
