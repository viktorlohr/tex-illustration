#!/bin/bash

FILENAME=$1



if [[ -z "$FILENAME" || ! "$FILENAME" == *.tex ]]; then
    echo "Error: Please provide a .tex filename to remove"
    exit 1
fi

read -p "Are you sure you want to delete $FILENAME? (y/n) " -n 1 -r
echo 

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
fi

if [[ -f "$FILENAME" ]]; then
    git rm "$FILENAME"
else
    echo "Warning: $FILENAME not found. Skipping file removal"
fi

sed -i.bak "/\[$FILENAME\]/d" README.md && rm README.md.bak
echo "REMOVED '$FILENAME' entry from README"

git add README.md
git commit -m "Removed '$FILENAME' and updated README"
git push

echo "Successfully removed $FILENAME from repo and updated README"

