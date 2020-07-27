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

# Level codes:

You can use --level-list to generate a list of passwords for all levels. 
These give you 6 paddles & 0 score, and are intended as a way to preview later levels.

Here's an example of them, for easy copy-pasting:

```
Level    1: MHMHM-HMHAE-63LB2
Level    2: 45454-54536-EA45Z
Level    3: 45454-545LB-HM36Z
Level    4: MHMHM-HMHHM-ZZHM2
Level    5: 45454-545MH-BLAEZ
Level    6: CPCPC-PCP99-PCHM4
Level    7: CPCPC-PCPEA-54BL4
Level    8: MHMHM-HMHPC-LBCP2
Level    9: 45454-545HM-ZZ54Z
Level   10: 36363-63663-363PC
Level   11: MHMHM-HMH45-AE9E2
Level   12: 45454-54563-362BZ
Level   13: 27272-727CP-997ML
Level   14: MHMHM-HMHLB-HMP32
Level   15: 27272-727LB-HM5CL
Level   16: 36363-6363P-99P3C
Level   17: LBLBL-BLB2B-HM4Z3
Level   18: MHMHM-HMH9E-632B2
Level   19: CPCPC-PCP2B-HM3P4
Level   20: CPCPC-PCPM7-722B4
Level   21: AEAEA-EAEB2-45B2M
Level   22: CPCPC-PCP9E-63E94
Level   23: MHMHM-HMH6L-CP5C2
Level   24: LBLBL-BLBB2-455C3
Level   25: 27272-727P3-36C5L
Level   26: 45454-5457M-ZZZCZ
Level   27: AEAEA-EAEC5-AE9HM
Level   28: CPCPC-PCPP3-36264
Level   29: 27272-727C5-AEH9L
Level   30: ZZZZZ-ZZZP3-36A75
Level   31: 36363-636C5-AEBMC
Level   32: 36363-63635-AE62C
Level   33: 45454-545CZ-MH62Z
Level   34: CPCPC-PCPLP-99ZC4
Level   35: MHMHM-HMHEE-63MB2
Level   36: LBLBL-BLB9H-BLMB3
Level   37: CPCPC-PCPA7-72MB4
Level   38: 36363-636EE-63EEC
Level   39: 27272-727BM-ZZ62L
Level   40: 36363-6367A-5462C
Level   41: ZZZZZ-ZZZEE-63BM5
Level   42: ZZZZZ-ZZZH9-PCP25
Level   43: 27272-727ZC-LB2PL
Level   44: 36363-63653-362PC
Level   45: 45454-545PL-CP2PZ
Level   46: AEAEA-EAE26-EA6MM
Level   47: 36363-636CZ-MH79C
Level   48: MHMHM-HMHM6-EA5L2
Level   49: AEAEA-EAE97-72C4M
Level   50: MHMHM-HMH97-723Z2
Level   51: ZZZZZ-ZZZ3Z-MH5L5
Level   52: CPCPC-PCPM6-EA3Z4
Level   53: 27272-727HE-6397L
Level   54: 36363-636EH-BL97C
Level   55: AEAEA-EAEP2-45P2M
Level   56: AEAEA-EAE5L-CPZ3M
Level   57: 36363-636BA-54P2C
Level   58: 36363-6366M-ZZZLC
Level   59: 27272-727Z3-36LZL
Level   60: LBLBL-BLBZ3-36253
Level   61: 45454-545P2-45LZZ
Level   62: AEAEA-EAE2P-99B9M
Level   63: 45454-545Z3-369BZ
Level   64: CPCPC-PCPCC-LBHH4
Level   65: 45454-545CC-LB7EZ
Level   66: LBLBL-BLBMP-99ZL3
Level   67: 45454-545LZ-MH52Z
Level   68: ZZZZZ-ZZZLZ-MHZL5
Level   69: 27272-727HH-BLA6L
Level   70: 36363-636E7-72A6C
Level   71: 27272-727B9-PC7EL
Level   72: 27272-7276A-546AL
Level   73: CPCPC-PCP7E-63B94
Level   74: 27272-72752-454LL
Level   75: 27272-727ZL-CP3CL
Level   76: LBLBL-BLBZL-CPL43
Level   77: 45454-545PM-ZZ3CZ
Level   78: MHMHM-HMHLZ-MHH72
Level   79: AEAEA-EAEMP-9969M
Level   80: 45454-5454L-CP96Z
Level   81: 45454-545C3-36H7Z
Level   82: AEAEA-EAEEB-HMC3M
Level   83: 27272-72796-EAC3L
Level   84: CPCPC-PCPM5-AE4L4
Level   85: MHMHM-HMH7H-BLAP2
Level   86: ZZZZZ-ZZZM5-AE3C5
Level   87: CPCPC-PCPEB-HMAP4
Level   88: CPCPC-PCPH7-72EB4
Level   89: 36363-636BE-63BEC
Level   90: 36363-63669-PCP9C
Level   91: 36363-636PA-54ZMC
Level   92: 45454-54569-PCZMZ
Level   93: MHMHM-HMH3C-LBA52
Level   94: MHMHM-HMHL4-27E62
Level   95: MHMHM-HMH2Z-MH772
Level   96: 36363-63633-36E6C
Level   97: LBLBL-BLB24-27BH3
Level   98: LBLBL-BLBMZ-MHP93
Level   99: ZZZZZ-ZZZ33-36BH5
Level  100: 36363-636A5-AE42C
```

# License

The game itself is by Pixel Painters Corp, I claim no copyright to it.

All the code here is by Foone Turing.

It's licensed under the terms of the GPL, version 3. (and you don't have to agree to it!)
