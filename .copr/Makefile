srpm:
	dnf -y module install nodejs:14
	dnf -y install rpmdevtools rpm-build npm
	npm up -g npm
	spectool -g -R owasp-threat-dragon.spec
	cp *.patch /builddir/build/SOURCES/
	cp owasp-threat-dragon.desktop /builddir/build/SOURCES/
	rpmbuild -bs owasp-threat-dragon.spec
	cp /builddir/build/SRPMS/* $(outdir)
