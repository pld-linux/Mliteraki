Summary:	Polish version of Mliteraki game
Summary(pl.UTF-8):   Polska wersja gry Mliteraki
Name:		Mliteraki
Version:	1.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
# data from http://www.mecenat.neostrada.pl/hardmard/pliki/Mliter/ML10L.tar.gz
# sources from http://www.mecenat.neostrada.pl/hardmard/pliki/Mliter/ML10Lkod.tar.gz ?
Source0:	%{name}_pl-%{version}.tar.gz
# Source0-md5:	91d5372cce673c4b9270f838fcf1b7c6
Patch0:		%{name}_pl-fixes.patch
URL:		http://www.mardo.prv.pl/
BuildRequires:	wxGTK-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mliteraki is scrabble-like game. It was written by Tomasz Mularczyk on
contest on kurnik.pl. This is Polish version of game.

%description -l pl.UTF-8
Mliteraki jest grą polegającą na układaniu wyrazów, jest to klon
popularnej gry scrabble. Została napisana przez Tomasza Mularczyka na
konkurs organizowany w portalu kurnik.pl. Jest to polska wersja gry.

%prep
%setup -q -n Mliteraki
%patch0 -p0

%build
%{__cxx} %{rpmldflags} %{rpmcflags} \
	`wxgtk-2.4-config --cflags` `wxgtk-2.4-config --libs` -o Mliter Mliter.cpp

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/Mliter_pl}

cp -r dane $RPM_BUILD_ROOT%{_datadir}/games/Mliter_pl
cp -r graf $RPM_BUILD_ROOT%{_datadir}/games/Mliter_pl
cp -r html $RPM_BUILD_ROOT%{_datadir}/games/Mliter_pl
cp -r slowniki  $RPM_BUILD_ROOT%{_datadir}/games/Mliter_pl
install Mliter $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc czytaj.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/Mliter_pl
