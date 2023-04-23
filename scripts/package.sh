#!/bin/bash

which zip > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "zip command does not exist." >&2
    exit 2
fi

if [ ! -f "./dist/font16seg.py" ]; then
    echo "./dist/font16seg.py does not exist." >&2
    echo "run build first" >&2
    exit 3
fi
if [ ! -f "./dist/font16seg.mpy" ]; then
    echo "./dist/font16seg.mpy does not exist." >&2
    echo "run build first" >&2
    exit 4
fi

rm -f "./dist/package.zip"
rm -rf "./dist/tmp"
mkdir "./dist/tmp"

echo "./dist/font16seg.mpy -> ./dist/tmp/font16seg.mpy"
cp "./dist/font16seg.mpy" "./dist/tmp/"
echo "./dist/font16seg.py -> ./dist/tmp/font16seg.py"
cp "./dist/font16seg.py" "./dist/tmp/"
echo "./LICENSE -> ./dist/tmp/LICENSE"
cp "./LICENSE" "./dist/tmp/"
echo "./readme.txt -> ./dist/tmp/readme.txt"
cp "./readme.txt" "./dist/tmp/"
echo
echo "Create archive file"
cd "./dist/tmp"
zip "../package.zip" -r *
cd "../../"
rm -rf "./dist/tmp"

echo
if [ -f "./dist/package.zip" ]; then
    FILE_SIZE=`stat -c "%s" ./dist/package.zip`
    if [ $? -ne 0 ]; then
        echo "stat failed" >&2
        exit 5
    fi
    echo "Name: ./dist/package.zip"
    echo "Size: ${FILE_SIZE}"
    echo
else
    echo "Failed" >&2
    exit 6
fi

exit 0
