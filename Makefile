slides:
	printf '# ' > slides.md
	head -n1 readme.md >> slides.md
	grep '^\(\[\?!\|##\)' readme.md | sed 's/^##/#/' >> slides.md
	reveal-md -s '\n' slides.md
