Summary:	HDD temperature sensor
Summary(pl):	Czujka temperatury dysku twardego
Name:		hddtemp
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://coredump.free.fr/linux/%{name}-%{version}.tar.gz
Source1:	http://coredump.free.fr/linux/%{name}.db
URL:		http://coredump.free.fr/linux/harddrive.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hddtemp is tool that give you the temperature of your IDE hard drive
by reading S.M.A.R.T. informations. Only moderns hard drives have a
temperature sensor. SCSI doesn't allow reading S.M.A.R.T.
informations.

%description -l pl
hddtemp jest narz�dziem sprawdzaj�cym temperatur� dysku twardego IDE
korzystaj�c z technologii S.M.A.R.T. Tylko nowoczesne dyski twarde
posiadaj� czujk� temperatury. SCSI nie pozwala na odczyt informacji ze
S.M.A.R.T.

%prep
%setup -q

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
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_datadir}}

install hddtemp $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/*
