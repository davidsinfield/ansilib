#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ansidemo.py
#  
#  Copyright 2017  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

dictForeBack={
'fore' : 3,
'back' : 4
}
dictColour={
'black' : 0,
'red' : 1,
'green' : 2, 
'yellow' : 3,
'blue' : 4,
'magenta' : 5,
'cyan' : 6,
'white' : 7
}
dictStyle={
'normal' : 0,
'bold': 1,
'italic' : 3,
'underline' :4,
'inverse': 7,
'strikethough' : 9
}
#========================================================================
#GetANSI(text,foreback,colour,style)
#text - text to print
#forecolour - [black|red|green|yellow|blue|magenta|cyan|white]
#backcolour - [black|red|green|yellow|blue|magenta|cyan|white]
#style - [normal|bold|italic|underline|inverse|strikethough]
#
#Returns a string with ansi precursors to set foreground and background
#colours and style. Set to normal after printing.
#
#Out of range parameters throw a dictionary error
#
#Example: set foreground to red
#	print GetANSI('this is red text','red','none','none')
#Example: set foreground bold red, background cyan
#	print GetANSI('set properties','red','cyan','bold')
#
#Update
#	empty string in a parameter is now the same as none.
#	Example:
#		GetANSI('text','','','bold')
#=========================================================================
def GetANSI(text,forecolour,backcolour,style):
	pre="\033["
	post="m"
	tonormal=pre+'0m'
	retval=""
	if forecolour != 'none' and forecolour != '':
		retval=retval+pre+str(dictForeBack['fore'])+str(dictColour[forecolour])+post
	if backcolour != 'none' and backcolour != '':
		retval=retval+pre+str(dictForeBack['back'])+str(dictColour[backcolour])+post
	if style != 'none' and style != '':
		retval=retval+pre+str(dictStyle[style])+post
	return (retval+text+tonormal)

def main():	
	print GetANSI('red text','red','none','none')
	print GetANSI('red text cyan bg bold','red','cyan','bold')
	print GetANSI('inverse of above','red','cyan','inverse')
	print GetANSI('black on white','none','none','inverse')
	print GetANSI('black on green','green','none','inverse')
	print GetANSI('non explicit green','green','','')
	print 'normal text'
	return 0

if __name__ == '__main__':
	main()

