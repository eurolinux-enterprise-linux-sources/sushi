Name:           sushi
Version:        3.8.1
Release:        3%{?dist}
Summary:        A quick previewer for Nautilus
Group:          User Interface/Desktops

License:        GPLv2+ with exceptions
URL:            http://live.gnome.org/ThreePointOne/Features/FilePreviewing
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/3.8/%{name}-%{version}.tar.xz

BuildRequires:  gtksourceview3-devel
BuildRequires:  intltool
BuildRequires:  gjs-devel
BuildRequires:  glib2-devel
BuildRequires:  clutter-devel
BuildRequires:  clutter-gtk-devel
BuildRequires:  clutter-gst2-devel
BuildRequires:  evince-devel
BuildRequires:  gtk3-devel
BuildRequires:  libmusicbrainz5-devel
BuildRequires:  webkitgtk3-devel

Obsoletes:      sushi-devel < 0.5.1

#Description from upstream's README.
%description
This is sushi, a quick previewer for Nautilus, the GNOME desktop
file manager.


%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f %{name}.lang
%doc README COPYING AUTHORS NEWS TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/*
%{_datadir}/glib-2.0/schemas/org.gnome.sushi.gschema.xml
%{_libexecdir}/*
%{_libdir}/sushi/


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.1-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.1-2
- Mass rebuild 2013-12-27

* Tue Apr 16 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Mon Mar 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar  5 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-2
- Rebuilt for cogl soname bump

* Thu Feb 07 2013 Richard Hughes <rhughes@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.7.4-2
- Rebuild for new cogl

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Wed Sep 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Thu Aug 30 2012 Bastien Nocera <bnocera@redhat.com> 3.5.90-1
- Update to 3.5.90
- Port to libmusicbrainz5

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 0.5.5-2
- Rebuild against new cogl/clutter

* Wed Aug 22 2012 Richard Hughes <hughsient@gmail.com> - 0.5.5-1
- Update to 0.5.5

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 0.5.4-1
- Update to 0.5.4

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 0.5.2-1
- Update to 0.5.2

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 0.5.1-1
- Update to 0.5.1
- Build with libmusicbrainz4
- Adjust the spec file for the changes in private library location
- Remove and obsolete the -devel subpackage

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Tue Mar 27 2012 Matthias Clasen <mclasen@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 0.3.92-2
- Rebuild for libevdocument3 soname bump

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 0.3.92-1
- Update to 0.3.92

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.91-3
- Rebuild against newer cogl

* Mon Mar  6 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.91-2
- Rebuild against newer cogl

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.91-1
- Update to 0.3.91

* Sun Feb 26 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.0-4
- Rebuild against new cogl

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.0-3
- Rebuild against new cogl

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Thu Nov 24 2011 Matthias Clasen <mclasen@redhat.com> - 0.2.1-3
- Rebuild against new clutter

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 0.1.92-2
- Rebuild against newer clutter

* Tue Sep 20 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.92-1
- New upstream release

* Tue Aug 30 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.90-1
- New upstream version

* Tue Jul 26 2011 Matthias Clasen <mclasen@redhat.com> - 0.0.5-1
- Update to 0.0.5

* Sat Jul 09 2011 Elad Alfassa <elad@fedoraproject.org> - 0.0.4-1
- Update to latest upstream version.

* Mon Jul 04 2011 Elad Alfassa <elad@fedoraproject.org> - 0.0.3-3
- Fix issues from review

* Sun Jul 03 2011 Elad Alfassa <elad@fedoraproject.org> - 0.0.3-2
- Added AUTHORS NEWS and TODO to doc

* Sat Jul 02 2011 Elad Alfassa <elad@fedoraproject.org> - 0.0.3-1
- Initial build

