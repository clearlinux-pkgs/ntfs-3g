#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ntfs-3g
Version  : 3g.progs.2022.10.3
Release  : 20
URL      : https://tuxera.com/opensource/ntfs-3g_ntfsprogs-2022.10.3.tgz
Source0  : https://tuxera.com/opensource/ntfs-3g_ntfsprogs-2022.10.3.tgz
Summary  : NTFS-3G Read/Write Driver Library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: ntfs-3g-bin = %{version}-%{release}
Requires: ntfs-3g-lib = %{version}-%{release}
Requires: ntfs-3g-license = %{version}-%{release}
Requires: ntfs-3g-man = %{version}-%{release}
BuildRequires : pkgconfig(fuse)
BuildRequires : util-linux-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
INTRODUCTION
============
The NTFS-3G driver is an open source, freely available read/write NTFS driver
for Linux, FreeBSD, macOS, NetBSD, OpenIndiana, QNX and Haiku. It provides
safe and fast handling of the Windows XP, Windows Server 2003, Windows 2000,
Windows Vista, Windows Server 2008, Windows 7, Windows 8, Windows Server 2012,
Windows Server 2016, Windows 10 and Windows Server 2019 NTFS file systems.

%package bin
Summary: bin components for the ntfs-3g package.
Group: Binaries
Requires: ntfs-3g-license = %{version}-%{release}

%description bin
bin components for the ntfs-3g package.


%package dev
Summary: dev components for the ntfs-3g package.
Group: Development
Requires: ntfs-3g-lib = %{version}-%{release}
Requires: ntfs-3g-bin = %{version}-%{release}
Provides: ntfs-3g-devel = %{version}-%{release}
Requires: ntfs-3g = %{version}-%{release}

%description dev
dev components for the ntfs-3g package.


%package doc
Summary: doc components for the ntfs-3g package.
Group: Documentation
Requires: ntfs-3g-man = %{version}-%{release}

%description doc
doc components for the ntfs-3g package.


%package lib
Summary: lib components for the ntfs-3g package.
Group: Libraries
Requires: ntfs-3g-license = %{version}-%{release}

%description lib
lib components for the ntfs-3g package.


%package license
Summary: license components for the ntfs-3g package.
Group: Default

%description license
license components for the ntfs-3g package.


%package man
Summary: man components for the ntfs-3g package.
Group: Default

%description man
man components for the ntfs-3g package.


%prep
%setup -q -n ntfs-3g_ntfsprogs-2022.10.3
cd %{_builddir}/ntfs-3g_ntfsprogs-2022.10.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676336561
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static --disable-ldconfig
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1676336561
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ntfs-3g
cp %{_builddir}/ntfs-3g_ntfsprogs-2022.10.3/COPYING %{buildroot}/usr/share/package-licenses/ntfs-3g/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/ntfs-3g_ntfsprogs-2022.10.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/ntfs-3g/44f7289042b71631acac29b2f143330d2da2479e || :
%make_install
## install_append content
ln -sf /usr/bin/mount.ntfs-3g %{buildroot}/usr/bin/mount.ntfs
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lowntfs-3g
/usr/bin/mkfs.ntfs
/usr/bin/mkntfs
/usr/bin/mount.lowntfs-3g
/usr/bin/mount.ntfs
/usr/bin/mount.ntfs-3g
/usr/bin/ntfs-3g
/usr/bin/ntfs-3g.probe
/usr/bin/ntfscat
/usr/bin/ntfsclone
/usr/bin/ntfscluster
/usr/bin/ntfscmp
/usr/bin/ntfscp
/usr/bin/ntfsfix
/usr/bin/ntfsinfo
/usr/bin/ntfslabel
/usr/bin/ntfsls
/usr/bin/ntfsresize
/usr/bin/ntfsundelete

%files dev
%defattr(-,root,root,-)
/usr/include/ntfs-3g/acls.h
/usr/include/ntfs-3g/attrib.h
/usr/include/ntfs-3g/attrlist.h
/usr/include/ntfs-3g/bitmap.h
/usr/include/ntfs-3g/bootsect.h
/usr/include/ntfs-3g/cache.h
/usr/include/ntfs-3g/collate.h
/usr/include/ntfs-3g/compat.h
/usr/include/ntfs-3g/compress.h
/usr/include/ntfs-3g/debug.h
/usr/include/ntfs-3g/device.h
/usr/include/ntfs-3g/device_io.h
/usr/include/ntfs-3g/dir.h
/usr/include/ntfs-3g/ea.h
/usr/include/ntfs-3g/efs.h
/usr/include/ntfs-3g/endians.h
/usr/include/ntfs-3g/index.h
/usr/include/ntfs-3g/inode.h
/usr/include/ntfs-3g/ioctl.h
/usr/include/ntfs-3g/layout.h
/usr/include/ntfs-3g/lcnalloc.h
/usr/include/ntfs-3g/logfile.h
/usr/include/ntfs-3g/logging.h
/usr/include/ntfs-3g/mft.h
/usr/include/ntfs-3g/misc.h
/usr/include/ntfs-3g/mst.h
/usr/include/ntfs-3g/ntfstime.h
/usr/include/ntfs-3g/object_id.h
/usr/include/ntfs-3g/param.h
/usr/include/ntfs-3g/plugin.h
/usr/include/ntfs-3g/realpath.h
/usr/include/ntfs-3g/reparse.h
/usr/include/ntfs-3g/runlist.h
/usr/include/ntfs-3g/security.h
/usr/include/ntfs-3g/support.h
/usr/include/ntfs-3g/types.h
/usr/include/ntfs-3g/unistr.h
/usr/include/ntfs-3g/volume.h
/usr/include/ntfs-3g/xattrs.h
/usr/lib64/libntfs-3g.so
/usr/lib64/pkgconfig/libntfs-3g.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/ntfs\-3g/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libntfs-3g.so.89
/usr/lib64/libntfs-3g.so.89.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ntfs-3g/44f7289042b71631acac29b2f143330d2da2479e
/usr/share/package-licenses/ntfs-3g/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/mkfs.ntfs.8
/usr/share/man/man8/mkntfs.8
/usr/share/man/man8/mount.lowntfs-3g.8
/usr/share/man/man8/mount.ntfs-3g.8
/usr/share/man/man8/ntfs-3g.8
/usr/share/man/man8/ntfs-3g.probe.8
/usr/share/man/man8/ntfscat.8
/usr/share/man/man8/ntfsclone.8
/usr/share/man/man8/ntfscluster.8
/usr/share/man/man8/ntfscmp.8
/usr/share/man/man8/ntfscp.8
/usr/share/man/man8/ntfsdecrypt.8
/usr/share/man/man8/ntfsfallocate.8
/usr/share/man/man8/ntfsfix.8
/usr/share/man/man8/ntfsinfo.8
/usr/share/man/man8/ntfslabel.8
/usr/share/man/man8/ntfsls.8
/usr/share/man/man8/ntfsprogs.8
/usr/share/man/man8/ntfsrecover.8
/usr/share/man/man8/ntfsresize.8
/usr/share/man/man8/ntfssecaudit.8
/usr/share/man/man8/ntfstruncate.8
/usr/share/man/man8/ntfsundelete.8
/usr/share/man/man8/ntfsusermap.8
/usr/share/man/man8/ntfswipe.8
