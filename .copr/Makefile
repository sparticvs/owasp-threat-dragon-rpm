srpm:
	dnf -y install rpmbuild spectool
	spectool -g -R owasp-threat-dragon.spec
	rpmbuild -bs owasp-threat-dragon.spec
	cp *.patch $(outdir)
	cp owasp-threat-dragon.desktop $(outdir)
