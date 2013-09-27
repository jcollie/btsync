Name:           btsync
Version:        1.1.82
Release:        1%{?dist}
Summary:        BitTorrent Sync

License:        Proprietary
URL:            http://labs.bittorrent.com/experiments/sync.html
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
* Fri Sep 27 2013 Jeffrey Ollie <jeff@ocjtech.us> - 1.1.82-1
- First version

