import os

lines = [
    "\\documentclass{article}\n",
    "\\input{preamble}\n",
    "\\begin{document}\n",
    ]

for filename in os.listdir('.'):
    if (
        filename.endswith('.tex') and 
        filename != "alle_bilder.tex" and
        filename != "preamble.tex"
        ):
        lines.append(f"\\include{{{filename}}}\n")

lines.append("\\end{document}")

with open("alle_bilder.tex", "w") as f:
    f.writelines(lines)