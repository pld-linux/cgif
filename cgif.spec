#
# Conditional build:
%bcond_without	static_libs	# static libraries
#
Summary:	CGIF - GIF encoder written in C
Summary(pl.UTF-8):	CGIF - koder GIF napisany w C
Name:		cgif
Version:	0.4.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/dloebl/cgif/releases
Source0:	https://github.com/dloebl/cgif/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3f3f31762e750dd380d32f6b65c523cc
URL:		https://github.com/dloebl/cgif
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast and lightweight GIF encoder that can create GIF animations and
images.

%description -l pl.UTF-8
Szybki i lekki koder GIF, potrafiący tworzyć animacje oraz obrazy GIF.

%package devel
Summary:	Header files for cgif library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cgif
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cgif library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cgif.

%package static
Summary:	Static cgif library
Summary(pl.UTF-8):	Statyczna biblioteka cgif
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cgif library.

%description static -l pl.UTF-8
Statyczna biblioteka cgif.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_libdir}/libcgif.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcgif.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcgif.so
%{_includedir}/cgif.h
%{_pkgconfigdir}/cgif.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcgif.a
%endif
