#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : randrproto
Version  : 1.5.0
Release  : 4
URL      : http://xorg.freedesktop.org/releases/individual/proto/randrproto-1.5.0.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/randrproto-1.5.0.tar.bz2
Summary  : Randr extension headers
Group    : Development/Tools
License  : HPND
Requires: randrproto-doc
BuildRequires : pkgconfig(xorg-macros)

%description
X Resize and Rotate Extension (RandR)
This extension defines a protocol for clients to dynamically change X screens,
so as to resize, rotate and reflect the root window of a screen.

%package dev
Summary: dev components for the randrproto package.
Group: Development

%description dev
dev components for the randrproto package.


%package doc
Summary: doc components for the randrproto package.
Group: Documentation

%description doc
doc components for the randrproto package.


%prep
%setup -q -n randrproto-1.5.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/randr.h
/usr/include/X11/extensions/randrproto.h
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/randrproto/*
