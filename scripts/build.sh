#!/bin/bash

if [ -f "./dist/font16seg.py" ]; then
    rm "./dist/font16seg.py"
fi

if [ ! -f "./src/font16seg.py" ]; then
    echo "./src/font16seg.py does not exist." >&2
    exit 2
fi

cp "./src/font16seg.py" "./dist/font16seg.py"
FILE_SIZE=`stat -c "%s" ./dist/font16seg.py`
if [ $? -ne 0 ]; then
    echo "stat failed" >&2
    exit 3
fi
echo "Name: ./dist/font16seg.py"
echo "Size: ${FILE_SIZE}"
echo

which mpy-cross > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "mpy-cross command does not exist." >&2
    exit 4
fi

if [ -f "./dist/font16seg.mpy" ]; then
    rm "./dist/font16seg.mpy"
fi

mpy-cross ./dist/font16seg.py

if [ -f "./dist/font16seg.mpy" ]; then
    FILE_SIZE=`stat -c "%s" ./dist/font16seg.mpy`
    echo "Name: ./dist/font16seg.mpy"
    echo "Size: ${FILE_SIZE}"
    echo
else
    echo "Failed" >&2
    exit 5
fi

mpy-cross --version

exit 0
