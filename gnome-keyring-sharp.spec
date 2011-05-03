%define name gnome-keyring-sharp
%define version 1.0.2
%define release %mkrel 2

Summary: Mono implementation of the GNOME Keyring API
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.go-mono.com/archive/%name/%{name}-%{version}.tar.gz
License: MIT
Group: System/Libraries
Url: http://go-mono.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: ndesk-dbus
BuildRequires: monodoc
BuildRequires: glib-sharp2
BuildRequires: libgnome-keyring-devel
BuildRequires: automake
Requires: gnome-keyring

%description
GNOME Keyring is a system which allows you to store passwords and
other sensitive data across GNOME applications. It provides an API to
access this information, as well as a daemon to manage it.

gnome-keyring-sharp is a fully managed implementation of libgnome-keyring.

%package doc
Summary: Development documentation for %name
Group: Development/Other
Requires(post): mono-tools >= 1.1.9
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%if %_lib != lib
mv %buildroot%_libdir/mono* %buildroot%_prefix/lib
%endif
%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi


%files
%defattr(-,root,root)
%doc README
%{_prefix}/lib/mono/gac/Gnome.Keyring
%{_prefix}/lib/mono/gnome-keyring-sharp-1.0/Gnome.Keyring.dll
%_libdir/libgnome-keyring-sharp-glue.so
%_libdir/libgnome-keyring-sharp-glue.la
%_libdir/pkgconfig/*.pc

%files doc
%defattr(-,root,root)
%{_prefix}/lib/monodoc/sources/Gnome.Keyring.*
