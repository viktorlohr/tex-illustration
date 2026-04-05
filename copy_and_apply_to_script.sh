ROOT_PATH=~/dev/abiturwissen-mathematik
INPUT_PATH="$ROOT_PATH/Graphiken/tikz-standalones"
OUTPUT_PATH="$ROOT_PATH/Graphiken_PDF/tikz-standalones"

cp *.tex "$INPUT_PATH"
cp farbeinstellung.txt "$INPUT_PATH"
cp compile_to_Graphiken_PDF.sh
latexmk -pdf -cd -outdir="$OUTPUT_PATH" "$INPUT_PATH"/*.tex