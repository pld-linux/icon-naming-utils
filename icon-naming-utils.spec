%include	/usr/lib/rpm/macros.perl
Summary:	Icon naming utility
Summary(pl):	Narzêdzie do nadawania nazw ikonom
Name:		icon-naming-utils
Version:	0.6.7
Release:	1
License:	GPL
Group:		Applications
Source0:	http://tango-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	46443ee6ac3ee85b1a72b2abc55a770a
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
Narzêdzie to adaptuje nazwy ikon u¿ywanych przez ¶rodowiska GNOME i
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
