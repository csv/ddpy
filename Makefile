slides:
	printf '# ' > slides.md
	head -n1 readme.md >> slides.md
	echo 'Thomas Levine ([thomaslevine.com](http://thomaslevine.com))' >> slides.md
	echo >> slides.md
	grep '^\(\[\?!\|##\)' readme.md | sed -e 's/^##/#/' -e 's/^/\n/' >> slides.md
	reveal-md -s '\n\n' slides.md
