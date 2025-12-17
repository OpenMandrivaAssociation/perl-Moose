%define modname	Moose

Summary:	A complete modern object system for Perl 5
Name:		perl-%{modname}
Version:	2.2207
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Moose
Source0:	http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Moose-%{version}.tar.gz
Patch0:		Moose-2.2010-buildfix.patch
BuildRequires:	perl(Class::Load)
BuildRequires:	perl(Data::OptList)
BuildRequires:	perl(Devel::GlobalDestruction)
BuildRequires:	perl(Devel::StackTrace)
BuildRequires:	perl(Dist::CheckConflicts)
BuildRequires:	perl(Eval::Closure)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Package::DeprecationManager)
BuildRequires:	perl(Package::Stash)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Task::Weaken)
#BuildRequires:	perl(Test::Output)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::LongString)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl-devel
Requires:	perl(Sub::Name)
Provides:	perl-Moose-implementation
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
