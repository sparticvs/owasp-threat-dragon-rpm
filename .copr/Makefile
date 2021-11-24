srpm:
	dnf -y install rpmdevtools rpm-build
	spectool -g -R owasp-threat-dragon.spec
	cp *.patch /builddir/build/SOURCES/
	cp owasp-threat-dragon.desktop /builddir/build/SOURCES/
	rpmbuild -bs owasp-threat-dragon.spec
	cp /builddir/build/SRPMS/* $(outdir)
