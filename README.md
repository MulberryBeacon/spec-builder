# Spec Builder

Script to generate multiple PC configurations.

## Description

To plan the purchase of a new PC, I initially used a spreadsheet to calculate
the cost of several different configurations. I eventually needed to generate
multiple combinations with a specific set of components and decided to create
this quick script to achieve it.

## Configuration

The script uses JSON data files (one for each type of component) that are stored
in the directory `data`:

```
ls -l /home/user/spec-builder/data/
case.json
cpu.json
gpu.json
memory.json
motherboard.json
psu.json
storage.json
```

## Instructions

To run the script, navigate to the directory with the source code and use the
Python executable:

```
cd /path/to/spec-builder/
python3 spec-builder.py
```

## Dependencies

All development and testing activities are carried out on Ubuntu 18.10 using
Python 3.6.7.

## Disclaimer

This **is not** production ready code.

## License

Copyright (c) 2019 Eduardo Ferreira

The code in this repository is MIT licensed, and therefore free to use as you
please for commercial or non-commercial purposes (see [LICENSE](LICENSE) for
details).
