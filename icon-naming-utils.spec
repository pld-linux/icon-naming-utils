%include	/usr/lib/rpm/macros.perl
Summary:	Icon naming utility
Summary(pl.UTF-8):	Narzędzie do nadawania nazw ikonom
Name:		icon-naming-utils
Version:	0.8.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://tango.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	7a7d340f59c7a6c26391e906b7afa08c
Patch0:		%{name}-paths.patch
URL:		http://tango-project.org/Standard_Icon_Naming_Specification
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-XML-Simple
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# noarch
%define		_pkgconfigdir	%{_datadir}/pkgconfig

%description
This utility maps the icon names used by the GNOME and KDE desktops to
the icon names proposed in the Icon Naming Specification.

%description -l pl.UTF-8
Narzędzie to adaptuje nazwy ikon używanych przez środowiska GNOME i
KDE do nazw zaproponowanych w standardzie Icon Naming Specification.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pkgconfigdir}/*.pc
