slides:
	printf '# ' > slides.md
	head -n1 readme.md >> slides.md
	echo 'Thomas Levine ([thomaslevine.com](http://thomaslevine.com)),<br/>' >> slides.md
	echo 'csv soundsystem ([csvsoundsystem.com](http://csvsoundsystem.com))' >> slides.md
	echo >> slides.md
	grep '^\(\[\?!\|##\)' readme.md | sed -e 's/^##/#/' -e 's/^/\n/' >> slides.md
	reveal-md -t solarized -s '\n\n' slides.md
