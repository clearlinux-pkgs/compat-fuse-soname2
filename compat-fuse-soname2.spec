#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-fuse-soname2
Version  : 2.9.4
Release  : 5
URL      : http://downloads.sourceforge.net/fuse/fuse-2.9.4.tar.gz
Source0  : http://downloads.sourceforge.net/fuse/fuse-2.9.4.tar.gz
Summary  : Filesystem in Userspace
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: compat-fuse-soname2-bin
Requires: compat-fuse-soname2-lib
Requires: compat-fuse-soname2-doc

%description
General Information
===================
FUSE (Filesystem in Userspace) is a simple interface for userspace
programs to export a virtual filesystem to the Linux kernel.  FUSE
also aims to provide a secure method for non privileged users to
create and mount their own filesystem implementations.

%package bin
Summary: bin components for the compat-fuse-soname2 package.
Group: Binaries

%description bin
bin components for the compat-fuse-soname2 package.


%package dev
Summary: dev components for the compat-fuse-soname2 package.
Group: Development
Requires: compat-fuse-soname2-lib
Requires: compat-fuse-soname2-bin
Provides: compat-fuse-soname2-devel

%description dev
dev components for the compat-fuse-soname2 package.


%package doc
Summary: doc components for the compat-fuse-soname2 package.
Group: Documentation

%description doc
doc components for the compat-fuse-soname2 package.


%package lib
Summary: lib components for the compat-fuse-soname2 package.
Group: Libraries

%description lib
lib components for the compat-fuse-soname2 package.


%prep
%setup -q -n fuse-2.9.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505676444
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1505676444
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/fusermount
%exclude /usr/bin/mount.fuse
%exclude /usr/bin/ulockmgr_server

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/ulockmgr.h
/usr/include/*.h
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

%files doc
%defattr(-,root,root,-)
%exclude /usr/share/man/man1/fusermount.1
%exclude /usr/share/man/man1/ulockmgr_server.1
%exclude /usr/share/man/man8/mount.fuse.8

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfuse.so.2
/usr/lib64/libfuse.so.2.9.4
/usr/lib64/libulockmgr.so.1
/usr/lib64/libulockmgr.so.1.0.1
