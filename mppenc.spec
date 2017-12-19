Summary:	Musepack SV7 encoder
Summary(pl.UTF-8):	Koder formatu Musepack SV7
Name:		mppenc
Version:	1.16
Release:	1
License:	LGPL v2.1+
Group:		Applications/Sound
#Source0Download: https://www.musepack.net/index.php?pg=src
Source0:	https://files.musepack.net/source/%{name}-%{version}.tar.bz2
# Source0-md5:	f1456141283814efcc012cfa15609bc6
URL:		https://www.musepack.net/
BuildRequires:	cmake >= 2.4
Obsoletes:	mpcenc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Musepack SV7 encoder.

%description -l pl.UTF-8
Koder formatu Musepack SV7.

%prep
%setup -q

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog 
%attr(755,root,root) %{_bindir}/mppenc
