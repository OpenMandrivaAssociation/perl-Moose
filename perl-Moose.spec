%define module	Moose
%define name	perl-%{module}
%define version 0.62
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A complete modern object system for Perl 5
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{module}-%{version}.tar.gz
License:	GPL
Group:		Development/Perl
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Class::MOP) >= 0.68
BuildRequires:	perl(Test::LongString)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(List::MoreUtils)
Requires:	perl(Sub::Name)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Moose is an extension of the Perl 5 object system.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%__make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Moose
%{perl_vendorlib}/Moose.pm
%{perl_vendorlib}/oose.pm
%{perl_vendorlib}/Test/Moose.pm
%{_mandir}/*/*

