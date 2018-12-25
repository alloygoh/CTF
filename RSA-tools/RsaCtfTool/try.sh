#!/bin/bash
for i in {0..2736}
  do
      ./RsaCtfTool.py --publickey output/key$i  .pub --uncipher cipher/cipher$i.txt
  done
