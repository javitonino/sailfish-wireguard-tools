Name:       wireguard-tools
Summary:    Required tools for WireGuard, such as wg(8) and wg-quick(8)
Version:    1.0.20210914
Release:    1
License:    MIT
URL:        https://www.wireguard.com

%description

%build
cd %{name}/src
make clean
make

%install
cd %{name}/src
make install DESTDIR=%{buildroot} WITH_WGQUICK=no

%files
%defattr(-,root,root,-)
%{_bindir}/wg
%{_datadir}/bash-completion/completions/wg
%{_datadir}/man/man8/wg.8.gz
