Summary:	Graphical predictive text entry system
Name:		dasher
Version:	4.11
Release:	7
License:	GPLv2+
Group:		Accessibility
URL:		http://www.dasher.org.uk/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		dasher-4.9.0-fix-stringformat.patch
BuildRequires:	expat-devel
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(gnome-speech-1.0)
BuildRequires:	pkgconfig(libspi-1.0)
BuildRequires:	scrollkeeper
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	perl-XML-Parser
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
Requires(post):	scrollkeeper
Requires(postun): scrollkeeper

%description 
Dasher is an information-efficient text-entry interface, driven by natural 
continuous pointing gestures. Dasher is a  competitive  text-entry
system wherever a full-size keyboard cannot be used.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x 
%make LIBS="-lX11"

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
rm -rf %{buildroot}/var/lib/scrollkeeper

%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Accessibility" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

mkdir -p %{buildroot}%{_miconsdir}
install -m 644 -D Data/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png
convert -scale 32 Data/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png
convert -scale 16 Data/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png

%files -f %{name}.lang
%doc README AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/dasher.schemas
%{_bindir}/*
%{_datadir}/applications/dasher.desktop
%{_datadir}/dasher
%{_datadir}/icons/hicolor/scalable/apps/dasher.svg
%{_datadir}/icons/hicolor/48x48/apps/dasher.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_mandir}/man1/*

%changelog
* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 4.11-4mdv2011.0
+ Revision: 677069
- rebuild to add gconf2 as req

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 4.11-3
+ Revision: 663751
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 4.11-2mdv2011.0
+ Revision: 604775
- rebuild

* Sun Mar 14 2010 GÃ¶tz Waschk <waschk@mandriva.org> 4.11-1mdv2010.1
+ Revision: 518837
- update to new version 4.11

* Mon Apr 27 2009 GÃ¶tz Waschk <waschk@mandriva.org> 4.10.1-1mdv2010.0
+ Revision: 369078
- update to new version 4.10.1

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 4.10.0-1mdv2009.1
+ Revision: 356240
- new version
- update file list

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - Fix string format

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 4.9.0-1mdv2009.0
+ Revision: 230958
- new version
- drop patch
- update url

* Mon Jun 30 2008 Frederic Crozat <fcrozat@mandriva.com> 4.7.3-2mdv2009.0
+ Revision: 230203
- Fix buildrequires
- Patch0: fix linking
- Fix missing endif
- Add missing macros and migrate to new filetrigger

* Wed Apr 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 4.7.3-1mdv2009.0
+ Revision: 192480
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 4.7.0-1mdv2008.1
+ Revision: 108580
- new version
- new version

* Mon Oct 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 4.6.1-1mdv2008.1
+ Revision: 98731
- new version

* Tue Sep 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 4.6.0-1mdv2008.0
+ Revision: 89453
- new version

* Mon Aug 06 2007 Frederic Crozat <fcrozat@mandriva.com> 4.5.2-2mdv2008.0
+ Revision: 59401
- Fix url (Mdv bug #21664)

* Mon Jul 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 4.5.2-1mdv2008.0
+ Revision: 50634
- new version

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 4.5.1-2mdv2008.0
+ Revision: 36134
- rebuild with correct optflags

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - new version

* Tue May 29 2007 GÃ¶tz Waschk <waschk@mandriva.org> 4.4.2-1mdv2008.0
+ Revision: 32414
- fix buildrequires
- new version

* Tue Apr 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 4.4.1-1mdv2008.0
+ Revision: 13826
- new version


* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 4.4.0-1mdv2007.1
+ Revision: 142016
- new version

* Sun Feb 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 4.3.5-1mdv2007.1
+ Revision: 125676
- new version

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 4.3.4-1mdv2007.1
+ Revision: 120127
- new version

* Tue Dec 19 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.3.3-1mdv2007.1
+ Revision: 99072
- new version

* Tue Dec 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.3.2-1mdv2007.1
+ Revision: 90710
- new version
- drop patch

* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.3.1-2mdv2007.1
+ Revision: 87921
- bot rebuild
- new version
- patch to fix build
- depend on libcanna
- add gconf and scrollkeeper stuff

* Wed Nov 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.2.2-1mdv2007.1
+ Revision: 86307
- new version

* Thu Oct 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.2.1-1mdv2007.0
+ Revision: 72573
- Import dasher

* Thu Oct 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.2.1-1mdv2007.1
- New version 4.2.1

* Mon Sep 04 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.2.0-1mdv2007.0
- New release 4.2.0

* Fri Aug 25 2006 Götz Waschk <waschk@mandriva.org> 4.1.10-2mdv2007.0
- fix buildrequires

* Wed Aug 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.1.10-1mdv2007.0
- New release 4.1.10

* Wed Aug 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.1.9-1mdv2007.0
- New release 4.1.9

* Tue Aug 08 2006 Götz Waschk <waschk@mandriva.org> 4.1.8-3mdv2007.0
- fix buildrequires

* Thu Aug 03 2006 Frederic Crozat <fcrozat@mandriva.com> 4.1.8-2mdv2007.0
- Rebuild with latest dbus

* Wed Jul 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.1.8-1
- New release 4.1.8

* Wed Jul 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.1.7-1mdv2007.0
- New release 4.1.7

* Fri Jun 30 2006 Nicolas Lécureuil <neoclust@mandriva.org> 4.1.4-2mdv2007.0
- Fix menu entry

* Fri Jun 30 2006 Jerome Soyer <saispo@mandriva.org> 4.1.4-1mdv2007.0
- Release 4.1.4
- XDG Menu

* Sat Jun 03 2006 Frederic Crozat <fcrozat@mandriva.com> 4.1.0-1mdv2007.0
- Release 4.1.0

* Mon Apr 03 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.0.2-1mdk
- New release 4.0.2

* Sat Mar 18 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.0.1-1mdk
- New release 4.0.1

* Mon Mar 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.0.0-1mdk
- New release 4.0.0

* Sun Feb 26 2006 Götz Waschk <waschk@mandriva.org> 3.99.5-1mdk
- update file list
- New release 3.99.5

* Mon Feb 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 3.99.4-1mdk
- New release 3.99.4

* Tue Jan 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 3.99.3-1mdk
- New release 3.99.3

* Mon Jan 30 2006 Götz Waschk <waschk@mandriva.org> 3.99.2-1mdk
- update file list
- New release 3.99.2

* Mon Jan 16 2006 GÃ¶tz Waschk <waschk@mandriva.org> 3.99.1-1mdk
- New release 3.99.1
- use mkrel

* Mon Jan 09 2006 Marcel Pol <mpol@mandriva.org> 3.2.18-3mdk
- rebuild for new openssl

* Thu Oct 13 2005 GÃ¶tz Waschk <waschk@mandriva.org> 3.2.18-2mdk
- rebuild for new libwnck

* Tue Sep 06 2005 GÃ¶tz Waschk <waschk@mandriva.org> 3.2.18-1mdk
- New release 3.2.18

* Mon Aug 29 2005 GÃ¶tz Waschk <waschk@mandriva.org> 3.2.17-1mdk
- New release 3.2.17

* Wed Aug 24 2005 Götz Waschk <waschk@mandriva.org> 3.2.16-1mdk
- fix icon
- replace prereq
- New release 3.2.16

* Tue May 10 2005 Frederic Crozat <fcrozat@mandriva.com> 3.2.15-3mdk 
- Remove patch0 (not needed with libwnck 2.10.x)

* Tue Apr 12 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 3.2.15-2mdk 
- fix build (Mdk bug #15367)
- Patch0 (CVS): use old libwnck API

* Wed Mar 09 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 3.2.15-1mdk
- New release 3.2.15

* Thu Feb 03 2005 Götz Waschk <waschk@linux-mandrake.com> 3.2.13-2mdk
- fix buildrequires

* Sun Jan 30 2005 Goetz Waschk <waschk@linux-mandrake.com> 3.2.13-1mdk
- New release 3.2.13

* Wed Jan 12 2005 Goetz Waschk <waschk@linux-mandrake.com> 3.2.12-1mdk
- New release 3.2.12

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 3.2.11-3mdk 
- Rebuild with latest howl

* Sun Nov 21 2004 Abel Cheung <deaddog@mandrake.org> 3.2.11-2mdk
- Fix BuildRequires

* Wed Oct 20 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 3.2.11-1mdk
- New release 3.2.11

* Fri Aug 27 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 3.2.10-3mdk
- Fix menu

* Sat Jul 24 2004 Michael Scherer <misc@mandrake.org> 3.2.10-2mdk 
- rebuild with new gcc

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 3.2.10-1mdk
- New release 3.2.10

* Wed Apr 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 3.2.9-1mdk
- New release 3.2.9

