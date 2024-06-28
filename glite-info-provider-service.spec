Name:          glite-info-provider-service
Version:       1.14.2
Release:       1%{?dist}
Summary:       The GLUE service information provider
Group:         Development/Libraries
License:       ASL 2.0
URL:           https://github.com/EGI-Federation/glite-info-provider-service
Source:        %{name}-%{version}.tar.gz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildRequires: rsync
BuildRequires: make
Requires: lsb_release
%if 0%{?rhel} >= 9
Requires: hostname
Requires: initscripts-service
%endif

%description
The GLUE service information provider

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/glite/info/service
%{_bindir}/glite-info-glue2-service
%{_bindir}/glite-info-glue2-endpoint
%{_bindir}/glite-info-glue2-simple
%{_bindir}/glite-info-glue2-multi
%{_bindir}/glite-info-glue2-voms
%{_bindir}/glite-info-service
%{_bindir}/glite-info-service-glue2
%{_bindir}/glite-info-service-glue2-beta
%{_bindir}/glite-info-service-test
%{_bindir}/glite-info-service-amga
%{_bindir}/glite-info-service-argus
%{_bindir}/glite-info-service-bdii
%{_bindir}/glite-info-service-vobox
%{_bindir}/glite-info-service-voms
%{_bindir}/glite-info-service-voms-wrapper
%{_bindir}/glite-info-service-voms-admin
%{_bindir}/glite-info-service-myproxy
%{_bindir}/glite-info-service-frontier
%{_bindir}/glite-info-service-squid
%{_bindir}/glite-info-service-cream
%{_bindir}/glite-info-service-dcache
%{_bindir}/glite-info-service-dpm
%{_bindir}/glite-info-service-rtepublisher
%{_bindir}/glite-info-service-status
%{_sysconfdir}/glite/info/service/glite-info-glue2-amga.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-argus-pap.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-argus-pep.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-argus-pdp.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-bdii-site.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-bdii-top.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-rtepublisher.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-vobox.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-voms.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-voms-admin.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-frontier.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-squid.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-myproxy.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-cemon.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-test.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-amga.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-argus-pap.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-argus-pep.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-argus-pdp.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-bdii.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-bdii-site.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-bdii-top.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-gsirfio.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-frontier.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-squid.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-cream.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-cemon.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-myproxy.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-vobox.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-voms.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-voms-admin.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-srm-dcache-v1.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-srm-dcache-v2.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-srm-dpm-v1.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-srm-dpm-v2.conf.template
%{_sysconfdir}/glite/info/service/glite-info-service-rtepublisher.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-test.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-test2.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-service-test.conf.template
%{_sysconfdir}/glite/info/service/glite-info-glue2-service-argus.conf.template
%{_sysconfdir}/glite/info/service/glue1.test.ldif
%{_sysconfdir}/glite/info/service/glue1.test.ldif.prev
%{_sysconfdir}/glite/info/service/glue2.test.ldif
%{_sysconfdir}/glite/info/service/glue2.multi.test.ldif
%{_sysconfdir}/glite/info/service/glue2.test.ldif.prev
%doc %{_docdir}/%{name}-%{version}/README.md
%doc %{_docdir}/%{name}-%{version}/README
%doc %{_docdir}/%{name}-%{version}/README-GLUE2
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license %{_datadir}/licenses/%{name}-%{version}/COPYRIGHT
%license %{_datadir}/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* Tue Apr 28 2024 Baptiste Grenier <baptiste.grenier@egi.eu> - 1.14.2-1
- Add missing dependency on lsb_release. (#11) (Baptiste Grenier)

* Tue Apr 28 2024 Baptiste Grenier <baptiste.grenier@egi.eu> - 1.14.1-1
- Add missing dependencies for EL9. (#7) (Baptiste Grenier)

* Tue Apr 11 2023 Baptiste Grenier <baptiste.grenier@egi.eu> - 1.14.0-1
- Drop some deprecated providers (gatekeeper, gridice, lbserver, wmproxy). (#3) (Baptiste Grenier)
- Lint code. (#3) (Enol Fernandez) (Baptiste Grenier)
- Add Community files and GitHub actions. (#2) (Baptiste Grenier)
- Build and release using CentOS 7, AlmaLinux 8 and 9. (#2) (Baptiste Grenier)

* Mon Aug 04 2014 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.13.4-1
- Patch for the RTEPublisher start time, GGUS #107264
- Publish the schema version as OtherInfo for the site and top BDII

* Tue Apr 15 2014 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.13.3-1
- Change the RPM name for the tag publisher version, bug #102207

* Thu Aug 01 2013 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.13.1-1
- Die if hostname -f returns a null string, voms providers, bug #101562

* Thu Aug 01 2013 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.13.0-1
- Allow longer strings in GlueServiceData, bug #102168
- Die if hostname -f returns a null string, bug #101562
- Allow for an rpm name change in the WMS templates, bug #100872
- Change the published URL for the Argus PDP templates, bug #100822
- Allow for a move in the pidfile location in the LB templates, bug #100126

* Mon Oct 22 2012 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.12.0-1
- Protect against non-ASCII characters in strings, bug #98374

* Sat Sep 29 2012 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.11.0-2
- Update the site and top BDII configuration, bug #97396
- Publish the OS name and version as OtherInfo items in the Endpoint, bug #97816

* Tue Aug 28 2012 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.10.0-1
- GLUE 2 updates: Export site name, publish EGI profile compliance, publish HostDN
- See bugs #96503, #96787

* Wed Jul 18 2012 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.9.0-1
- GLUE 2 updates: new README, change VOMS ServiceType, fix MyProxy bug
- See bugs #80792, #95869, #95872

* Thu Dec 08 2011 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.8.1-2
- Fix the spec file

* Thu Dec 08 2011 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.8.1-1
- Update config for MyProxy, voms-admin and AMGA, see bugs #86398, #86524 and task #21920

* Wed Nov 23 2011 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.8.0-1
- New Config for Argus, see bug 86646

* Mon Nov 14 2011 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.8.0-1
- New provider glite-info-glue2-multi, see bug 86646

* Thu Jul 21 2011 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.7.0-1
- Various updates for voms, CREAM and WMS, see bugs 80789, 81840, 82645, 83105, 83313, 84373

* Thu May 05 2011 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.6.3-1
- ... and fix a missing tab in the make file ...

* Thu May 05 2011 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.6.2-1
- Add the ldif from the test config to the rpm

* Thu May 05 2011 Stephen Burke <stephen.burke@stfc.ac.uk> - 1.6.1-1
- Various minor bug fixes, see patch #4534 for details

* Fri Mar 25 2011 Laurence Field <laurence.field@cern.ch> - 1.5.2-1
- Changed the value of MYPROXY_CONF

* Tue Mar 08 2011 Laurence Field <laurence.field@cern.ch> - 1.5.0-1
- Now FHS Compliant

* Tue Apr 06 2010 Laurence Field <laurence.field@cern.ch> - 1.3.3-1
- Improved packaging
