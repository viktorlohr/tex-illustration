import os
import subprocess
import sys

# create alle_bilder.tex
lines = [
    "\\documentclass{article}\n",
    "\\input{preamble}\n",
    "\\begin{document}\n",
    ]

# get all images
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

# compile
filename = "alle_bilder.pdf"
try:
    subprocess.run(["pdflatex","-interaction=nonstopmode", "alle_bilder.tex"], check=True)
    subprocess.run(["open", filename], check=True)
except subprocess.CalledProcessError:
    print("LaTeX compilation failed")
    sys.exit(1)

# copy to gdrive
dest_dir = os.path.expanduser("~/gdrive/1_nachhilfe/akademus-skript/meine-bilder")
os.makedirs(dest_dir, exist_ok=True)
dest_path = os.path.join(dest_dir, filename)
subprocess.run(["cp", filename, dest_path])
subprocess.run(["open", dest_dir])


