#!/bin/bash

FILENAME=$1

if [ -e "$FILENAME"]; then
    echo "File already exists!"
    exit 1
fi

if [[ ! "$FILENAME" == *.tex ]]; then
    echo "Error: File must have .tex extension."
    exit 1
fi


cat <<EOF > "$FILENAME"
\documentclass{standalone}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\begin{document}
\begin{tikzpicture}
\end{tikzpicture}
\end{document}
EOF


URL="https://www.overleaf.com/docs?snip_uri=https://raw.githubusercontent.com/viktorlohr/tex-illustration/refs/heads/main/$FILENAME"

echo "* [$FILENAME]($URL)" >> README.md


git add "$FILENAME" README.md
git commit -m "created '$FILENAME' "
git push


echo "Successfully created $FILENAME, pushed it and updated README with Overleaf-Link "

