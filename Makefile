slides:
	head -n2 readme.md > slides.md
	grep '^\(\[\?!\|##\)' readme.md | sed 's/^##/#/' >> slides.md
	reveal-md -s '\n' slides.md
