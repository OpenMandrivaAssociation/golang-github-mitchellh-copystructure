# http://github.com/mitchellh/copystructure

%global goipath         github.com/mitchellh/copystructure
%global commit          cdac8253d00f2ecf0a0b19fbff173a9a72de4f82


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Go library for deep copying values in Go
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/mitchellh/reflectwalk)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.gitcdac825
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitcdac825
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitcdac825
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitcdac825
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jan 05 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.gitcdac825
- First package for Fedora
  resolves: #1410401
