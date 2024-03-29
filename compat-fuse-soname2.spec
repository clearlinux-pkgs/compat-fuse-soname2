#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD113FCAC3C4E599F (Nikolaus@rath.org)
#
Name     : compat-fuse-soname2
Version  : 2.9.9
Release  : 13
URL      : https://github.com/libfuse/libfuse/releases/download/fuse-2.9.9/fuse-2.9.9.tar.gz
Source0  : https://github.com/libfuse/libfuse/releases/download/fuse-2.9.9/fuse-2.9.9.tar.gz
Source1  : https://github.com/libfuse/libfuse/releases/download/fuse-2.9.9/fuse-2.9.9.tar.gz.asc
Summary  : Filesystem in Userspace
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: compat-fuse-soname2-lib = %{version}-%{release}
Requires: compat-fuse-soname2-license = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
# Suppress generation of debuginfo
%global debug_package %{nil}
Patch1: 0001-Whitelist-UFSD-backport-to-2.9-branch-452.patch
Patch2: 0002-Correct-errno-comparison-571.patch
Patch3: 0003-util-ulockmgr_server.c-conditionally-define-closefro.patch

%description
libfuse
=======
Warning: unresolved security issue
----------------------------------

%package dev
Summary: dev components for the compat-fuse-soname2 package.
Group: Development
Requires: compat-fuse-soname2-lib = %{version}-%{release}
Provides: compat-fuse-soname2-devel = %{version}-%{release}
Requires: compat-fuse-soname2 = %{version}-%{release}

%description dev
dev components for the compat-fuse-soname2 package.


%package dev32
Summary: dev32 components for the compat-fuse-soname2 package.
Group: Default
Requires: compat-fuse-soname2-lib32 = %{version}-%{release}
Requires: compat-fuse-soname2-dev = %{version}-%{release}

%description dev32
dev32 components for the compat-fuse-soname2 package.


%package lib
Summary: lib components for the compat-fuse-soname2 package.
Group: Libraries
Requires: compat-fuse-soname2-license = %{version}-%{release}

%description lib
lib components for the compat-fuse-soname2 package.


%package lib32
Summary: lib32 components for the compat-fuse-soname2 package.
Group: Default
Requires: compat-fuse-soname2-license = %{version}-%{release}

%description lib32
lib32 components for the compat-fuse-soname2 package.


%package license
Summary: license components for the compat-fuse-soname2 package.
Group: Default

%description license
license components for the compat-fuse-soname2 package.


%prep
%setup -q -n fuse-2.9.9
cd %{_builddir}/fuse-2.9.9
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a fuse-2.9.9 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628528712
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1628528712
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-fuse-soname2
cp %{_builddir}/fuse-2.9.9/COPYING %{buildroot}/usr/share/package-licenses/compat-fuse-soname2/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/fuse-2.9.9/COPYING.LIB %{buildroot}/usr/share/package-licenses/compat-fuse-soname2/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/fusermount
rm -f %{buildroot}/usr/bin/mount.fuse
rm -f %{buildroot}/usr/bin/ulockmgr_server
rm -f %{buildroot}/usr/include/ulockmgr.h
rm -f %{buildroot}/usr/share/man/man1/fusermount.1
rm -f %{buildroot}/usr/share/man/man1/ulockmgr_server.1
rm -f %{buildroot}/usr/share/man/man8/mount.fuse.8

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/fuse.h
/usr/include/fuse/cuse_lowlevel.h
/usr/include/fuse/fuse.h
/usr/include/fuse/fuse_common.h
/usr/include/fuse/fuse_common_compat.h
/usr/include/fuse/fuse_compat.h
/usr/include/fuse/fuse_lowlevel.h
/usr/include/fuse/fuse_lowlevel_compat.h
/usr/include/fuse/fuse_opt.h
/usr/lib64/libfuse.so
/usr/lib64/libulockmgr.so
/usr/lib64/pkgconfig/fuse.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libfuse.so
/usr/lib32/libulockmgr.so
/usr/lib32/pkgconfig/32fuse.pc
/usr/lib32/pkgconfig/fuse.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfuse.so.2
/usr/lib64/libfuse.so.2.9.9
/usr/lib64/libulockmgr.so.1
/usr/lib64/libulockmgr.so.1.0.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libfuse.so.2
/usr/lib32/libfuse.so.2.9.9
/usr/lib32/libulockmgr.so.1
/usr/lib32/libulockmgr.so.1.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-fuse-soname2/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/compat-fuse-soname2/4cc77b90af91e615a64ae04893fdffa7939db84c
