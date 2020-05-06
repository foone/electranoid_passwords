# electranoid_passwords
 An encoder/decoder for Electranoid (by Pixel Painters) passwords

# Usage

To decode a password, use decode.py *password*

```
$ python decode.py P2799-99972-ZZ4ML
paddles  =  5
level    =  4
score    =  12345
checksum =  71 (VALID)
```

To encode a password:
encode.py *score* *level* *paddles*

```
$ python encode.py 12345 4 5
P2799-99972-ZZ4ML
```
# Requirements

* Python 2.7.x
* A copy of Pixel Painters' Electranoid 1.20r. Other versions may work, but have not been tested.

# Notes

This was reverse engineered from the EXE using Ghidra and a lot of dosbox-x debugger work. 

No check is included for valid values: paddles should be 0-6, level 1-100, and score... I don't know.

You can optionally specify a randomization value when encoding: 
if left off it'll be randomly picked from 1-7. This doesn't affect the game, but it does change the code itself.
So if you want repeatability for some reason, specify it. 

Dashes are not important to either the decoder or the game, you can happily leave them off. 

# License

The game itself is by Pixel Painters Corp, I claim no copyright to it.

All the code here is by Foone Turing.

It's licensed under the terms of the GPL, version 3. (and you don't have to agree to it!)