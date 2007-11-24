%define		_beta	beta15
%define		_rel	2
Summary:	HDD temperature sensor
Summary(pl.UTF-8):	Czujka temperatury dysku twardego
Name:		hddtemp
Version:	0.3
Release:	0.%{_beta}.%{_rel}
License:	GPL v2
Group:		Applications/System
Source0:	http://www.guzu.net/files/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	8b829339e1ae9df701684ec239021bb8
# from http://www.guzu.net/linux/hddtemp.db
Source1:	%{name}.db
Source2:	%{name}d.init
Source3:	%{name}d.sysconfig
Source4:	%{name}-pl.po
URL:		http://www.guzu.net/linux/hddtemp.php
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hddtemp is tool that gives you the temperature of your IDE hard drive
by reading S.M.A.R.T. informations. Only modern hard drives have a
temperature sensor. hddtemp doesn't support reading S.M.A.R.T.
informations from SCSI devices.

%description -l pl.UTF-8
hddtemp jest narzędziem sprawdzającym temperaturę dysku twardego IDE
korzystając z technologii S.M.A.R.T. Tylko nowoczesne dyski twarde
posiadają czujnik temperatury. hddtemp nie potrafi odczytać informacji
S.M.A.R.T. z urządzeń SCSI.

%package hddtempd
Summary:	hddtemp daemon
Summary(pl.UTF-8):	Demon hddtemp
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts

%description hddtempd
hddtemp in daemon mode.

%description hddtempd
hddtemp w trybie demona.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

cp %{SOURCE4} po/pl.po
echo 'pl' >> po/LINGUAS
rm -f po/stamp-po

%build
cp -f /usr/share/automake/config.* .
%configure \
	--with-db-path=%{_datadir}/misc/hddtemp.db
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_datadir}/misc/} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/misc/hddtemp.db

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/hddtempd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/hddtempd

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post hddtempd
/sbin/chkconfig --add hddtempd
if [ "$1" = 1 ]; then
	echo "You have to configure hddtempd in /etc/sysconfig/hddtempd."
fi
%service hddtempd restart "hddtempd daemon"

%preun hddtempd
if [ "$1" = "0" ]; then
	%service hddtempd stop
	/sbin/chkconfig --del hddtempd
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%{_datadir}/misc/*

%files hddtempd
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/hddtempd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/hddtempd
