# ansilib
ANSI Library provides access to the ANSI terminal escape codes.

Provided as is and without warranty under the terms of the GPL. It would be nice if you credited me if you use it. 

Version 1 has only a single function GetANSI which wraps a string with the codes to format coloured output
It has been tested on 
  xcfe on raspian and ubuntu 14.04 and 16.04, 
  gnome-terminal on ubuntu 14.04 and 16.04
  lxde on raspian
This version will through a dictionary item not found error if the parameters passed are out of range.
See comments in code for the permitted values.

Planned work:
Do cursor control function

If anyone tests this successfully or unsuccsessfully on any other terminals please let me know and I will add them to the platform list.

Happy to hear of bugs/suggestions
