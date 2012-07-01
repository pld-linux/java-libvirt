#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
#
%include	/usr/lib/rpm/macros.java
Summary:	Java binding to the libvirt library
Summary(pl.UTF-8):	Wiązanie Javy do biblioteki libvirt
Name:		java-libvirt
Version:	0.4.7
Release:	1
License:	LGPL v2.1
Group:		Libraries/Java
Source0:	ftp://libvirt.org/libvirt/java/libvirt-java-%{version}.tar.gz
# Source0-md5:	47d2558a1d2783fb88595a081889e01a
URL:		http://libvirt.org/
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	libvirt-devel >= 0.8.2
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java binding to the libvirt library.

%description -l pl.UTF-8
Wiązanie Javy do biblioteki libvirt.

%package javadoc
Summary:	Documentation for java-libvirt binding
Summary(pl.UTF-8):	Dokumentacja do wiązań java-libvirt
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for java-libvirt binding.

%description javadoc -l pl.UTF-8
Dokumentacja do wiązań java-libvirt.

%prep
%setup -q -n libvirt-java-%{version}

%build
export JAVA_HOME="%{java_home}"

%ant build %{?with_javadoc:docs}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -p target/libvirt-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s libvirt-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/libvirt.jar

%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/libvirt-%{version}
cp -a target/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/libvirt-%{version}
ln -s libvirt-%{version} $RPM_BUILD_ROOT%{_javadocdir}/libvirt # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs libvirt-%{version} %{_javadocdir}/libvirt

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_javadir}/libvirt-%{version}.jar
%{_javadir}/libvirt.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/libvirt-%{version}
%ghost %{_javadocdir}/libvirt
%endif
