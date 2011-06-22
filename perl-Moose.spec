%define upstream_name	 Moose
%define upstream_version 2.0010
%define _requires_exceptions perl(Moose::Conflicts)

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
Summary:	A complete modern object system for Perl 5
License:    GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Data::OptList)
BuildRequires:	perl(Devel::GlobalDestruction)
BuildRequires:	perl(Eval::Closure)
BuildRequires:	perl(List::MoreUtils) >= 0.120.0
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Package::DeprecationManager) >= 0.070.0
BuildRequires:	perl(Package::Stash)
BuildRequires:	perl(Params::Util) >= 1.000.0
BuildRequires:	perl(Scalar::Util) >= 1.190.0
BuildRequires:	perl(Sub::Exporter) >= 0.098.0
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Task::Weaken)
#BuildRequires:	perl(Test::Output)
BuildRequires:	perl(Test::Exception) >= 0.270
BuildRequires:	perl(Test::More) >= 0.880
BuildRequires:	perl(Test::Requires) >= 0.050
BuildRequires:	perl(Test::LongString)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Try::Tiny) >= 0.020.0
BuildRequires:	perl-devel
Requires:	perl(Sub::Name)
Provides:   perl-Moose-implementation
Provides:   perl-Class-MOP
Obsoletes:  perl-Class-MOP

%description
Moose is an extension of the Perl 5 object system.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/moose-outdated
%{perl_vendorlib}/*
%{_mandir}/*/*
