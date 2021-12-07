srpm:
	dnf -y install rpmdevtools rpm-build npm
	dnf -y module reset nodejs
	dnf -y module install nodejs:14
	npm up -g npm
	spectool -g -R owasp-threat-dragon.spec
	cp *.patch /builddir/build/SOURCES/
	cp owasp-threat-dragon.desktop /builddir/build/SOURCES/
	rpmbuild -bs owasp-threat-dragon.spec
	cp /builddir/build/SRPMS/* $(outdir)
