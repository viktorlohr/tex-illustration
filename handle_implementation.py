import os
import subprocess
import sys

script_dir = os.path.expanduser("~/dev/abiturwissen-mathematik")
# create alle_bilder.tex
lines = [
    "\\documentclass{article}\n",
    "\\input{preamble}\n",
    "\\begin{document}\n",
    ]

# get all relevant pdf-files, compile and copy them into the script directory; 
# also include them in "alle_bilder.tex"

pdf_dir = os.path.join(script_dir,"Graphiken_PDF/tikz-standalones")
files = []
for filepath in os.listdir('.'):
    if (
        filepath.endswith('.tex') and 
        filepath != "alle_bilder.tex" and
        filepath != "preamble.tex"
        ):
        files.append(filepath) # used for later
        
        # compile the pdfs
        try:
            subprocess.run(["pdflatex", "-interaction=nonstopmode", filepath],
                        check=True)
        except subprocess.CalledProcessError:
            print(f"LaTeX-compilation of {filepath} failed")
            sys.exit(1)

        # copy the pdfs into script dir
        no_ext_name = filepath[:-4]
        pdf_name = no_ext_name+".pdf"
        try:
            subprocess.run(["cp", pdf_name, os.path.join(pdf_dir, pdf_name)], 
                       check=True)
        except subprocess.CalledProcessError:
            print(f"could not copy {pdf_name}")
            sys.exit(1)


        # include the pdfs in alle_bilder.tex
        lines.append(f"{no_ext_name}\n\\includegraphics{{{no_ext_name}}}\n\clearpage")

lines.append("\\end{document}")

with open("alle_bilder.tex", "w") as f:
    f.writelines(lines)



# copy all relevant tex files (all of the above + preamble)
source_code_dir = os.path.join(script_dir,"Graphiken/tikz-standalones")
relevant_tex_files = files + ["preamble.tex"]
for filepath in relevant_tex_files:
    try:
        subprocess.run(["cp", filepath, os.path.join(source_code_dir, filepath)])
    except subprocess.CalledProcessError:
        print(f"copy of {filepath} failed")

# compile alle_bilder.tex und abiturwissen_mathematik.tex
"alle_bilder.tex"
script_name = "abiturwissen_mathematik.tex"
script_path = os.path.join(script_dir, script_name)
for filepath in ["alle_bilder.tex", script_path]:
    pdf_path = filepath[:-4] + ".pdf"
    _path, pdf_filename = os.path.split(pdf_path)
    try:
        subprocess.run(["latexmk","-cd", "-pdf", "-interaction=nonstopmode", filepath], 
                    check=True)
        subprocess.run(["open", pdf_path], check=True)
    except subprocess.CalledProcessError:
        print(f"LaTeX compilation of {filepath} failed")
        sys.exit(1)

    # copy alle_bilder.pdf and script to gdrive
    gdrive_dest_dir = os.path.expanduser("~/gdrive/1_nachhilfe/akademus-skript/meine-bilder")
    os.makedirs(gdrive_dest_dir, exist_ok=True)
    dest_path = os.path.join(gdrive_dest_dir, pdf_filename)
    subprocess.run(["cp", pdf_path, dest_path])
    subprocess.run(["open", gdrive_dest_dir])

