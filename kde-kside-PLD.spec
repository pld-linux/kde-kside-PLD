Summary:	PLD kicker sidebar
Summary(pl.UTF-8):	Pasek boczny PLD dla kickera
Name:		kde-kside-PLD
Version:	0.1
Release:	4
License:	GPL
Group:		Themes
Source0:	http://www.culm.net/~adasi/%{name}-%{version}.tgz
# Source0-MD5:	fdad8fec9b5d3a7345bf37754e10a3ae
Requires:	kdebase-desktop >= 9:3.2.2
Provides:	kde-kside
Obsoletes:	kde-kside
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD kicker sidebar.

%description -l pl.UTF-8
Pasek boczny PLD dla kickera.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kicker/pics

cp -Rf kside{,_tile}.png $RPM_BUILD_ROOT%{_datadir}/apps/kicker/pics

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kicker/pics/*
