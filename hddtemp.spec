Summary:	HDD temperature sensor
Summary(pl):	Czujka temperatury dysku twardego
Name:		hddtemp
Version:	0.3
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://coredump.free.fr/linux/%{name}-%{version}-beta6.tar.gz
# Source0-md5:	884bdfc69dcdcb16e20159185c56efae
Source1:	http://coredump.free.fr/linux/%{name}.db
# Source1-md5:	a0e8be49b06c3fbb0142f8b36370aae9
URL:		http://coredump.free.fr/linux/hddtemp.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hddtemp is tool that give you the temperature of your IDE hard drive
by reading S.M.A.R.T. informations. Only moderns hard drives have a
temperature sensor. hddtemp doesn't support reading S.M.A.R.T.
informations from SCSI devices.

%description -l pl
hddtemp jest narzêdziem sprawdzaj±cym temperaturê dysku twardego IDE
korzystaj±c z technologii S.M.A.R.T. Tylko nowoczesne dyski twarde
posiadaj± czujkê temperatury. hddtemp nie potrafi odczytaæ informacji
S.M.A.R.T. z urz±dzeñ SCSI.

%prep
%setup -q -n %{name}-%{version}-beta6

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DARCH_I386" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}}

install hddtemp $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_sysconfdir}/*
