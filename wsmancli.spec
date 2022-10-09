Summary:	Command line client utilities for WS-Management
Summary(pl.UTF-8):	Narzędzia klienckie do zarządzania WS z linii poleceń
Name:		wsmancli
Version:	2.6.0
Release:	1
License:	BSD
Group:		Applications/System
#Source0Download: https://github.com/Openwsman/wsmancli/releases
Source0:	https://github.com/Openwsman/wsmancli/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	df418d6d78160fd4f88f890a8953907a
URL:		https://github.com/Openwsman/wsmancli
# for tests
#BuildRequires:	CUnit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openwsman-devel >= 2.6.0
BuildRequires:	pkgconfig
Requires:	openwsman-libs >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides:
- wsman: CLI utility for resource management over the WS-Management
  protocol
- wseventmgr: CLI utility for event management over the WS-Management
  protocol

%description -l pl.UTF-8
Ten pakiet zawiera:
- wsman - narzędzie linii poleceń do zarządzania zasobami przy użyciu
  protokołu WS-Management
- wseventmgr - narzędzie linii poleceń do zarządzania zdarzeniami przy
  użyciu protokołu WS-Management

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog 
%attr(755,root,root) %{_bindir}/wseventmgr
%attr(755,root,root) %{_bindir}/wsman
%{_mandir}/man1/wseventmgr.1*
%{_mandir}/man1/wsman.1*
