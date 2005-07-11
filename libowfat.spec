Summary:	libowfat - reimplement libdjb
Name:		libowfat
Version:	0.23
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.fefe.de/%{name}-%{version}.tar.bz2
# Source0-md5:	08b0686d2423dc586fe732ee3c51b0c3
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.fefe.de/libowfat/
BuildRequires:	dietlibc-devel
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One of the best ways to learn good programming practices is to read
others people's code. I have read the source code from a lot of
people. One of the most inspiring moments of my career as C programmer
was to look at Dan Bernstein's code. While most programmers stumble
about bad APIs throughout their life, Dan started not only question
them, but he defined new and better APIs and implemented them.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO

%attr(755,root,root) /opt/diet/*
