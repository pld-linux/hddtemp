# TODO:
# - it can work as daemon - make separate subpackage with that.
%define		_beta	beta12
Summary:	HDD temperature sensor
Summary(pl):	Czujka temperatury dysku twardego
Name:		hddtemp
Version:	0.3
Release:	0.%{_beta}.1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.guzu.net/linux/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	51f19658fa6e745eee62f6e100838884
Source1:	http://www.guzu.net/linux/%{name}.db
# Source1-md5:	f816512c3feee3cc9a92a9a8d27e9cff
URL:		http://www.guzu.net/linux/hddtemp.php
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hddtemp is tool that gives you the temperature of your IDE hard drive
by reading S.M.A.R.T. informations. Only modern hard drives have a
temperature sensor. hddtemp doesn't support reading S.M.A.R.T.
informations from SCSI devices.

%description -l pl
hddtemp jest narzêdziem sprawdzaj±cym temperaturê dysku twardego IDE
korzystaj±c z technologii S.M.A.R.T. Tylko nowoczesne dyski twarde
posiadaj± czujnik temperatury. hddtemp nie potrafi odczytaæ informacji
S.M.A.R.T. z urz±dzeñ SCSI.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
cp -f /usr/share/automake/config.* .
%configure \
	--with-db-path=%{_datadir}/misc/hddtemp.db
%{__make}

%install
#rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_datadir}/misc/}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/misc/hddtemp.db

%find_lang %{name}

%clean
#rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%{_datadir}/misc/*
