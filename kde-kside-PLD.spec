Summary:	PLD kicker sidebar
Summary(pl):	Pasek boczny PLD
Name:		kde-kside-PLD
Version:	0.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.culm.net/~adasi/%{name}-%{version}.tgz
Requires:	kdebase-kicker
Provides:	kde-kside
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD kicker sidebar

%description -l pl
Pasek boczny PLD

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
