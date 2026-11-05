Name:           libtrawldb
Version:        0.1
Release:        1%{?dist}
Summary:        C client library for the trawl configuration daemon
License:        Apache-2.0
URL:            https://github.com/regolith-linux/libtrawldb
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Debian Build-Depends, as pkgconfig() capabilities where they exist.
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-unix-2.0)

# ${shlibs:Depends} and ${misc:Depends} are dropped: RPM generates library
# dependencies itself.
Requires:       trawld

%description
A C library for clients of trawld, the daemon that holds Regolith's X
resources style configuration on the D-Bus session bus.

# Not in Debian, which ships the headers and the pkg-config file in
# libtrawldb itself. Fedora keeps development files in -devel.
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, the shared library link used at link time and the trawldb-0
pkg-config file for building against %{name}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_libdir}/libtrawl-client.so.0
%{_libdir}/libtrawl-client.so.0.1

%files          devel
%{_includedir}/trawldb/
%{_libdir}/libtrawl-client.so
%{_libdir}/pkgconfig/trawldb-0.pc

%changelog
* Wed Nov 04 2026 Regolith Fedora Port <port@regolith.invalid> - 0.1-1
- Initial package
