%include	/usr/lib/rpm/macros.perl
Summary:	Icon naming utility
Summary(pl):	Narz�dzie do nadawania nazw ikonom
Name:		icon-naming-utils
Version:	0.6.6
Release:	1
License:	GPL
Group:		Applications
Source0:	http://tango-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	70e20fc78317c530e4fca1a6cb42d1a7
Patch0:		%{name}-paths.patch
URL:		http://tango-project.org/Standard_Icon_Naming_Specification
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-XML-Simple
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility maps the icon names used by the GNOME and KDE desktops to
the icon names proposed in the Icon Naming Specification.

%description -l pl
Narz�dzie to adaptuje nazwy ikon u�ywanych przez �rodowiska GNOME i
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
