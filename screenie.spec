Summary:	lightweight screen(1) frontend
Summary(pl):	lekki frontend do screen(1)
Name:		screenie
Version:	1.25.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://pubwww.fhzh.ch/~mgloor/data/%{name}-%{version}.tar.gz
# Source0-md5:	e61d5cc3ffc2ca79297e3de3e6fcf28a
URL:		http://pubwww.fhzh.ch/~mgloor/screenie.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Screenie is a small and lightweight GNU screen(1) frontend that is
designed to be a session handler that simplifies the process of
administrating detached jobs by providing an interactive menu.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
