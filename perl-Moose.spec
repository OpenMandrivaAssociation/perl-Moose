%define modname	Moose

%ifarch %{x86_64}
# FIXME debuginfo bug workaround
%global _debugsource_template %{nil}
%endif

Summary:	A complete modern object system for Perl 5
Name:		perl-%{modname}
Version:	2.2206
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Moose
Source0:	http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Moose-%{version}.tar.gz
Patch0:		Moose-2.2010-buildfix.patch
BuildRequires:	perl(Class::Load)
BuildRequires:	perl(Data::OptList)
BuildRequires:	perl(Devel::GlobalDestruction)
BuildRequires:	perl(Devel::StackTrace)
BuildRequires:	perl(Dist::CheckConflicts)
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
Provides:	perl-Moose-implementation
Obsoletes:	perl-Class-MOP <= 1.120.0
Provides:	perl-Class-MOP = 1.120.0
# Not caught by dependency generator
Provides:	perl(Moose::Conflicts) = %{version}

%description
Moose is an extension of the Perl 5 object system.

%prep
%autosetup -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor --skipdeps

%build
%make_build

#check
#too many deps
#make test

%install
%make_install

%files
%doc Changes 
%{_bindir}/moose-outdated
%{perl_vendorarch}/*
%{_mandir}/man3/*
