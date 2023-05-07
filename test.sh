#!/bin/bash

exec python3 /home/test.py /home/log1.log &
exec python3 /home/test.py /home/log2.log &
exec python3 /home/test.py /home/log3.log