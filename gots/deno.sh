#!/bin/zsh

if [ $1 -ge 0 ] && [ $1 -lt 10 ]; then
    filename="230$1.ts"
elif [ $1 -ge 10 ] && [ $1 -lt 100 ]; then
    filename="23$1.ts"
else
    echo "arg no good"
    exit 1
fi

deno run --allow-read --allow-env --allow-net $filename
