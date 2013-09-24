##---------------------------------------------------------
# Name:        tifglobs.py
# Purpose:     globals
#
# Author:      Tim
#
# Created:     08/07/2013
# Copyright:   (c) Tim 2013
# Licence:     Creative Commons Attribution-ShareAlike 3.0 Unported License.
##---------------------------------------------------------

SILABS_VID          = 0x10c4
CP2112_PID          = 0xea90

VID_HID             = SILABS_VID
PID_HID             = CP2112_PID

DEFAULT_BUSY_LOOPS  = 5

##---------------------------------------------------------
# XO2 configuration memory
CFG_PAGE_SIZE           = 16
UFM_PAGE_SIZE           = 16

## XO2-1200
CFG_PAGE_COUNT_1200     = 2175
UFM_PAGE_COUNT_1200     = 512

## XO2-2000
CFG_PAGE_COUNT_2000     = 3198
UFM_PAGE_COUNT_2000     = 640

## XO2-4000
CFG_PAGE_COUNT_4000     = 5758
UFM_PAGE_COUNT_4000     = 768

## XO2-7000
CFG_PAGE_COUNT_7000     = 9212
UFM_PAGE_COUNT_7000     = 2048


##---------------------------------------------------------
# register addresses.
# these _must_ match the addresses defined for the hardware in tifdefs.vhd
# read-only ID register

R_ID                = 0
# write-only Scratch and Misc registers
W_SCRATCH_REG       = 1
W_MISC_REG          = 2
# misc register LED control values
LED_ALTERNATING     = 0
LED_SYNC            = 1
LED_OFF             = 2

##---------------------------------------------------------
# write command format
# the basic idea is to send an address, followed by a series of data values
# both address and data are six bit values
# the byte format is as follows, two top bits ssignal address or data
#   bit number      76543210
#   address format  00aaaaaa    aaaaaa is the register address
#   data format     01dddddd    dddddd is the data for the register

ADDRESS_MASK        = 0
DATA_MASK           = 0x40

##---------------------------------------------------------
STR_LEDS_ALT        = 'alternating'
STR_LEDS_SYNC       = 'synchronized'
STR_LEDS_OFF        = 'off'

# EOF -----------------------------------------------------------------
