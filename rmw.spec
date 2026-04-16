%global debug_package %{nil}

Name:		rmw
Version:	0.9.5
Release:	1
Source0:	https://github.com/theimpossibleastronaut/rmw/archive/refs/tags/v0.9.5.tar.gz#/%{name}-%{version}.tar.gz
Summary:	A trashcan/recycle bin utility for the command line
URL:		https://github.com/theimpossibleastronaut/rmw
License:	GPLv3
Group:		Tools

BuildSystem:	meson

BuildRequires:	meson
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
%{_mandir}/man1/%{name}.1.zst
