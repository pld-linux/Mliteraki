
Summary:	Polish version of Mliteraki game
Summary(pl):	Polska wersja gry Mliteraki
Name:		Mliteraki
Version:	1.0
Release:	0.3
License:	GPL v2
Group:		X11/Applications/Games
Source0:	%{name}_pl-%{version}.tar.gz
# Source0-md5:	91d5372cce673c4b9270f838fcf1b7c6
Patch0:		%{name}_pl_config.patch
URL:		http://www.mardo.prv.pl
Requires:	wxGTK
BuildRequires:	wxGTK-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mliteraki is scrabble-like game. It was written by Tomasz Mularczyk on
contest on kurnik.pl. This is Polish version of game.

%description -l pl
Mliteraki jest gr± polegaj±c± na uk³adaniu wyrazów, jest to klon
popularnej gry scrabble. Zosta³a napisana przez Tomasza Mularczyka na
konkurs organizowany w portalu kurnik.pl. Jest to polska wersja gry.

%define  _instdir  /usr/local/

%prep
%setup -q -n Mliteraki
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_instdir}/bin,%{%_instdir}/games/Mliter_pl}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT$/%{_instdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_instdir}/games/Mliter_pl/
%dir %{_instdir}/games/Mliter_pl/dane/
%dir %{_instdir}/games/Mliter_pl/graf/
%dir %{_instdir}/games/Mliter_pl/html/
%dir %{_instdir}/games/Mliter_pl/slowniki/
%{_instdir}/games/Mliter_pl/*.txt
%{_instdir}/games/Mliter_pl/dane/*
%{_instdir}/games/Mliter_pl/graf/*
%{_instdir}/games/Mliter_pl/html/*
%{_instdir}/games/Mliter_pl/slowniki/*
%attr(755,root,root) %{_instdir}/games/Mliter_pl/Mliter
%attr(755,root,root) %{_instdir}/bin/*
