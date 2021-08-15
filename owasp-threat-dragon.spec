Name:	    owasp-threat-dragon
Version:	1.5.0
Release:	1%{?dist}
Summary:	An open source, online threat modeling tool from OWASP

Group:		OWASP
License:	Apache-2.0
URL:		https://docs.threatdragon.org
Source0:	https://github.com/OWASP/threat-dragon/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	nodejs >= 10.0

BuildArch:  x86_64

%description
An open source, online threat modeling tool from OWASP

%prep
%setup -q -n threat-dragon-%{version}

%build
cd td.desktop
npm install
npm run build
npx electron-builder build --linux

%install
mkdir -p /opt/OWASP-Threat-Dragon/
install -t /opt/OWASP-Threat-Dragon/ threatdragon

%clean


%files
%{_bindir}/threatdragon
%{_libdir}/libEGL.so
%{_libdir}/libffmpeg.so
%{_libdir}/libGLESv2.so
%{_libdir}/libvk_swiftshader.so
%{_libdir}/libvulkan.so
%license LICENSE.txt
%license LICENSE.electron.txt
%license LICENSE.chromium.html
%doc



%changelog

