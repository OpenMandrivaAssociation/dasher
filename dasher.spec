%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Graphical predictive text entry system
Name:		dasher
Version:	4.11
Release:	11
License:	GPLv2+
Group:		Accessibility
Url:		http://www.dasher.org.uk/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/dasher/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		dasher-4.9.0-fix-stringformat.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-speech-1.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libspi-1.0)
BuildRequires:	pkgconfig(libwnck-1.0)

%description 
Dasher is an information-efficient text-entry interface, driven by natural 
continuous pointing gestures. Dasher is a  competitive  text-entry
system wherever a full-size keyboard cannot be used.

%prep
%setup -q
%apply_patches

%build
%configure2_5x

%make LIBS="-lX11"

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-MoreApplications-Accessibility" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

mkdir -p %{buildroot}%{_miconsdir}

%files -f %{name}.lang
%doc README AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/dasher.schemas
%{_bindir}/*
%{_datadir}/applications/dasher.desktop
%{_datadir}/dasher
%{_iconsdir}/hicolor/scalable/apps/dasher.svg
%{_iconsdir}/hicolor/48x48/apps/dasher.png
%{_mandir}/man1/*

