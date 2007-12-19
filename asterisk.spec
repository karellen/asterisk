%define with_apidoc %{?_with_apidoc: 1} %{!?_with_apidoc: 0}

Summary: The Open Source PBX
Name: asterisk
Version: 1.4.16
Release: 2%{?dist}
License: GPLv2
Group: Applications/Internet
URL: http://www.asterisk.org/

# will file a bug once the asterisk bugzilla component shows up
ExcludeArch: ppc64

# The asterisk tarball contains some items that we don't want in there,
# so start with the original tarball from here:
# http://downloads.digium.com/pub/telephony/asterisk/releases/asterisk-%{version}.tar.gz
# Then run the included script file to build the stripped tarball:
#
# sh asterisk-strip.sh %{version}
#
# MD5 Sums
# ========
# 2bc92ed77ba1dede35da744cca046ac0  asterisk-1.4.16.tar.gz
# 76a17563c4f6e3cc7b4457377db0b85b  asterisk-1.4.16-stripped.tar.gz
#
# SHA1 Sums
# =========
# 996ef122e2cd11a348c6679133019b664a8535ee  asterisk-1.4.16.tar.gz
# e4ec1416016dc757ad8a6aad3eeefc49b4d0e76c  asterisk-1.4.16-stripped.tar.gz

Source0: asterisk-%{version}-stripped.tar.gz
Source1: asterisk-logrotate
Source2: menuselect.makedeps
Source3: menuselect.makeopts
Source4: asterisk-strip.sh

Patch1:  asterisk-1.4.16-initscripts.patch
Patch2:  asterisk-1.4.16-system-imap.patch
Patch3:  asterisk-1.4.16-alternate-voicemail.patch
Patch4:  asterisk-1.4.16-spandspfax.patch
Patch5:  asterisk-1.4.16-appconference.patch
Patch6:  asterisk-1.4.16-alternate-extensions.patch
Patch7:  asterisk-1.4.16-optimization.patch
Patch8:  asterisk-1.4.16-libcap.patch
Patch9:  asterisk-1.4.16-chanmobile.patch
Patch10: asterisk-1.4.16-autoconf.patch
Patch11: asterisk-1.4.16-1.4.16.1-update.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

# core build requirements
BuildRequires: openssl-devel
BuildRequires: newt-devel
%if 0%{?fedora} <= 8
BuildRequires: libtermcap-devel
%endif
BuildRequires: ncurses-devel
BuildRequires: libcap-devel
BuildRequires: gtk2-devel

%if %{with_apidoc}
# for building docs
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: graphviz-gd
%endif

# for codec_speex and app_conference
BuildRequires: speex-devel >= 1.2

# for format_ogg_vorbis
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel

# codec_gsm
BuildRequires: gsm-devel

Requires(pre): %{_sbindir}/useradd
Requires(pre): %{_sbindir}/groupadd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description
Asterisk is a complete PBX in software. It runs on Linux and provides
all of the features you would expect from a PBX and more. Asterisk
does voice over IP in three protocols, and can interoperate with
almost all standards-based telephony equipment using relatively
inexpensive hardware.

%package alsa
Summary: Modules for Asterisk that use Alsa sound drivers
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: alsa-lib-devel

%description alsa
Modules for Asterisk that use Alsa sound drivers.

%if %{with_apidoc}
%package apidoc
Summary: API documentation for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description apidoc
API documentation for Asterisk.
%endif

%package conference
Summary: Audio/video conferencing application for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: speex-devel

%description conference
Audio/video conferencing application for Asterisk.

%package curl
Summary: Modules for Asterisk that use cURL
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: curl-devel

%description curl
Modules for Asterisk that use cURL.

%package devel
Summary: Development files for Asterisk
Group: Development/Libraries
Requires: asterisk = %{version}-%{release}

%description devel
Development files for Asterisk.

%package fax
Summary: FAX applications for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: spandsp-devel

%description fax
FAX applications for Asterisk

%package festival
Summary: Festival application for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: festival

%description festival
Application for the Asterisk PBX that uses Festival to convert text to speech.

%package firmware
Summary: Firmware for the Digium S101I (IAXy)
Group: Applications/Internet
License: Redistributable, no modification permitted
Requires: asterisk = %{version}-%{release}
Requires: festival

%description firmware
Firmware for the Digium S101I (IAXy).

%package jabber
Summary: Jabber/XMPP resources for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: iksemel-devel

%description jabber
Jabber/XMPP resources for Asterisk.

%package misdn
Summary: mISDN channel for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires(pre): %{_sbindir}/usermod
BuildRequires: mISDN-devel

%description misdn
mISDN channel for Asterisk.

%package mobile
Summary: Asterisk channel driver for bluetooth phones and headsets
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: bluez-libs-devel

%description mobile
Asterisk channel driver to allow Bluetooth cell/mobile phones to be
used as FXO devices, and headsets as FXS devices.

%package odbc
Summary: Applications for Asterisk that use ODBC (except voicemail)
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: libtool-ltdl-devel
BuildRequires: unixODBC-devel

%description odbc
Applications for Asterisk that use ODBC (except voicemail)

%package oss
Summary: Modules for Asterisk that use OSS sound drivers
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description oss
Modules for Asterisk that use OSS sound drivers.

%package postgresql
Summary: Applications for Asterisk that use PostgreSQL
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: postgresql-devel

%description postgresql
Applications for Asterisk that use PostgreSQL.

%package radius
Summary: Applications for Asterisk that use RADIUS
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: radiusclient-ng-devel

%description radius
Applications for Asterisk that use RADIUS.

%package skinny
Summary: Modules for Asterisk that support the SCCP/Skinny protocol
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description skinny
Modules for Asterisk that support the SCCP/Skinny protocol.

%package snmp
Summary: Module that enables SNMP monitoring of Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: net-snmp-devel
BuildRequires: lm_sensors-devel

%description snmp
Module that enables SNMP monitoring of Asterisk.

%package tds
Summary: Modules for Asterisk that use FreeTDS
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: freetds-devel

%description tds
Modules for Asterisk that use FreeTDS.

%package voicemail
Summary: Common Voicemail Modules for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail-implementation = %{version}-%{release}
Requires: /usr/bin/sox
Requires: /usr/sbin/sendmail

%description voicemail
Common Voicemail Modules for Asterisk.

%package voicemail-imap
Summary: Store voicemail on an IMAP server
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail = %{version}-%{release}
Provides: asterisk-voicemail-implementation = %{version}-%{release}
BuildRequires: uw-imap-devel

%description voicemail-imap
Voicemail implementation for Asterisk that stores voicemail on an IMAP
server.

%package voicemail-odbc
Summary: Store voicemail in a database using ODBC
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail = %{version}-%{release}
Provides: asterisk-voicemail-implementation = %{version}-%{release}

%description voicemail-odbc
Voicemail implementation for Asterisk that uses ODBC to store
voicemail in a database.

%package voicemail-plain
Summary: Store voicemail on the local filesystem
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: asterisk-voicemail = %{version}-%{release}
Provides: asterisk-voicemail-implementation = %{version}-%{release}

%description voicemail-plain
Voicemail implementation for Asterisk that stores voicemail on the
local filesystem.

%package zaptel
Summary: Modules for Asterisk that use Zaptel
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: zaptel >= 1.4.0
Requires(pre): %{_sbindir}/usermod
BuildRequires: zaptel-devel >= 1.4.0
BuildRequires: libpri-devel >= 1.4.0

%description zaptel
Modules for Asterisk that use Zaptel.

%prep
%setup0 -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

cp %{SOURCE2} menuselect.makedeps
cp %{SOURCE3} menuselect.makeopts

# Fixup makefile so sound archives aren't downloaded/installed
%{__perl} -pi -e 's/^all:.*$/all:/' sounds/Makefile
%{__perl} -pi -e 's/^install:.*$/install:/' sounds/Makefile

# convert comments in one file to UTF-8
mv main/fskmodem.c main/fskmodem.c.old
iconv -f iso-8859-1 -t utf-8 -o main/fskmodem.c main/fskmodem.c.old
touch -r main/fskmodem.c.old main/fskmodem.c

%build

pushd menuselect/mxml
%configure
popd

pushd menuselect
%configure
popd 

pushd main/editline
%configure
popd

%configure --with-imap=system --with-gsm=/usr

ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_plain.so
mv apps/app_directory.so apps/app_directory_plain.so

%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=IMAP_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_imap.so
mv apps/app_directory.so apps/app_directory_imap.so

%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=ODBC_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_odbc.so
mv apps/app_directory.so apps/app_directory_odbc.so

# so that these modules don't get built again during the install phase
touch apps/app_voicemail.o apps/app_directory.o
touch apps/app_voicemail.so apps/app_directory.so

%if %{with_apidoc}
ASTCFLAGS="%{optflags}" make progdocs DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk NOISY_BUILD=1

# fix dates so that we don't get multilib conflicts
find doc/api/html -type f -print0 | xargs --null touch -r ChangeLog
%endif

%install
rm -rf %{buildroot}

ASTCFLAGS="%{optflags}" make install DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk
ASTCFLAGS="%{optflags}" make samples DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk

install -D -p -m 0755 contrib/init.d/rc.redhat.asterisk %{buildroot}%{_initrddir}/asterisk
install -D -p -m 0644 contrib/sysconfig/asterisk %{buildroot}%{_sysconfdir}/sysconfig/asterisk
install -D -p -m 0644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/asterisk
install -D -p -m 0644 doc/asterisk-mib.txt %{buildroot}%{_datadir}/snmp/mibs/ASTERISK-MIB.txt
install -D -p -m 0644 doc/digium-mib.txt %{buildroot}%{_datadir}/snmp/mibs/DIGIUM-MIB.txt

rm %{buildroot}%{_libdir}/asterisk/modules/app_directory.so
rm %{buildroot}%{_libdir}/asterisk/modules/app_voicemail.so
install -D -p -m 0755 apps/app_directory_imap.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_voicemail_imap.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_directory_odbc.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_voicemail_odbc.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_directory_plain.so %{buildroot}%{_libdir}/asterisk/modules/
install -D -p -m 0755 apps/app_voicemail_plain.so %{buildroot}%{_libdir}/asterisk/modules/

# create some directories that need to be packaged
mkdir -p %{buildroot}%{_datadir}/asterisk/moh/
mkdir -p %{buildroot}%{_datadir}/asterisk/sounds/
mkdir -p %{buildroot}%{_localstatedir}/lib/asterisk
mkdir -p %{buildroot}%{_localstatedir}/log/asterisk/cdr-custom/
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/outgoing/

# We're not going to package any of the sample AGI scripts
rm -f %{buildroot}%{_datadir}/asterisk/agi-bin/*

# Don't package the sample voicemail user
rm -rf %{buildroot}%{_localstatedir}/spool/asterisk/voicemail/default

%if %{with_apidoc}
find doc/api/html -name \*.map -size 0 -delete
%endif

%clean
rm -rf %{buildroot}

%pre
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d /var/lib/asterisk -M \
                               -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%post
# Register the asterisk service
/sbin/chkconfig --add asterisk

%preun
if [ "$1" -eq "0" ]; then
        /sbin/service asterisk stop > /dev/null 2>&1 || :
        /sbin/chkconfig --del asterisk
fi

%pre misdn
%{_sbindir}/usermod -a -G misdn asterisk

%pre zaptel
%{_sbindir}/usermod -a -G zaptel asterisk

%files
%defattr(-,root,root,-)
%doc README* *.txt ChangeLog BUGS CREDITS configs

%doc doc/00README.1st
%doc doc/ael.txt
%doc doc/ajam.txt
%doc doc/app-sms.txt
%doc doc/apps.txt
%doc doc/asterisk-conf.txt
%doc doc/asterisk.sgml
%doc doc/backtrace.txt
%doc doc/billing.txt
%doc doc/callfiles.txt
%doc doc/callingpres.txt
%doc doc/cdrdriver.txt
%doc doc/chaniax.txt
%doc doc/channels.txt
%doc doc/channelvariables.txt
%doc doc/cliprompt.txt
%doc doc/configuration.txt
%doc doc/cygwin.txt
%doc doc/dundi.txt
%doc doc/enum.txt
%doc doc/extconfig.txt
%doc doc/extensions.txt
%doc doc/externalivr.txt
%doc doc/h323.txt
%doc doc/hardware.txt
%doc doc/iax.txt
%doc doc/ices.txt
%doc doc/ip-tos.txt
%doc doc/jitterbuffer.txt
%doc doc/localchannel.txt
%doc doc/macroexclusive.txt
%doc doc/manager.txt
%doc doc/math.txt
%doc doc/model.txt
%doc doc/PEERING
%doc doc/privacy.txt
%doc doc/queuelog.txt
%doc doc/queues-with-callback-members.txt
%doc doc/realtime.txt
%doc doc/rtp-packetization.txt
%doc doc/security.txt
%doc doc/sla.pdf
%doc doc/sla.tex
%doc doc/smdi.txt
%doc doc/sms.txt
%doc doc/speechrec.txt
%doc doc/video.txt

%{_initrddir}/asterisk
%config(noreplace) %{_sysconfdir}/sysconfig/asterisk

%dir %{_libdir}/asterisk
%dir %{_libdir}/asterisk/modules

%{_libdir}/asterisk/modules/app_adsiprog.so
%{_libdir}/asterisk/modules/app_alarmreceiver.so
%{_libdir}/asterisk/modules/app_amd.so
%{_libdir}/asterisk/modules/app_authenticate.so
%{_libdir}/asterisk/modules/app_cdr.so
%{_libdir}/asterisk/modules/app_chanisavail.so
%{_libdir}/asterisk/modules/app_channelredirect.so
%{_libdir}/asterisk/modules/app_chanspy.so
%{_libdir}/asterisk/modules/app_controlplayback.so
%{_libdir}/asterisk/modules/app_db.so
%{_libdir}/asterisk/modules/app_dial.so
%{_libdir}/asterisk/modules/app_dictate.so
%{_libdir}/asterisk/modules/app_directed_pickup.so
%{_libdir}/asterisk/modules/app_disa.so
%{_libdir}/asterisk/modules/app_dumpchan.so
%{_libdir}/asterisk/modules/app_echo.so
%{_libdir}/asterisk/modules/app_exec.so
%{_libdir}/asterisk/modules/app_externalivr.so
%{_libdir}/asterisk/modules/app_followme.so
%{_libdir}/asterisk/modules/app_forkcdr.so
%{_libdir}/asterisk/modules/app_getcpeid.so
%{_libdir}/asterisk/modules/app_ices.so
%{_libdir}/asterisk/modules/app_image.so
%{_libdir}/asterisk/modules/app_lookupblacklist.so
%{_libdir}/asterisk/modules/app_lookupcidname.so
%{_libdir}/asterisk/modules/app_macro.so
%{_libdir}/asterisk/modules/app_milliwatt.so
%{_libdir}/asterisk/modules/app_mixmonitor.so
%{_libdir}/asterisk/modules/app_morsecode.so
%{_libdir}/asterisk/modules/app_nbscat.so
%{_libdir}/asterisk/modules/app_parkandannounce.so
%{_libdir}/asterisk/modules/app_playback.so
%{_libdir}/asterisk/modules/app_privacy.so
%{_libdir}/asterisk/modules/app_queue.so
%{_libdir}/asterisk/modules/app_random.so
%{_libdir}/asterisk/modules/app_readfile.so
%{_libdir}/asterisk/modules/app_read.so
%{_libdir}/asterisk/modules/app_realtime.so
%{_libdir}/asterisk/modules/app_record.so
%{_libdir}/asterisk/modules/app_sayunixtime.so
%{_libdir}/asterisk/modules/app_senddtmf.so
%{_libdir}/asterisk/modules/app_sendtext.so
%{_libdir}/asterisk/modules/app_setcallerid.so
%{_libdir}/asterisk/modules/app_setcdruserfield.so
%{_libdir}/asterisk/modules/app_settransfercapability.so
%{_libdir}/asterisk/modules/app_sms.so
%{_libdir}/asterisk/modules/app_softhangup.so
%{_libdir}/asterisk/modules/app_speech_utils.so
%{_libdir}/asterisk/modules/app_stack.so
%{_libdir}/asterisk/modules/app_system.so
%{_libdir}/asterisk/modules/app_talkdetect.so
%{_libdir}/asterisk/modules/app_test.so
%{_libdir}/asterisk/modules/app_transfer.so
%{_libdir}/asterisk/modules/app_url.so
%{_libdir}/asterisk/modules/app_userevent.so
%{_libdir}/asterisk/modules/app_verbose.so
%{_libdir}/asterisk/modules/app_waitforring.so
%{_libdir}/asterisk/modules/app_waitforsilence.so
%{_libdir}/asterisk/modules/app_while.so
%{_libdir}/asterisk/modules/app_zapateller.so
%{_libdir}/asterisk/modules/cdr_csv.so
%{_libdir}/asterisk/modules/cdr_custom.so
%{_libdir}/asterisk/modules/cdr_manager.so
%{_libdir}/asterisk/modules/chan_agent.so
%{_libdir}/asterisk/modules/chan_features.so
%{_libdir}/asterisk/modules/chan_iax2.so
%{_libdir}/asterisk/modules/chan_local.so
%{_libdir}/asterisk/modules/chan_mgcp.so
%{_libdir}/asterisk/modules/chan_phone.so
%{_libdir}/asterisk/modules/chan_sip.so
%{_libdir}/asterisk/modules/codec_adpcm.so
%{_libdir}/asterisk/modules/codec_alaw.so
%{_libdir}/asterisk/modules/codec_a_mu.so
%{_libdir}/asterisk/modules/codec_g726.so
%{_libdir}/asterisk/modules/codec_gsm.so
%{_libdir}/asterisk/modules/codec_lpc10.so
%{_libdir}/asterisk/modules/codec_speex.so
%{_libdir}/asterisk/modules/codec_ulaw.so
%{_libdir}/asterisk/modules/format_g723.so
%{_libdir}/asterisk/modules/format_g726.so
%{_libdir}/asterisk/modules/format_g729.so
%{_libdir}/asterisk/modules/format_gsm.so
%{_libdir}/asterisk/modules/format_h263.so
%{_libdir}/asterisk/modules/format_h264.so
%{_libdir}/asterisk/modules/format_jpeg.so
%{_libdir}/asterisk/modules/format_ogg_vorbis.so
%{_libdir}/asterisk/modules/format_pcm.so
%{_libdir}/asterisk/modules/format_sln.so
%{_libdir}/asterisk/modules/format_vox.so
%{_libdir}/asterisk/modules/format_wav_gsm.so
%{_libdir}/asterisk/modules/format_wav.so
%{_libdir}/asterisk/modules/func_base64.so
%{_libdir}/asterisk/modules/func_callerid.so
%{_libdir}/asterisk/modules/func_cdr.so
%{_libdir}/asterisk/modules/func_channel.so
%{_libdir}/asterisk/modules/func_curl.so
%{_libdir}/asterisk/modules/func_cut.so
%{_libdir}/asterisk/modules/func_db.so
%{_libdir}/asterisk/modules/func_enum.so
%{_libdir}/asterisk/modules/func_env.so
%{_libdir}/asterisk/modules/func_global.so
%{_libdir}/asterisk/modules/func_groupcount.so
%{_libdir}/asterisk/modules/func_language.so
%{_libdir}/asterisk/modules/func_logic.so
%{_libdir}/asterisk/modules/func_math.so
%{_libdir}/asterisk/modules/func_md5.so
%{_libdir}/asterisk/modules/func_moh.so
%{_libdir}/asterisk/modules/func_rand.so
%{_libdir}/asterisk/modules/func_realtime.so
%{_libdir}/asterisk/modules/func_sha1.so
%{_libdir}/asterisk/modules/func_strings.so
%{_libdir}/asterisk/modules/func_timeout.so
%{_libdir}/asterisk/modules/func_uri.so
%{_libdir}/asterisk/modules/pbx_ael.so
%{_libdir}/asterisk/modules/pbx_config.so
%{_libdir}/asterisk/modules/pbx_dundi.so
%{_libdir}/asterisk/modules/pbx_loopback.so
%{_libdir}/asterisk/modules/pbx_realtime.so
%{_libdir}/asterisk/modules/pbx_spool.so
%{_libdir}/asterisk/modules/res_adsi.so
%{_libdir}/asterisk/modules/res_agi.so
%{_libdir}/asterisk/modules/res_clioriginate.so
%{_libdir}/asterisk/modules/res_convert.so
%{_libdir}/asterisk/modules/res_crypto.so
%{_libdir}/asterisk/modules/res_features.so
%{_libdir}/asterisk/modules/res_indications.so
%{_libdir}/asterisk/modules/res_monitor.so
%{_libdir}/asterisk/modules/res_musiconhold.so
%{_libdir}/asterisk/modules/res_smdi.so
%{_libdir}/asterisk/modules/res_speech.so

%{_sbindir}/aelparse
%{_sbindir}/asterisk
%{_sbindir}/astgenkey
%{_sbindir}/astman
%{_sbindir}/autosupport
%{_sbindir}/muted
%{_sbindir}/rasterisk
%{_sbindir}/safe_asterisk
%{_sbindir}/smsq
%{_sbindir}/stereorize
%{_sbindir}/streamplayer

%{_mandir}/man8/asterisk.8*
%{_mandir}/man8/astgenkey.8*
%{_mandir}/man8/autosupport.8*
%{_mandir}/man8/safe_asterisk.8*

%dir %{_sysconfdir}/asterisk
%config(noreplace) %{_sysconfdir}/asterisk/adsi.conf
%config(noreplace) %{_sysconfdir}/asterisk/adtranvofr.conf
%config(noreplace) %{_sysconfdir}/asterisk/agents.conf
%config(noreplace) %{_sysconfdir}/asterisk/alarmreceiver.conf
%config(noreplace) %{_sysconfdir}/asterisk/amd.conf
%config(noreplace) %{_sysconfdir}/asterisk/asterisk.adsi
%config(noreplace) %{_sysconfdir}/asterisk/asterisk.conf
%config(noreplace) %{_sysconfdir}/asterisk/cdr.conf
%config(noreplace) %{_sysconfdir}/asterisk/cdr_custom.conf
%config(noreplace) %{_sysconfdir}/asterisk/cdr_manager.conf
%config(noreplace) %{_sysconfdir}/asterisk/codecs.conf
%config(noreplace) %{_sysconfdir}/asterisk/dnsmgr.conf
%config(noreplace) %{_sysconfdir}/asterisk/dundi.conf
%config(noreplace) %{_sysconfdir}/asterisk/enum.conf
%config(noreplace) %{_sysconfdir}/asterisk/extconfig.conf
%config(noreplace) %{_sysconfdir}/asterisk/extensions.ael
%config(noreplace) %{_sysconfdir}/asterisk/extensions.conf
%config(noreplace) %{_sysconfdir}/asterisk/features.conf
%config(noreplace) %{_sysconfdir}/asterisk/followme.conf
%config(noreplace) %{_sysconfdir}/asterisk/h323.conf
%config(noreplace) %{_sysconfdir}/asterisk/http.conf
%config(noreplace) %{_sysconfdir}/asterisk/iax.conf
%config(noreplace) %{_sysconfdir}/asterisk/iaxprov.conf
%config(noreplace) %{_sysconfdir}/asterisk/indications.conf
%config(noreplace) %{_sysconfdir}/asterisk/logger.conf
%config(noreplace) %{_sysconfdir}/asterisk/manager.conf
%config(noreplace) %{_sysconfdir}/asterisk/mgcp.conf
%config(noreplace) %{_sysconfdir}/asterisk/modules.conf
%config(noreplace) %{_sysconfdir}/asterisk/musiconhold.conf
%config(noreplace) %{_sysconfdir}/asterisk/muted.conf
%config(noreplace) %{_sysconfdir}/asterisk/osp.conf
%config(noreplace) %{_sysconfdir}/asterisk/phone.conf
%config(noreplace) %{_sysconfdir}/asterisk/privacy.conf
%config(noreplace) %{_sysconfdir}/asterisk/queues.conf
%config(noreplace) %{_sysconfdir}/asterisk/rpt.conf
%config(noreplace) %{_sysconfdir}/asterisk/rtp.conf
%config(noreplace) %{_sysconfdir}/asterisk/say.conf
%config(noreplace) %{_sysconfdir}/asterisk/sip.conf
%config(noreplace) %{_sysconfdir}/asterisk/sip_notify.conf
%config(noreplace) %{_sysconfdir}/asterisk/sla.conf
%config(noreplace) %{_sysconfdir}/asterisk/smdi.conf
%config(noreplace) %{_sysconfdir}/asterisk/telcordia-1.adsi
%config(noreplace) %{_sysconfdir}/asterisk/udptl.conf
%config(noreplace) %{_sysconfdir}/asterisk/users.conf
%config(noreplace) %{_sysconfdir}/asterisk/vpb.conf

%config(noreplace) %{_sysconfdir}/logrotate.d/asterisk

%dir %{_datadir}/asterisk/
%dir %{_datadir}/asterisk/agi-bin/
%{_datadir}/asterisk/images/
%{_datadir}/asterisk/keys/
%{_datadir}/asterisk/static-http/
%dir %{_datadir}/asterisk/moh/
%dir %{_datadir}/asterisk/sounds/

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/lib/asterisk/

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk/
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk/cdr-csv/
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk/cdr-custom/

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/
%attr(0770,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/outgoing/
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/tmp/
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/voicemail/

%attr(0755,asterisk,asterisk) %dir %{_localstatedir}/run/asterisk

%files alsa
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/asterisk/alsa.conf
%{_libdir}/asterisk/modules/chan_alsa.so

%if %{with_apidoc}
%files apidoc
%defattr(-,root,root,-)
%doc doc/api/html/*
%endif

%files conference
%defattr(-,root,root,-)
%doc apps/conference/CLI.txt
%doc apps/conference/Flags.txt
%doc apps/conference/LICENSE
%doc apps/conference/README
%doc apps/conference/README.videoswitch
%doc apps/conference/TODO
%{_libdir}/asterisk/modules/app_conference.so

%files curl
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/func_curl.so

%files devel
%defattr(-,root,root,-)
%doc doc/CODING-GUIDELINES
%doc doc/datastores.txt
%doc doc/linkedlists.txt
%doc doc/modules.txt
%doc doc/valgrind.txt

%dir %{_includedir}/asterisk
%{_includedir}/asterisk.h
%{_includedir}/asterisk/*.h

%files fax
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/app_rxfax.so
%{_libdir}/asterisk/modules/app_txfax.so

%files festival
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/asterisk/festival.conf
%{_libdir}/asterisk/modules/app_festival.so

%files firmware
%defattr(-,root,root,-)
%{_datadir}/asterisk/firmware/

%files jabber
%defattr(-,root,root,-)
%doc doc/jabber.txt
%doc doc/jingle.txt
%config(noreplace) %{_sysconfdir}/asterisk/gtalk.conf
%config(noreplace) %{_sysconfdir}/asterisk/jabber.conf
%{_libdir}/asterisk/modules/chan_gtalk.so
%{_libdir}/asterisk/modules/res_jabber.so

%files misdn
%defattr(-,root,root,-)
%doc doc/misdn.txt
%config(noreplace) %{_sysconfdir}/asterisk/misdn.conf
%{_libdir}/asterisk/modules/chan_misdn.so

%files mobile
%defattr(-,root,root,-)
%doc doc/chan_mobile.txt
%config(noreplace) %{_sysconfdir}/asterisk/mobile.conf
%{_libdir}/asterisk/modules/chan_mobile.so

%files odbc
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/asterisk/cdr_odbc.conf
%config(noreplace) %{_sysconfdir}/asterisk/func_odbc.conf
%config(noreplace) %{_sysconfdir}/asterisk/res_odbc.conf
%{_libdir}/asterisk/modules/cdr_odbc.so
%{_libdir}/asterisk/modules/func_odbc.so
%{_libdir}/asterisk/modules/res_config_odbc.so
%{_libdir}/asterisk/modules/res_odbc.so

%files oss
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/asterisk/oss.conf
%{_libdir}/asterisk/modules/chan_oss.so

%files postgresql
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/asterisk/cdr_pgsql.conf
%config(noreplace) %{_sysconfdir}/asterisk/res_pgsql.conf
%{_libdir}/asterisk/modules/cdr_pgsql.so
%{_libdir}/asterisk/modules/res_config_pgsql.so

%files radius
%defattr(-,root,root,-)
%doc doc/radius.txt
%{_libdir}/asterisk/modules/cdr_radius.so

%files skinny
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/asterisk/skinny.conf
%{_libdir}/asterisk/modules/chan_skinny.so

%files snmp
%defattr(-,root,root,-)
%doc doc/asterisk-mib.txt
%doc doc/digium-mib.txt
%doc doc/snmp.txt
%config(noreplace) %{_sysconfdir}/asterisk/res_snmp.conf
%{_datadir}/snmp/mibs/ASTERISK-MIB.txt
%{_datadir}/snmp/mibs/DIGIUM-MIB.txt
%{_libdir}/asterisk/modules/res_snmp.so

%files tds
%defattr(-,root,root,-)
%doc doc/freetds.txt
%config(noreplace) %{_sysconfdir}/asterisk/cdr_tds.conf
%{_libdir}/asterisk/modules/cdr_tds.so

%files voicemail
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/asterisk/voicemail.conf
%{_libdir}/asterisk/modules/app_hasnewvoicemail.so

%files voicemail-imap
%defattr(-,root,root,)
%doc doc/imapstorage.txt
%{_libdir}/asterisk/modules/app_directory_imap.so
%{_libdir}/asterisk/modules/app_voicemail_imap.so

%files voicemail-odbc
%defattr(-,root,root,-)
%doc doc/odbcstorage.txt
%doc doc/voicemail_odbc_postgresql.txt
%{_libdir}/asterisk/modules/app_directory_odbc.so
%{_libdir}/asterisk/modules/app_voicemail_odbc.so

%files voicemail-plain
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/app_directory_plain.so
%{_libdir}/asterisk/modules/app_voicemail_plain.so

%files zaptel
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/asterisk/meetme.conf
%config(noreplace) %{_sysconfdir}/asterisk/zapata.conf
%{_libdir}/asterisk/modules/app_flash.so
%{_libdir}/asterisk/modules/app_meetme.so
%{_libdir}/asterisk/modules/app_page.so
%{_libdir}/asterisk/modules/app_zapbarge.so
%{_libdir}/asterisk/modules/app_zapras.so
%{_libdir}/asterisk/modules/app_zapscan.so
%{_libdir}/asterisk/modules/chan_zap.so
%{_libdir}/asterisk/modules/codec_zap.so

%changelog
* Wed Dec 19 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16-2
- Add patch to bring source up to version 1.4.16.1 which will be
  released shortly to fix some crasher bugs introduced by 1.4.16.

* Tue Dec 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16-1
- Update to 1.4.16 to fix security bug.

* Sat Dec 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-7
- Really, really fix the build problems on devel.

* Sat Dec 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-6
- Tweaks to get to build on x86_64

* Wed Dec 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-5
- Exclude PPC64

* Wed Dec 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-4
- Don't build apidocs by default since there's a problem building on x86_64.

* Tue Dec 11 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-3
- Really get rid of zero length map files.

* Mon Dec 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-2
- Get rid of zero length map files.
- Shorten descriptions of voicemail subpackages

* Fri Nov 30 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.15-1
- Update to 1.4.15

* Tue Nov 20 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.14-2
- Fix license and other rpmlint warnings.

* Mon Nov 19 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.14-1
- Update to 1.4.14

* Fri Nov 16 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.13-7
- Add chan_mobile

* Tue Nov 13 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.13-6
- Don't build cdr_sqlite because sqlite2 has been orphaned.
- Rebase local patches to latest upstream SVN
- Update app_conference patch to latest from upstream SVN
- Apply post-1.4.13 patches from upstream SVN

* Wed Oct 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.13-1
- Update to 1.4.13

* Tue Oct  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.12.1-1
- Update to 1.4.12.1

* Wed Aug 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.11-1
- Update to 1.4.11

* Fri Aug 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.10.1-1
- Update to 1.4.10.1.

* Tue Aug  7 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.10-1
- Update to 1.4.10 (security update).

* Tue Aug  7 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-7
- Add a patch that allows alternate extensions to be defined in users.conf

* Mon Aug  6 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-6
- Update app_conference patch. Enter/leave sounds are now possible.

* Fri Jul 27 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-5
- Update patches so we don't need to run auto* tools, because autoconf
  2.60 is required and FC-6 and RHEL5 only have autoconf 2.59.

* Thu Jul 26 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-4
- Don't build app_mp3

* Wed Jul 25 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-3
- Add app_conference

* Wed Jul 25 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-2
- Use plain useradd/groupadd rather than the fedora-usermgmt
- Clean up requirements
- Clean up build requirements by moving them to package sections

* Tue Jul 24 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.9-1
- Update to 1.4.9

* Tue Jul 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.8-1
- Update to 1.4.8
- Drop ixjuser patch.

* Tue Jul 10 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.7.1-1
- Update to 1.4.7.1

* Mon Jul  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.7-1
- Update to 1.4.7
- RxFAX/TxFAX applications

* Sun Jul  1 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-4
- It's "sbin", not "bin" silly.

* Sat Jun 30 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-3
- Add patch that lets us change TOS bits even when running non-root

* Fri Jun 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-2
- voicemail needs to require /usr/bin/sox and /usr/bin/sendmail

* Fri Jun 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-1
- Update to 1.4.6
- Remove upstreamed patch.

* Thu Jun 21 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-10
- Build the IMAP and ODBC storage options of voicemail and split
  voicemail out into subpackages.
- Apply patch so that the system UW IMAP libray can be linked against.
- Patch modules.conf.sample so that alternal voicemail modules don't
  get loaded simultaneously.
- Link against system GSM library rather than internal copy.
- Patch the Makefile so that it doesn't add redundant/wrong compiler
  options.
- Force building with the standard RPM optimization flags.
- Install the Asterisk MIB in a location that net-snmp can find it.
- Only package docs in the main package that are relevant and that
  haven't been packaged by a subpackage.
- Other minor cleanups.

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-9
- Move sounds

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-8
- Update some more ownership/permissions

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-7
- Fix some permissions.

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-6
- Update init script patch
- Move pid file to subdir of /var/run

* Mon Jun 18 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-5
- Update init script patch to run as non-root

* Sun Jun 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-4
- Build modules that depend on FreeTDS.
- Don't build voicemail with ODBC storage.

* Sun Jun 17 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-3
- Have the build output the commands executing, rather than covering them up.

* Fri Jun 15 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-1
- Update to 1.4.5
- Remove upstreamed patch.

* Wed May  9 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.4-2
- Add a patch to fix CVE-2007-2488/ASA-2007-013

* Fri Apr 27 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.4-1
- Update to 1.4.4

* Wed Mar 21 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.2-1
- Update to 1.4.2

* Tue Mar  6 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.1-2
- Package the IAXy firmware
- Minor clean-ups in files

* Mon Mar  5 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.1-1
- Update to 1.4.1
- Don't build/package codec_zap (zaptel 1.4.0 doesn't support it)

* Fri Dec 15 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-6.beta4
- Update to 1.4.0-beta4
- Various cleanups.

* Fri Oct 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-5.beta3
- Don't package IAXy firmware because of license
- Don't build app_rpt
- Don't BR lm_sensors on PPC
- Better way to prevent download/installation of sound archives
- Redo tarball to eliminate non-free items

* Thu Oct 19 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-4.beta3
- Remove explicit dependency on glibc-kernheaders.
- Build jabber modules on PPC

* Wed Oct 18 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-3.beta3
- *Really* update to beta3
- chan_jingle has been taken out of 1.4
- Move misplaced binaries to where they should be

* Wed Oct 18 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-2.beta3
- Remove requirement on asterisk-sounds-core until licensing can be
  figured out.

* Wed Oct 18 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-1.beta3
- Update to 1.4.0-beta3

* Sun Oct 15 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.0-0.beta2
- Update to 1.4.0-beta2

* Tue Jul 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.10-1
- Update to 1.2.10.

* Wed Jun  7 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.9.1
- Update to 1.2.9.1

* Fri Jun  2 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.8
- Update to 1.2.8
- Add misdn.conf to list of configs.
- Drop chan_bluetooth patch for now...

* Tue May  2 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-6
- Zaptel subpackage shouldn't obsolete the sqlite subpackage.
- Remove mISDN until build issues can be figured out.

* Mon Apr 24 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-5
- Build mISDN channel drivers, modelled after spec file from David Woodhouse

* Thu Apr 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-4
- Update chan_bluetooth patch with some additional information as to
  it's source and comment out more in the configuration file.

* Thu Apr 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-3
- Add chan_bluetooth

* Wed Apr 19 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7.1-2
- Split off more stuff into subpackages.

* Wed Apr 12 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.7-1
- Update to 1.2.7

* Mon Apr 10 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.6-3
- Fix detection of libpri on 64 bit arches (taken from Matthias Saou's rpmforge package)
- Change sqlite subpackage name to sqlite2 (there are sqlite3 modules in development).

* Thu Apr  6 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.6-2
- Don't build GTK 1.X console since GTK 1.X is being moved out of core...

* Mon Mar 27 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.6-1
- Update to 1.2.6

* Mon Mar  6 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.5-1
- Update to 1.2.5.
- Removed upstreamed MOH patch.
- Add full urls to the app_(r|t)xfax.c sources.
- Update spandsp patch.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-4
- Actually apply the patch.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-3
- Add patch to keep Asterisk from crashing when using MOH inside a MeetMe conference.

* Mon Feb  6 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-2
- BR sqlite2-devel

* Tue Jan 31 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.4-1
- Update to 1.2.4.

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-4
- Took some tricks from Asterisk packages by Roy-Magne Mo.
-   Enable gtk console module.
-   BR gtk+-devel.
-   Add logrotate script.
-   BR sqlite2-devel and new sqlite subpackage.
-   BR doxygen and graphviz for building duxygen documentation. (But don't build it yet.)

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-3
- Completely eliminate the "asterisk" user from the spec file.
- Move more config files to subpackages.
- Consolidate two patches that patch the init script.
- BR curl-devel
- BR alsa-lib-devel
- alsa, curl, oss subpackages

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-2
- Do not run as user "asterisk" as that prevents setting of IP TOS (which is bad for quality of service).
- Add patch for setting TOS separately for SIP and RTP packets.

* Wed Jan 25 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2.3-1
- First version for Fedora Extras.

