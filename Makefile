slides:
	grep '^\(\[\?!\|##\)' readme.md | sed 's/^##/#/' > slides.md
	reveal-md -s '\n' slides.md
