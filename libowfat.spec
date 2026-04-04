Summary:	libowfat - reimplement libdjb
Summary(pl.UTF-8):	libowfat - reimplementacja libdjb
Name:		libowfat
Version:	0.34
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://www.fefe.de/libowfat/%{name}-%{version}.tar.xz
# Source0-md5:	ca7ca7c14e66cc148ac663a29126f4d0
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.fefe.de/libowfat/
BuildRequires:	gcc >= 6:7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libowfat is a library of general purpose APIs extracted from Dan
Bernstein's software.

%description -l pl.UTF-8
libowfat to biblioteka ogólnego przeznaczenia zawierająca interfejsy
(API) wyciągnięte z oprogramowania Dana Bernsteina.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -std=gnu17 -I." \
	DIET=

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{_libdir}/libowfat.a
%{_includedir}/libowfat
%{_mandir}/man3/add_of.3*
%{_mandir}/man3/array*.3*
%{_mandir}/man3/assign.3*
%{_mandir}/man3/bs_capacityassert.3*
%{_mandir}/man3/buffer*.3*
%{_mandir}/man3/byte_*.3*
%{_mandir}/man3/carp.3*
%{_mandir}/man3/carpsys.3*
%{_mandir}/man3/case_*.3*
%{_mandir}/man3/cdb_*.3*
%{_mandir}/man3/critbit0_*.3*
%{_mandir}/man3/die.3*
%{_mandir}/man3/diesys.3*
%{_mandir}/man3/dns_*.3*
%{_mandir}/man3/errmsg_iam.3*
%{_mandir}/man3/fmt_*.3*
%{_mandir}/man3/iarray_*.3*
%{_mandir}/man3/imult*.3*
%{_mandir}/man3/io_*.3*
%{_mandir}/man3/iob_*.3*
%{_mandir}/man3/iom_*.3*
%{_mandir}/man3/iopause.3*
%{_mandir}/man3/mmap_*.3*
%{_mandir}/man3/msg.3*
%{_mandir}/man3/msgsys.3*
%{_mandir}/man3/ndelay_*.3*
%{_mandir}/man3/open*.3*
%{_mandir}/man3/range*.3*
%{_mandir}/man3/readclose*.3*
%{_mandir}/man3/scan_*.3*
%{_mandir}/man3/socket_*.3*
%{_mandir}/man3/str_*.3*
%{_mandir}/man3/stralloc_*.3*
%{_mandir}/man3/sub_of.3*
%{_mandir}/man3/tai_*.3*
%{_mandir}/man3/taia_*.3*
%{_mandir}/man3/uint16_*.3*
%{_mandir}/man3/uint32_*.3*
%{_mandir}/man3/uint64_*.3*
%{_mandir}/man3/umult*.3*
