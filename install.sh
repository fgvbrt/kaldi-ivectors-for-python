echo "Enter the full path to the Kaldi installation root: "
read kaldi_root
shellname=$(basename $SHELL)
echo "export KALDI_ROOT=\"${kaldi_root}\"" >> "$HOME/.${shellname}rc"
