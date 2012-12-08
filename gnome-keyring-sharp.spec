Summary:	Mono implementation of the GNOME Keyring API
Name:		gnome-keyring-sharp
Version:	1.0.2
Release:	4
Source0:	http://www.go-mono.com/archive/%{name}/%{name}-%{version}.tar.gz
License:	MIT
Group:		System/Libraries
Url:		http://go-mono.com
BuildRequires:	pkgconfig(mono)
BuildRequires:	ndesk-dbus
BuildRequires:	monodoc
BuildRequires:	glib-sharp2
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	automake
Requires:		gnome-keyring

%description
GNOME Keyring is a system which allows you to store passwords and
other sensitive data across GNOME applications. It provides an API to
access this information, as well as a daemon to manage it.

gnome-keyring-sharp is a fully managed implementation of libgnome-keyring.

%package doc
Summary:	Development documentation for %{name}
Group:		Development/Other
Requires(post):	mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
Gecko-sharp is a C# language binding for the gtkembedmoz widget. You
can use it to embed mozilla into C# programs.

This package contains the API documentation for the %name in
Monodoc format.


%prep
%setup -q

%build
%configure2_5x --disable-static
make

%install
%makeinstall_std
%if %{_lib} != lib
mv %{buildroot}%{_libdir}/mono* %{buildroot}%{_prefix}/lib
%endif

%post doc
%{_bindir}/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %{_bindir}/monodoc ]; then %{_bindir}/monodoc --make-index > /dev/null
fi

%files
%doc README
%{_prefix}/lib/mono/gac/Gnome.Keyring
%{_prefix}/lib/mono/gnome-keyring-sharp-1.0/Gnome.Keyring.dll
%{_libdir}/libgnome-keyring-sharp-glue.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_prefix}/lib/monodoc/sources/Gnome.Keyring.*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 664870
- mass rebuild

* Tue Jul 13 2010 Götz Waschk <waschk@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 551906
- fix installation
- update build deps
- update build deps
- new version
- make it am arch-dependant package

* Fri Dec 11 2009 Götz Waschk <waschk@mandriva.org> 1.0.1-0.r127410.2mdv2010.1
+ Revision: 476293
- rebuild for new webkit-sharp

* Thu Feb 19 2009 Götz Waschk <waschk@mandriva.org> 1.0.1-0.r127410.1mdv2009.1
+ Revision: 342878
- new snapshot

* Mon Aug 11 2008 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 270734
- new version

* Mon Jul 28 2008 Götz Waschk <waschk@mandriva.org> 1.0-0.87622.2mdv2009.0
+ Revision: 251134
- fix license
- move pkgconfig file to the right directory

* Sun Jul 27 2008 Funda Wang <fwang@mandriva.org> 1.0-0.87622.1mdv2009.0
+ Revision: 250596
- New snapshot at 87622

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1.0-0.84869.1mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 27 2007 Götz Waschk <waschk@mandriva.org> 0.1.0-0.84869.1mdv2008.0
+ Revision: 71883
- use the Mono Project's gnome-keyring-sharp

* Wed Aug 08 2007 Götz Waschk <waschk@mandriva.org> 0.0.1-2mdv2008.0
+ Revision: 60226
- remove bogus dep from pkgconfig file

* Wed Aug 08 2007 Götz Waschk <waschk@mandriva.org> 0.0.1-1mdv2008.0
+ Revision: 60123
- Import gnome-keyring-sharp




* Wed Aug  8 2007 Götz Waschk <waschk@mandriva.org> 0.0.1-1mdv2008.0
- initial package
