Summary:	HDD temperature sensor
Summary(pl):	Czujka temperatury dysku twardego
Name:		hddtemp
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://coredump.free.fr/linux/%{name}-%{version}.tar.gz
Source1:	http://coredump.free.fr/linux/%{name}.db
Patch0:		%{name}-types.patch
URL:		http://coredump.free.fr/linux/harddrive.html
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
%setup -q
%patch0 -p1
sed 's@/usr/share@&/misc@' hddtemp.c > hddtemp.c-
mv -f hddtemp.c- hddtemp.c

%build
%{__make} \
	CC="%{__cc}" \
%ifarch %ix86	
	CFLAGS="%{rpmcflags} -DARCH_I386" \
%else
	CFLAGS="%{rpmcflags}" \
%endif
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_datadir}/misc}

install hddtemp $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/misc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/misc/*
