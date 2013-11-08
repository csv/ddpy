slides:
	grep '^\(\[\?!\|##\)' readme.md > slides.md
	reveal-md -s '\n' slides.md
