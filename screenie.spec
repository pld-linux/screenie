Summary:	Lightweight screen(1) frontend
Summary(pl.UTF-8):	Lekki frontend do programu screen(1)
Name:		screenie
Version:	1.30.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://pubwww.fhzh.ch/~mgloor/data/%{name}-%{version}.tar.gz
# Source0-md5:	bdd72ff7655c1ec24bb019cccffce7d3
URL:		http://pubwww.fhzh.ch/~mgloor/screenie.html
Requires:	screen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Screenie is a small and lightweight GNU screen(1) frontend that is
designed to be a session handler that simplifies the process of
administrating detached jobs by providing an interactive menu.

%description -l pl.UTF-8
Screenie to mały i lekki frontend do programu GNU screen(1)
zaprojektowany do obsługi sesji upraszczający proces administrowania
odłączonymi zadaniami poprzez interaktywne menu.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install screenie.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/screenie.1*
