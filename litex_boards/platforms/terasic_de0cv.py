#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2014-2019 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.altera import AlteraPlatform
from litex.build.altera.programmer import USBBlaster

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk / Rst
    ("clk50", 0, Pins("M9"),  IOStandard("3.3-V LVTTL")),
#    ("clk50", 1, Pins("H13"), IOStandard("3.3-V LVTTL")),
#    ("clk50", 2, Pins("E10"), IOStandard("3.3-V LVTTL")),
#    ("clk50", 3, Pins("V15"), IOStandard("3.3-V LVTTL")),
    ("reset_n", 0, Pins("P22"), IOStandard("3.3-V LVTTL")),

    # Leds
    ("user_led", 0, Pins("AA2"), IOStandard("3.3-V LVTTL")),
    ("user_led", 1, Pins("AA1"), IOStandard("3.3-V LVTTL")),
    ("user_led", 2, Pins("W2"),  IOStandard("3.3-V LVTTL")),
    ("user_led", 3, Pins("Y3"),  IOStandard("3.3-V LVTTL")),
    ("user_led", 4, Pins("N2"),  IOStandard("3.3-V LVTTL")),
    ("user_led", 5, Pins("N1"),  IOStandard("3.3-V LVTTL")),
    ("user_led", 6, Pins("U2"),  IOStandard("3.3-V LVTTL")),
    ("user_led", 7, Pins("U1"),  IOStandard("3.3-V LVTTL")),
    ("user_led", 8, Pins("L2"),  IOStandard("3.3-V LVTTL")),
    ("user_led", 9, Pins("L1"),  IOStandard("3.3-V LVTTL")),

    # Button
    ("key", 0, Pins("U7"), IOStandard("3.3-V LVTTL")),
    ("key", 1, Pins("W9"), IOStandard("3.3-V LVTTL")),
    ("key", 2, Pins("M7"), IOStandard("3.3-V LVTTL")),
    ("key", 3, Pins("M6"), IOStandard("3.3-V LVTTL")),

    # Switches
    ("sw", 0, Pins("U13"),  IOStandard("3.3-V LVTTL")),
    ("sw", 1, Pins("V13"),  IOStandard("3.3-V LVTTL")),
    ("sw", 2, Pins("T13"),  IOStandard("3.3-V LVTTL")),
    ("sw", 3, Pins("T12"),  IOStandard("3.3-V LVTTL")),
    ("sw", 4, Pins("AA15"), IOStandard("3.3-V LVTTL")),
    ("sw", 5, Pins("AB15"), IOStandard("3.3-V LVTTL")),
    ("sw", 6, Pins("AA14"), IOStandard("3.3-V LVTTL")),
    ("sw", 7, Pins("AA13"), IOStandard("3.3-V LVTTL")),
    ("sw", 8, Pins("AB13"), IOStandard("3.3-V LVTTL")),
    ("sw", 9, Pins("AB12"), IOStandard("3.3-V LVTTL")),

    # SDCard
    ("spisdcard", 0,
        Subsignal("clk",  Pins("H11")),
        Subsignal("cs_n", Pins("C11")),
        Subsignal("mosi", Pins("B11"), Misc("WEAK_PULL_UP_RESISTOR ON")),
        Subsignal("miso", Pins("K9"),  Misc("WEAK_PULL_UP_RESISTOR ON")),
        IOStandard("3.3-V LVTTL"),
    ),

    ("sdcard", 0,
        Subsignal("data", Pins("K9 D12 E12 C11"), Misc("WEAK_PULL_UP_RESISTOR ON")),
        Subsignal("cmd",  Pins("B11"), Misc("WEAK_PULL_UP_RESISTOR ON")),
        Subsignal("clk",  Pins("H11")),
        Misc("FAST_OUTPUT_REGISTER ON"),
        IOStandard("3.3-V LVTTL"),
    ),

    # PS2
    ("ps2", 0,
        Subsignal("clk", Pins("D3")),
        Subsignal("dat", Pins("G2")),
        IOStandard("3.3-V LVTTL"),
    ),
    ("ps2", 1,
        Subsignal("clk", Pins("E2")),
        Subsignal("dat", Pins("G1")),
        IOStandard("3.3-V LVTTL"),
    ),

    # VGA
    ("vga", 0,
        Subsignal("hsync_n", Pins("H8")),
        Subsignal("vsync_n", Pins("G8")),
        Subsignal("r", Pins("A9  B10 C9  A5")),
        Subsignal("g", Pins("L7  K7  J7  J8")),
        Subsignal("b", Pins("B6  B7  A8  A7")),
        Misc("CURRENT_STRENGTH_NEW \"8MA\""),
        Misc("FAST_OUTPUT_REGISTER ON"),
        IOStandard("3.3-V LVTTL"),
    ),

    # SDR SDRAM
    ("sdram_clock", 0, Pins("AB11"), IOStandard("3.3-V LVTTL")),
    ("sdram", 0,
        Subsignal("a",     Pins(
            "W8 T8 U11 Y10 N6 AB10 P12 P7 P8 R5 U8 P6 R7")),
        Subsignal("ba",    Pins("T7 AB7")),
        Subsignal("cs_n",  Pins("U6")),
        Subsignal("cke",   Pins("R6")),
        Subsignal("ras_n", Pins("AB6")),
        Subsignal("cas_n", Pins("V6")),
        Subsignal("we_n",  Pins("AB5")),
        Subsignal("dq", Pins(
            "Y9  T10 R9  Y11 R10 R11 R12 AA12",
            "AA9 AB8 AA8 AA7 V10 V9  U10 T9"),
            Misc("FAST_OUTPUT_ENABLE_REGISTER ON"),
            Misc("FAST_INPUT_REGISTER ON")),
        Subsignal("dm", Pins("U12 N8")),
        Misc("CURRENT_STRENGTH_NEW \"MAXIMUM CURRENT\""),
        Misc("FAST_OUTPUT_REGISTER ON"),
        Misc("ALLOW_SYNCH_CTRL_USAGE OFF"),
        IOStandard("3.3-V LVTTL")
    ),

    # GPIOs
    ("gpio", 0, Pins(
        "JP1:1  JP1:2  JP1:3  JP1:4  JP1:5  JP1:6  JP1:7  JP1:8",
        "JP1:9  JP1:10 JP1:13 JP1:14 JP1:15 JP1:16 JP1:17 JP1:18",
        "JP1:19 JP1:20 JP1:21 JP1:22 JP1:23 JP1:24 JP1:25 JP1:26",
        "JP1:27 JP1:28 JP1:31 JP1:32 JP1:33 JP1:34 JP1:35 JP1:36",
        "JP1:37 JP1:38 JP1:39 JP1:40"),
        IOStandard("3.3-V LVTTL")
    ),
    ("gpio", 1, Pins(
        "JP2:1  JP2:2  JP2:3  JP2:4  JP2:5  JP2:6  JP2:7  JP2:8",
        "JP2:9  JP2:10 JP2:13 JP2:14 JP2:15 JP2:16 JP2:17 JP2:18",
        "JP2:19 JP2:20 JP2:21 JP2:22 JP2:23 JP2:24 JP2:25 JP2:26",
        "JP2:27 JP2:28 JP2:31 JP2:32 JP2:33 JP2:34 JP2:35 JP2:36",
        "JP2:37 JP2:38 JP2:39 JP2:40"),
        IOStandard("3.3-V LVTTL")
    ),

    # Serial
    ("gpio_serial", 0,
        # Compatible with cheap FT232 based cables (ex: Gaoominy 6Pin Ftdi Ft232Rl Ft232)
        # GND on JP1 Pin 12.
        Subsignal("tx", Pins("JP1:10"), IOStandard("3.3-V LVTTL")),
        Subsignal("rx", Pins("JP1:8"),  IOStandard("3.3-V LVTTL"))
    ),
]

# Connectors ---------------------------------------------------------------------------------------

_connectors = [
    # PIN    0  1   2   3   4   5   6   7   8   9   10  11  12 13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30 31  32  33  34  35  36  37  38  39  40
    ("JP1", "-  N16 B16 M16 C16 D17 K20 K21 K22 K20 M21 -   -  N21 R22 R21 T22 N20 N19 M22 P10 L22 P17 P16 M18 L18 L17 L19 K17 -   -  K19 P18 R15 R17 R16 T20 T19 T18 T17 T15"),
    ("JP2", "-  H16 A12 H15 B12 A13 B13 C13 D13 G18 G17 -   -  H18 J18 J19 G11 H10 J11 H14 A15 J13 L8  A14 B15 C15 E14 E15 E16 -   -  F14 F15 F13 F12 G16 G15 G13 G12 J17 K16")
]

# Platform -----------------------------------------------------------------------------------------

class Platform(AlteraPlatform):
    default_clk_name   = "clk50"
    default_clk_period = 1e9/50e6

    def __init__(self, toolchain="quartus"):
        AlteraPlatform.__init__(self, "5CEBA4F23C7", _io, _connectors, toolchain=toolchain)

    def create_programmer(self):
        return USBBlaster()

    def do_finalize(self, fragment):
        AlteraPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk50", 0, loose=True), 1e9/50e6)
#        self.add_period_constraint(self.lookup_request("clk50", 1, loose=True), 1e9/50e6)
#        self.add_period_constraint(self.lookup_request("clk50", 2, loose=True), 1e9/50e6)
#        self.add_period_constraint(self.lookup_request("clk50", 3, loose=True), 1e9/50e6)
        self.toolchain.additional_sdc_commands.append("set_false_path -from [get_ports {reset_n}]")
        self.toolchain.additional_sdc_commands.append("create_clock -name altera_reserved_tck -period 6MHz [get_ports {altera_reserved_tck}]")
        self.toolchain.additional_sdc_commands.append("set_clock_groups -asynchronous -group {altera_reserved_tck}")
