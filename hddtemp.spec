Summary:	HDD temperature sensor
Summary(pl):	Czujka temperatury dysku twardego
Name:		hddtemp
Version:	0.3
%define		_beta	beta14
Release:	0.%{_beta}.1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.guzu.net/linux/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	bbf8be4539495e18bec54af77511a680
Source1:	http://www.guzu.net/linux/%{name}.db
# NoSource1-md5: 2f831d9203e096fe06064adbe7533b31
Source2:	hddtempd.init
Source3:	hddtempd.sysconfig
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

%package hddtempd
Summary:	hddtemp daemon
Summary(pl):	Demon hddtemp
Group:		Daemons
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description hddtempd
hddtemp in daemon mode.

%description hddtempd
hddtemp w trybie demona.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

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
if [ -f /var/lock/subsys/hddtempd ]; then
	/etc/rc.d/init.d/hddtempd restart >&2
else
	echo "You have to configure hddtempd in /etc/sysconfig/hddtempd."
	echo "Then run \"/etc/rc.d/init.d/hddtempd start\" to start hddtempd daemon." >&2
fi

%preun hddtempd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/hddtempd ]; then
		/etc/rc.d/init.d/hddtempd stop >&2
	fi
	/sbin/chkconfig --del hddtempd
fi

%files hddtempd
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/hddtempd
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/hddtempd

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%{_datadir}/misc/*
