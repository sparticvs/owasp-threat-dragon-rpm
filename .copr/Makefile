srpm:
	dnf -y install rpmdevtools rpm-build
	spectool -g -R owasp-threat-dragon.spec
	cp *.patch $(outdir)
	cp owasp-threat-dragon.desktop $(outdir)
	rpmbuild -bs owasp-threat-dragon.spec
