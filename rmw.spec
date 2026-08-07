%global debug_package %{nil}

Name:		rmw
Version:	0.10.0
Release:	1
Source0:	https://github.com/theimpossibleastronaut/rmw/archive/refs/tags/v0.10.0.tar.gz#/%{name}-%{version}.tar.gz
Summary:	A trashcan/recycle bin utility for the command line
URL:		https://github.com/theimpossibleastronaut/rmw
License:	GPL-3.0-only
Group:		Tools

BuildSystem:	meson

BuildRequires:	meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(canfigger)
BuildRequires:	gettext

%description
A trashcan/recycle bin utility for the command line. It can move and 
restore files to and from directories specified in a configuration file,
and can also be integrated with your regular desktop trash folder.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_docdir}/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_mandir}/man1/%{name}.1.zst
