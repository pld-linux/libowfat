Summary:	libowfat - reimplement libdjb
Summary(pl.UTF-8):	libowfat - reimplementacja libdjb
Name:		libowfat
Version:	0.24
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.fefe.de/%{name}-%{version}.tar.bz2
# Source0-md5:	a38b74998a45fd6c47e93e0fec1f6560
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.fefe.de/libowfat/
BuildRequires:	dietlibc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libowfat is a library of general purpose APIs extracted from Dan
Bernstein's software.

%description -l pl.UTF-8
libowfat to biblioteka API ogólnego przeznaczenia wyciągniętego z
oprogramowania Dana Bernsteina.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I."

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
