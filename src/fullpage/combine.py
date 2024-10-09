import os
import re

black_prefix = os.environ["BLACK"] if "BLACK" in os.environ else "black"
white_prefix = os.environ["WHITE"] if "WHITE" in os.environ else "white"
black_txt = "../" + black_prefix + ".txt"
white_txt = "../" + white_prefix + ".txt"

sources = [black_txt, white_txt]
destinations = ["black.data", "white.data"]

preamble = "\\noindent \\begin{tikzpicture}[remember picture, overlay] \\node [shift={(0.1in,0in)}]  at (current page.south west) { \\begin{tikzpicture}[remember picture, overlay,yscale=-1,line width=1pt] "
pattern = "\\node [below right,text width=1.86in] at (\LEFTMARGIN + %d * \CARDWIDTH, \TOPMARGIN + %d * \CARDHEIGHT) { \\fontsize{12}{0}\\selectfont %s };"
postamble = "\\end{tikzpicture} }; \\end{tikzpicture} \\newpage \\backgroundreverse"

def clean_content(line):
    # Remove \REFERENCE{url} patterns
    line = re.sub(r'\\REFERENCE\{.*\}', '', line)

	# Remove \OPTIONAL{..} patterns
    line = re.sub(r'\\OPTIONAL\{.*\}', '', line)

    # Escape special LaTeX characters
    # line = escape_latex(line)

    # Trim any resulting double spaces
    line = re.sub(r'\s+', ' ', line)
    return line.strip()

for i in range(len(sources)):
	with open(sources[i]) as source:
		with open(destinations[i], 'w') as destination:
			it = 0
			for line in source:
				if (it % 9) == 0:
					if it > 0:
						print(postamble, file=destination)
						print("\\newpage", file=destination)
					print(preamble, file=destination)
				content = clean_content(line)
				col = (it % 3)
				row = (it // 3) % 3
				print(pattern % (col, row, content), file=destination)
				it += 1
			print(postamble, file=destination)
