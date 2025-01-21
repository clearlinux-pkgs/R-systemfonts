#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-systemfonts
Version  : 1.2.1
Release  : 42
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/systemfonts_1.2.1.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/systemfonts_1.2.1.tar.gz
Summary  : System Native Font Finding
Group    : Development/Tools
License  : MIT
Requires: R-systemfonts-lib = %{version}-%{release}
Requires: R-cpp11
Requires: R-jsonlite
Requires: R-lifecycle
BuildRequires : R-cpp11
BuildRequires : R-jsonlite
BuildRequires : R-lifecycle
BuildRequires : buildreq-R
BuildRequires : fontconfig-dev
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
handling varies between systems it is difficult to correctly locate
    installed fonts across different operating systems. The 'systemfonts'
    package provides bindings to the native libraries on Windows, macOS
    and Linux for finding font files that can then be used further by e.g.
    graphic devices. The main use is intended to be from compiled code but
    'systemfonts' also provides access from R.

%package dev
Summary: dev components for the R-systemfonts package.
Group: Development
Requires: R-systemfonts-lib = %{version}-%{release}
Provides: R-systemfonts-devel = %{version}-%{release}
Requires: R-systemfonts = %{version}-%{release}

%description dev
dev components for the R-systemfonts package.


%package lib
Summary: lib components for the R-systemfonts package.
Group: Libraries

%description lib
lib components for the R-systemfonts package.


%prep
%setup -q -n systemfonts
pushd ..
cp -a systemfonts buildavx2
popd
pushd ..
cp -a systemfonts buildavx512
popd
pushd ..
cp -a systemfonts buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737473019

%install
export SOURCE_DATE_EPOCH=1737473019
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/systemfonts/DESCRIPTION
/usr/lib64/R/library/systemfonts/INDEX
/usr/lib64/R/library/systemfonts/LICENSE
/usr/lib64/R/library/systemfonts/Meta/Rd.rds
/usr/lib64/R/library/systemfonts/Meta/features.rds
/usr/lib64/R/library/systemfonts/Meta/hsearch.rds
/usr/lib64/R/library/systemfonts/Meta/links.rds
/usr/lib64/R/library/systemfonts/Meta/nsInfo.rds
/usr/lib64/R/library/systemfonts/Meta/package.rds
/usr/lib64/R/library/systemfonts/Meta/vignette.rds
/usr/lib64/R/library/systemfonts/NAMESPACE
/usr/lib64/R/library/systemfonts/NEWS.md
/usr/lib64/R/library/systemfonts/R/sysdata.rdb
/usr/lib64/R/library/systemfonts/R/sysdata.rdx
/usr/lib64/R/library/systemfonts/R/systemfonts
/usr/lib64/R/library/systemfonts/R/systemfonts.rdb
/usr/lib64/R/library/systemfonts/R/systemfonts.rdx
/usr/lib64/R/library/systemfonts/doc/c_interface.R
/usr/lib64/R/library/systemfonts/doc/c_interface.Rmd
/usr/lib64/R/library/systemfonts/doc/c_interface.html
/usr/lib64/R/library/systemfonts/doc/index.html
/usr/lib64/R/library/systemfonts/help/AnIndex
/usr/lib64/R/library/systemfonts/help/aliases.rds
/usr/lib64/R/library/systemfonts/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/systemfonts/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/systemfonts/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/systemfonts/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/systemfonts/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/systemfonts/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/systemfonts/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/systemfonts/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/systemfonts/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/systemfonts/help/paths.rds
/usr/lib64/R/library/systemfonts/help/systemfonts.rdb
/usr/lib64/R/library/systemfonts/help/systemfonts.rdx
/usr/lib64/R/library/systemfonts/html/00Index.html
/usr/lib64/R/library/systemfonts/html/R.css
/usr/lib64/R/library/systemfonts/tests/testthat.R
/usr/lib64/R/library/systemfonts/tests/testthat/test-match_font.R
/usr/lib64/R/library/systemfonts/tests/testthat/test-system_fonts.R
/usr/lib64/R/library/systemfonts/unfont.ttf

%files dev
%defattr(-,root,root,-)
/usr/lib64/R/library/systemfonts/include/systemfonts-ft.h
/usr/lib64/R/library/systemfonts/include/systemfonts.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/systemfonts/libs/systemfonts.so
/V4/usr/lib64/R/library/systemfonts/libs/systemfonts.so
/VA/usr/lib64/R/library/systemfonts/libs/systemfonts.so
/usr/lib64/R/library/systemfonts/libs/systemfonts.so
