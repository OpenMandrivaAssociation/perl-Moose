%define upstream_name	 Moose
%define upstream_version 2.0604

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Moose::Conflicts\\)'
%else
%define _requires_exceptions perl(Moose::Conflicts)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6
Summary:	A complete modern object system for Perl 5
License:    GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DO/DOY/%{upstream_name}-%{upstream_version}.tar.gz
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
Obsoletes:	perl-Class-MOP <= 1.120.0
Provides:	perl-Class-MOP = 1.120.0

%description
Moose is an extension of the Perl 5 object system.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/moose-outdated
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.1.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-3
+ Revision: 765494
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-2
+ Revision: 763989
- rebuilt for perl-5.14.x

* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.0-1
+ Revision: 686642
- update to new version 2.0010

* Mon May 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.700-1
+ Revision: 675016
- update to new version 2.0007

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.600-2
+ Revision: 674607
- fix dependencies

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.600-1
+ Revision: 673815
- update to new version 2.0006

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.200-1
+ Revision: 662124
- update to new version 2.0002

* Wed Apr 27 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.100-5
+ Revision: 659669
- obsoletes perl-Class-MOP, as it has been merged with Moose
- no dependency on additional Moose packages
- fix conflict with perl-Class-MOP

  + Funda Wang <fwang@mandriva.org>
    - rebuild for updated spec-helper

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 2.0.100-3
+ Revision: 658239
- add more req

* Sat Apr 23 2011 Jani Välimaa <wally@mandriva.org> 2.0.100-2
+ Revision: 657758
- package isn't noarch package
- debug files belongs to -debug package

* Sat Apr 23 2011 Sandro Cazzaniga <kharec@mandriva.org> 2.0.100-1
+ Revision: 657734
- fix file
- fix file list
- Buildarch is now noarch for fix build
- remove an unless br
- Add a BR on Eval::Closure (pkg just created before)
- new version 2.0001
- packaged /usr/bin/moose-outdated
- add a BR on Test::Output

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.240.0-1
+ Revision: 639659
- update to new version 1.24
- update to new version 1.23

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.210.0-1mdv2011.0
+ Revision: 601934
- update to new version 1.21

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.190.0-1mdv2011.0
+ Revision: 594671
- update to new version 1.19

* Tue Nov 02 2010 Shlomi Fish <shlomif@mandriva.org> 1.170.0-2mdv2011.0
+ Revision: 592303
- Updated the versions of the BuildRequires

* Tue Oct 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 586835
- update to new version 1.17

  + Shlomi Fish <shlomif@mandriva.org>
    - Add missing dependencies

* Sun Oct 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.150.0-1mdv2011.0
+ Revision: 586167
- new version

* Wed Sep 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 575077
- adding missing buildrequires:
- update to 1.12

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 572937
- update to 1.10

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2011.0
+ Revision: 561954
- update to 1.09

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-2mdv2011.0
+ Revision: 556007
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 552244
- update to 1.08

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-2mdv2010.1
+ Revision: 528111
- rebuild
- update to 1.01

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 527733
- update to 1.00

* Fri Mar 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.990.0-2mdv2010.1
+ Revision: 518457
- ship debug files in -debug

* Tue Mar 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.990.0-1mdv2010.1
+ Revision: 517114
- update to 0.99

* Thu Feb 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.980.0-1mdv2010.1
+ Revision: 504075
- update to 0.98

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.970.0-1mdv2010.1
+ Revision: 503735
- update to 0.97

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.960.0-1mdv2010.1
+ Revision: 502087
- update to 0.96

* Fri Feb 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.950.0-1mdv2010.1
+ Revision: 501138
- update to 0.95

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.940.0-1mdv2010.1
+ Revision: 493553
- package has some xs parts now
- update to 0.94

* Sat Nov 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.930.0-1mdv2010.1
+ Revision: 467880
- update to 0.93

* Wed Sep 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.0
+ Revision: 447633
- update to 0.92

* Mon Sep 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.910.0-1mdv2010.0
+ Revision: 446431
- update to 0.91

* Wed Sep 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.900.0-1mdv2010.0
+ Revision: 443511
- adding missing buildrequires:
- update to 0.90

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.890.0-1mdv2010.0
+ Revision: 418663
- update to 0.89

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.880.0-1mdv2010.0
+ Revision: 399595
- update to 0.88

* Wed Jul 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.870.0-1mdv2010.0
+ Revision: 393635
- update to 0.87

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.860.0-1mdv2010.0
+ Revision: 392692
- update to 0.86
- using %%perl_convert_version
- fixed license field

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.85-1mdv2010.0
+ Revision: 389796
- update to new version 0.85

* Thu Jun 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.83-1mdv2010.0
+ Revision: 389017
- update to new version 0.83

* Tue Jun 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.82-1mdv2010.0
+ Revision: 388738
- update to new version 0.82

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.81-1mdv2010.0
+ Revision: 384027
- update to new version 0.81

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.79-2mdv2010.0
+ Revision: 378180
- provides perl-Moose-implementation virtual package

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.79-1mdv2010.0
+ Revision: 376150
- update to new version 0.79

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.77-1mdv2010.0
+ Revision: 371455
- new version

* Sat Feb 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.72-1mdv2009.1
+ Revision: 345915
- update to new version 0.72

* Fri Feb 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.71-1mdv2009.1
+ Revision: 343229
- update to new version 0.71

* Sun Feb 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.70-1mdv2009.1
+ Revision: 340567
- update to new version 0.70

* Fri Feb 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.69-1mdv2009.1
+ Revision: 340032
- update to new version 0.69

* Thu Feb 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.68-1mdv2009.1
+ Revision: 337784
- update to new version 0.68

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.66-1mdv2009.1
+ Revision: 337425
- update to new version 0.66

* Fri Jan 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.65-1mdv2009.1
+ Revision: 332993
- update to new version 0.65

* Mon Jan 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.64-1mdv2009.1
+ Revision: 325017
- new version

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-1mdv2009.1
+ Revision: 314253
- update to new version 0.63

* Fri Nov 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.62-1mdv2009.1
+ Revision: 307417
- update to new version 0.62

* Sat Nov 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.61-1mdv2009.1
+ Revision: 301108
- new version

* Sun Oct 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.60-2mdv2009.1
+ Revision: 297292
- fix dependencies

* Sat Oct 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.60-1mdv2009.1
+ Revision: 297201
- new version

* Tue Oct 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.59-1mdv2009.1
+ Revision: 296085
- new version

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.57-1mdv2009.0
+ Revision: 281701
- new version

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.56-1mdv2009.0
+ Revision: 279193
- new version

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdv2009.0
+ Revision: 270491
- new version

* Sun Jul 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.54-1mdv2009.0
+ Revision: 232130
- update to new version 0.54

* Fri Jul 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.53-1mdv2009.0
+ Revision: 231602
- update to new version 0.53

* Wed Jul 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.51-1mdv2009.0
+ Revision: 230702
- new version

* Tue Jun 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-1mdv2009.0
+ Revision: 223408
- new version

* Fri May 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.48-1mdv2009.0
+ Revision: 213356
- update to new version 0.48

* Thu May 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.46-1mdv2009.0
+ Revision: 212940
- update to new version 0.46

* Tue May 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-1mdv2009.0
+ Revision: 206820
- update to new version 0.44

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-2mdv2009.0
+ Revision: 201954
- drop last build dependency, it is redundant  with Class::MOP

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-1mdv2009.0
+ Revision: 201933
- fix build dependency
- update to new version 0.43

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.40-1mdv2009.0
+ Revision: 193866
- update to new version 0.40

* Sat Feb 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2008.1
+ Revision: 169257
- update to new version 0.38

* Sun Jan 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2008.1
+ Revision: 158625
- update to new version 0.36

* Fri Jan 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2008.1
+ Revision: 158107
- update to new version 0.35

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2008.1
+ Revision: 156179
- update to new version 0.34

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2008.1
+ Revision: 121687
- new version

* Wed Dec 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2008.1
+ Revision: 115534
- new version

* Tue Nov 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2008.1
+ Revision: 113432
- new version
- new version

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2008.1
+ Revision: 110245
- new version

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2008.1
+ Revision: 97518
- update to new version 0.26

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2008.0
+ Revision: 75281
- import perl-Moose


* Wed Aug 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2008.0
- first mdv release 
