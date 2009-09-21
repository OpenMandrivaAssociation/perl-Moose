%define upstream_name	 Moose
%define upstream_version 0.91

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	A complete modern object system for Perl 5
License:    GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Class::MOP)     >= 0.930.0
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::LongString)
BuildRequires:	perl(Try::Tiny)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	perl(Sub::Name)
Provides:   perl-Moose-implementation

%description
Moose is an extension of the Perl 5 object system.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

