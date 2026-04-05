import os

DRYRUN = False

PREAMBLE = [
    "\\documentclass{standalone}\n",
    "\\input{preamble}\n\n"
]

# find relevant .tex files
files = []
for filename in os.listdir('.'):
    if filename.endswith('.tex') and filename != "preamble.tex":
        files.append(filename)


for filename in files:
    # read lines
    with open(filename, 'r') as file:
        lines=file.readlines()

    # delete all lines before "\begin{document}"
    for i, line in enumerate(lines):
        if "\\begin{document}" in line:
            ending_index = i
    for i in range(ending_index):
        # iterate backwards
        j = ending_index-i-1
        print(f"deleting line {j} in file {filename}")
        lines.pop(j)
    
     # add the desired preamble
    new_lines = PREAMBLE + lines
    print("\n".join(new_lines))
    if DRYRUN is False:
        with open(filename, 'w') as file:
            file.writelines(new_lines)
    
   
    

        
        




# # delete everything inside the preamble
