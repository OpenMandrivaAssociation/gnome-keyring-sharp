Summary:	Mono implementation of the GNOME Keyring API
Name:		gnome-keyring-sharp
Version:	1.0.2
Release:	9
License:	MIT
Group:		System/Libraries
Url:		http://go-mono.com
Source0:	http://www.go-mono.com/archive/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	ndesk-dbus
BuildRequires:	monodoc
BuildRequires:	pkgconfig(glib-sharp-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(mono)
Requires:	gnome-keyring

%description
GNOME Keyring is a system which allows you to store passwords and
other sensitive data across GNOME applications. It provides an API to
access this information, as well as a daemon to manage it.

gnome-keyring-sharp is a fully managed implementation of libgnome-keyring.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}

%description devel
The pkgconfig for %{name}.

%package doc
Summary:	Development documentation for %{name}
Group:		Development/Other
Requires(post,postun):	mono-tools >= 1.1.9

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

%files devel
%{_libdir}/pkgconfig/*.pc

%files doc
%{_prefix}/lib/monodoc/sources/Gnome.Keyring.*

