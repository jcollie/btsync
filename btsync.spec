%global __filter_GLIBC_PRIVATE 1

Name:           btsync
Version:        1.1.82
Release:        3%{?dist}
Summary:        BitTorrent Sync

License:        Proprietary
URL:            http://labs.bittorrent.com/experiments/sync.html

# Sometimes you may need to use the following to get the latest:
# wget -O btsync_x64-%{version}.tar.gz http://download-lb.utorrent.com/endpoint/btsync/os/linux-x64/track/stable

Source0:        http://syncapp.bittorrent.com/%{version}/btsync_x64-%{version}.tar.gz
Source1:        btsync@.service
Source2:        btsync-pre

BuildRequires:  systemd

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
BitTorrent Sync

%prep
%setup -c

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 btsync %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{S:1} %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_libexecdir}
install -p -m 0755 %{S:2} %{buildroot}%{_libexecdir}

%post
%systemd_post btsync@.service

%preun
%systemd_preun btsync@.service

%postun
%systemd_postun_with_restart btsync@.service 

%files
%doc LICENSE.TXT
%{_bindir}/btsync
%{_unitdir}/btsync@.service
%{_libexecdir}/btsync-pre

%changelog
* Fri Sep 27 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.1.82-3
- Fix logging in btsync-pre

* Fri Sep 27 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.1.82-2
- Filter out GLIBC_PRIVATE requirements
- Add some comments on how to obtain latest version

* Fri Sep 27 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.1.82-1
- First version

