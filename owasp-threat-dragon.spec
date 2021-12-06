Name:	    owasp-threat-dragon
Version:	1.5.8
Release:	1%{?dist}
Summary:	An open source, online threat modeling tool from OWASP

Group:		OWASP
License:	Apache-2.0
URL:		https://docs.threatdragon.org
Source0:	https://github.com/OWASP/threat-dragon/archive/refs/tags/v%{version}.tar.gz
# Not a bug - reducing build time by removing extra build targets
Patch0:		optimize-electron-build.patch
# Not a bug - Just lazy at the moment
Patch1:     desktop_file.patch

BuildRequires:	nodejs >= 7.0
BuildRequires:  npm

%description
An open source, online threat modeling tool from OWASP

%global debug_package %{nil}

%prep
%setup -q -n threat-dragon-%{version}
%patch0 -p0
%patch1 -p0

%build
cd td.desktop
npm -g update npm
npm install
npm run build
npx electron-builder build --linux

%install
%define td_desktop_dir /opt/OWASP-Threat-Dragon
%define td_desktop_install %{buildroot}%{td_desktop_dir}
%define td_desktop_root %{_builddir}/threat-dragon-%{version}/td.desktop
%define td_desktop_build %{td_desktop_root}/installers/linux-unpacked

install -d -m 755 %{td_desktop_install}
cp -r %{td_desktop_build}/* %{td_desktop_install}
chmod 0755 %{td_desktop_install}/{chrome-sandbox,libEGL.so,libffmpeg.so,libGLESv2.so,libvk_swiftshader.so,libvulkan.so,threat-dragon}
mkdir -p %{td_desktop_install}/icon/
install -m 644 %{td_desktop_root}/public/content/icons/png/128x128.png %{td_desktop_install}/icon/
mkdir -p %{buildroot}%{_datadir}/applications/
install -m 644 %{td_desktop_root}/owasp-threat-dragon.desktop %{buildroot}%{_datadir}/applications/
# Add a .desktop file

%clean
umask 022
cd %{_builddir}
rm -rf threat-dragon-%{version}

%files
%defattr(644, root, root)
%{td_desktop_dir}/chrome_100_percent.pak
%{td_desktop_dir}/chrome_200_percent.pak
%{td_desktop_dir}/icudtl.dat
%{td_desktop_dir}/locales
%{td_desktop_dir}/resources*
%{td_desktop_dir}/snapshot_blob.bin
%{td_desktop_dir}/v8_context_snapshot.bin
%{td_desktop_dir}/vk_swiftshader_icd.json
%{td_desktop_dir}/icon/128x128.png
%{_datadir}/applications/owasp-threat-dragon.desktop
%defattr(755, root, root)
%dir %{td_desktop_dir}
%{td_desktop_dir}/chrome-sandbox
%{td_desktop_dir}/libEGL.so
%{td_desktop_dir}/libffmpeg.so
%{td_desktop_dir}/libGLESv2.so
%{td_desktop_dir}/libvk_swiftshader.so
%{td_desktop_dir}/libvulkan.so
%{td_desktop_dir}/threat-dragon
%{td_desktop_dir}/swiftshader/libEGL.so
%{td_desktop_dir}/swiftshader/libGLESv2.so
%license %{td_desktop_dir}/LICENSE.electron.txt
%license %{td_desktop_dir}/LICENSES.chromium.html



%changelog
* Mon Dec 06 2021 Charles Timko <sparticvs@popebp.com> - 1.5.8-1
- Add v1.5.8 release

* Wed Dec 01 2021 Charles Timko <sparticvs@popebp.com> - 1.5.5-4
- Add npm rpm to BuildRequires

* Wed Dec 01 2021 Charles Timko <sparticvs@popebp.com> - 1.5.5-3
- Add fullpath to npm/npx

* Wed Dec 01 2021 Charles Timko <sparticvs@popebp.com> - 1.5.5-2
- Correct invalid date for initial spec file

* Sat Sep 25 2021 Charles Timko <ctimko@redhat.com> - 1.5.5-1
- Updating to v1.5.5

* Tue Aug 31 2021 Charles Timko <ctimko@redhat.com> - 1.5.3-1
- Updating to v1.5.3

* Tue Aug 17 2021 Charles Timko <ctimko@redhat.com> - 1.5.0-1
- Initial Version


