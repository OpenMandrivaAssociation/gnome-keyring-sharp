%define name gnome-keyring-sharp
%define version 0.0.1
%define release %mkrel 2

Summary: Mono bindings for the GNOME Keyring API
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://russell.rucus.net/2005/gnome-keyring-sharp/downloads/%{name}-%{version}.tar.bz2
Patch: gnome-keyring-sharp-0.0.1-pkgconfig.patch
License: LGPL
Group: System/Libraries
Url: http://russell.rucus.net/2005/gnome-keyring-sharp/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: gtk-sharp2
BuildRequires: gtk-sharp2-devel
BuildRequires: gnome-keyring-devel
BuildArch: noarch
Requires: gnome-keyring

%description
GNOME Keyring is a system which allows you to store passwords and
other sensitive data across GNOME applications. It provides an API to
access this information, as well as a daemon to manage it.

gnome-keyring-sharp is a set of CIL bindings for the GNOME Keyring API, 
written in C#.


%prep
%setup -q
%patch -p1

%build
./configure --prefix=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_prefix/lib/mono/gac/gnome-keyring-sharp
%_prefix/lib/mono/gnome-keyring-sharp
%_datadir/pkgconfig/gnome-keyring-sharp.pc
