Summary: Graphical predictive text entry system
Name: dasher
Version: 4.4.1
Release: %mkrel 1
License: GPL
Group: Accessibility
URL: http://www.infer-ence.phy.cam.ac.uk/dasher/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: expat-devel
BuildRequires: libglade2.0-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libwnck-devel >= 2.10.0
BuildRequires: gnome-speech-devel
BuildRequires: at-spi-devel
BuildRequires: libcanna-devel
BuildRequires: scrollkeeper
BuildRequires: gnome-doc-utils
BuildRequires: perl-XML-Parser
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description 
Dasher is an information-efficient text-entry interface, driven by natural 
continuous pointing gestures. Dasher is a  competitive  text-entry
system wherever a full-size keyboard cannot be used.

%prep
%setup -q

%build

%configure2_5x 

%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
rm -rf %buildroot/var/lib/scrollkeeper

%find_lang %{name} --with-gnome
for omf in %buildroot%_datadir/omf/*/*-??.omf;do
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed s!%buildroot!!)" >> %name.lang
done


desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-MoreApplications-Accessibility" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p %buildroot%_miconsdir
install -m 644 -D Data/%name.png %buildroot%_liconsdir/%name.png
convert -scale 32 Data/%name.png %buildroot%_iconsdir/%name.png
convert -scale 16 Data/%name.png %buildroot%_miconsdir/%name.png

%post
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q || true ; fi
%{update_desktop_database}
%post_install_gconf_schemas dasher

%preun
%preun_uninstall_gconf_schemas dasher

%postun
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q || true ; fi
%{clean_desktop_database}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS ChangeLog
%_sysconfdir/gconf/schemas/dasher.schemas
%{_bindir}/*
%{_datadir}/applications/dasher.desktop
%{_datadir}/dasher
%_datadir/icons/hicolor/scalable/apps/dasher.svg
%_datadir/icons/hicolor/48x48/apps/dasher.png
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
%{_mandir}/man1/*
%{_datadir}/omf/dasher/dasher-C.omf
