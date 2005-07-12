Summary:	libowfat - reimplement libdjb
Name:		libowfat
Version:	0.23
Release:	0.2
License:	GPL
Group:		Applications
Source0:	http://dl.fefe.de/%{name}-%{version}.tar.bz2
# Source0-md5:	08b0686d2423dc586fe732ee3c51b0c3
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.fefe.de/libowfat/
BuildRequires:	dietlibc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libowfat is a library of general purpose APIs extracted from Dan
Bernstein's software, reimplemented and covered by the GNU General
Public License Version 2 (no later versions).

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_libdir}/*
%{_includedir}/*.h
%{_mandir}/man3/*
