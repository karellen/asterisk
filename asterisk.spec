#define _rc 2
Summary: The Open Source PBX
Name: asterisk
Version: 1.6.1.9
Release: 1%{?_rc:.rc%{_rc}}%{?dist}
License: GPLv2
Group: Applications/Internet
URL: http://www.asterisk.org/

Source0: http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-%{version}%{?_rc:-rc%{_rc}}.tar.gz
Source1: asterisk-logrotate
Source2: menuselect.makedeps
Source3: menuselect.makeopts
Source5: http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-%{version}%{?_rc:-rc%{_rc}}.tar.gz.asc

Patch1:  0001-Modify-init-scripts-for-better-Fedora-compatibility.patch
Patch2:  0002-Modify-modules.conf-so-that-different-voicemail-modu.patch
Patch5:  0005-Build-using-external-libedit.patch
Patch8:  0008-change-configure.ac-to-look-for-pkg-config-gmime-2.0.patch
Patch9:  0008-Revert-changes-to-pbx_lua-from-rev-126363-that-cause.patch
Patch11: 0011-Fix-up-some-paths.patch
Patch12: 0012-Add-LDAP-schema-that-is-compatible-with-Fedora-Direc.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: autoconf
BuildRequires: automake

# core build requirements
BuildRequires: openssl-devel
BuildRequires: newt-devel
%if 0%{?fedora} <= 8
BuildRequires: libtermcap-devel
%endif
BuildRequires: ncurses-devel
BuildRequires: libcap-devel
BuildRequires: gtk2-devel

# for res_http_post
BuildRequires: gmime22-devel

# for building docs
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: graphviz-gd

# for codec_speex
BuildRequires: speex-devel >= 1.2

# for format_ogg_vorbis
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel

# codec_gsm
BuildRequires: gsm-devel

# cli
BuildRequires: libedit-devel

Requires(pre): %{_sbindir}/useradd
Requires(pre): %{_sbindir}/groupadd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

# needed for icons used from %{_datadir}/asterisk/static-http/*
Requires: latex2html

# asterisk-conference package removed since patch no longer compiles
Obsoletes: asterisk-conference <= 1.6.0-0.14.beta9
Obsoletes: asterisk-mobile <= 1.6.1-0.23.rc1
Obsoletes: asterisk-firmware < 1.6.1.9-1

%description
Asterisk is a complete PBX in software. It runs on Linux and provides
all of the features you would expect from a PBX and more. Asterisk
does voice over IP in three protocols, and can interoperate with
almost all standards-based telephony equipment using relatively
inexpensive hardware.

%package ais
Summary: Modules for Asterisk that use OpenAIS
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: openais-devel

%description ais
Modules for Asterisk that use OpenAIS.

%package alsa
Summary: Modules for Asterisk that use Alsa sound drivers
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: alsa-lib-devel

%description alsa
Modules for Asterisk that use Alsa sound drivers.

%package apidoc
Summary: API documentation for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description apidoc
API documentation for Asterisk.

%package curl
Summary: Modules for Asterisk that use cURL
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: curl-devel

%description curl
Modules for Asterisk that use cURL.

%package dahdi
Summary: Modules for Asterisk that use DAHDI
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: dahdi-tools >= 2.0.0
Requires(pre): %{_sbindir}/usermod
BuildRequires: dahdi-tools-devel >= 2.0.0
BuildRequires: dahdi-tools-libs >= 2.0.0
BuildRequires: libpri-devel >= 1.4.6
BuildRequires: libss7-devel >= 1.0.1
Obsoletes: asterisk-zaptel <= 1.6.0-0.22.beta9
Provides: asterisk-zaptel = %{version}-%{release}

%description dahdi
Modules for Asterisk that use DAHDI.

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
BuildRequires: spandsp-devel >= 0.0.5-0.1.pre4

%description fax
FAX applications for Asterisk

%package festival
Summary: Festival application for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: festival

%description festival
Application for the Asterisk PBX that uses Festival to convert text to speech.

%package ices
Summary: Stream audio from Asterisk to an IceCast server
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: ices
Obsoletes: asterisk < 1.4.18-1
Conflicts: asterisk < 1.4.18-1

%description ices
Stream audio from Asterisk to an IceCast server.

%package jabber
Summary: Jabber/XMPP resources for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: iksemel-devel

%description jabber
Jabber/XMPP resources for Asterisk.

%package jack
Summary: JACK resources for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libresample-devel

%description jack
JACK resources for Asterisk.

%package lua
Summary: Lua resources for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: lua-devel

%description lua
Lua resources for Asterisk.

%package ldap
Summary: LDAP resources for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: openldap-devel

%description ldap
LDAP resources for Asterisk.

%package ldap-fds
Summary: LDAP resources for Asterisk and the Fedora Directory Server
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires: asterisk-ldap = %{version}-%{release}
Requires: fedora-ds-base

%description ldap-fds
LDAP resources for Asterisk and the Fedora Directory Server.

%package misdn
Summary: mISDN channel for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
Requires(pre): %{_sbindir}/usermod
BuildRequires: mISDN-devel

%description misdn
mISDN channel for Asterisk.

%package minivm
Summary: MiniVM applicaton for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description minivm
MiniVM application for Asterisk.

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

%package portaudio
Summary: Modules for Asterisk that use the portaudio library
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: portaudio-devel >= 19

%description portaudio
Modules for Asterisk that use the portaudio library.

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
# This subpackage depends on perl-libs, this Requires tracks versioning.
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description snmp
Module that enables SNMP monitoring of Asterisk.

%package sqlite
Summary: Sqlite modules for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: sqlite-devel

%description sqlite
Sqlite modules for Asterisk.

%package tds
Summary: Modules for Asterisk that use FreeTDS
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: freetds-devel

%description tds
Modules for Asterisk that use FreeTDS.

%package unistim
Summary: Unistim channel for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}

%description unistim
Unistim channel for Asterisk

%package usbradio
Summary: USB radio channel for Asterisk
Group: Applications/Internet
Requires: asterisk = %{version}-%{release}
BuildRequires: libusb-devel
BuildRequires: alsa-lib-devel

%description usbradio
Unistim channel for Asterisk

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

%prep
%setup0 -q -n asterisk-%{version}%{?_rc:-rc%{_rc}}
%patch1 -p0
%patch2 -p0
%patch5 -p0
%patch8 -p0
%patch9 -p1
%patch11 -p0
%patch12 -p1

cp %{SOURCE2} menuselect.makedeps
cp %{SOURCE3} menuselect.makeopts

# Fixup makefile so sound archives aren't downloaded/installed
%{__perl} -pi -e 's/^all:.*$/all:/' sounds/Makefile
%{__perl} -pi -e 's/^install:.*$/install:/' sounds/Makefile

# convert comments in one file to UTF-8
mv main/fskmodem.c main/fskmodem.c.old
iconv -f iso-8859-1 -t utf-8 -o main/fskmodem.c main/fskmodem.c.old
touch -r main/fskmodem.c.old main/fskmodem.c
rm main/fskmodem.c.old

chmod -x contrib/scripts/dbsep.cgi

%build

%define optflags %(rpm --eval %%{optflags}) -Werror-implicit-function-declaration

aclocal -I autoconf
autoconf
autoheader

pushd menuselect/mxml
%configure
popd

pushd menuselect
%configure
popd 

pushd main/editline
%configure
popd

%configure --with-imap=system --with-gsm=/usr --with-libedit=yes

ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_plain.so
mv apps/app_directory.so apps/app_directory_plain.so

%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=IMAP_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_imap.so
mv apps/app_directory.so apps/app_directory_imap.so

%{__sed} -i -e 's/^MENUSELECT_OPTS_app_voicemail=.*$/MENUSELECT_OPTS_app_voicemail=ODBC_STORAGE/' menuselect.makeopts
ASTCFLAGS="%{optflags}" make DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk NOISY_BUILD=1

rm apps/app_voicemail.o apps/app_directory.o
mv apps/app_voicemail.so apps/app_voicemail_odbc.so
mv apps/app_directory.so apps/app_directory_odbc.so

# so that these modules don't get built again during the install phase
touch apps/app_voicemail.o apps/app_directory.o
touch apps/app_voicemail.so apps/app_directory.so

ASTCFLAGS="%{optflags}" make progdocs DEBUG= OPTIMIZE= ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk  ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk NOISY_BUILD=1

# fix dates so that we don't get multilib conflicts
find doc/api/html -type f -print0 | xargs --null touch -r ChangeLog

%install
rm -rf %{buildroot}

ASTCFLAGS="%{optflags}" make install DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk
ASTCFLAGS="%{optflags}" make samples DEBUG= OPTIMIZE= DESTDIR=%{buildroot} ASTVARRUNDIR=%{_localstatedir}/run/asterisk ASTDATADIR=%{_datadir}/asterisk ASTVARLIBDIR=%{_datadir}/asterisk ASTDBDIR=%{_localstatedir}/spool/asterisk

install -D -p -m 0755 contrib/init.d/rc.redhat.asterisk %{buildroot}%{_initrddir}/asterisk
install -D -p -m 0644 contrib/sysconfig/asterisk %{buildroot}%{_sysconfdir}/sysconfig/asterisk
install -D -p -m 0644 contrib/scripts/99asterisk.ldif %{buildroot}%{_sysconfdir}/dirsrv/schema/99asterisk.ldif
install -D -p -m 0644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/asterisk
install -D -p -m 0644 doc/asterisk-mib.txt %{buildroot}%{_datadir}/snmp/mibs/ASTERISK-MIB.txt
install -D -p -m 0644 doc/digium-mib.txt %{buildroot}%{_datadir}/snmp/mibs/DIGIUM-MIB.txt

rm %{buildroot}%{_libdir}/asterisk/modules/app_directory.so
rm %{buildroot}%{_libdir}/asterisk/modules/app_voicemail.so
install -D -p -m 0755 apps/app_directory_imap.so %{buildroot}%{_libdir}/asterisk/modules
install -D -p -m 0755 apps/app_voicemail_imap.so %{buildroot}%{_libdir}/asterisk/modules
install -D -p -m 0755 apps/app_directory_odbc.so %{buildroot}%{_libdir}/asterisk/modules
install -D -p -m 0755 apps/app_voicemail_odbc.so %{buildroot}%{_libdir}/asterisk/modules
install -D -p -m 0755 apps/app_directory_plain.so %{buildroot}%{_libdir}/asterisk/modules
install -D -p -m 0755 apps/app_voicemail_plain.so %{buildroot}%{_libdir}/asterisk/modules

# create some directories that need to be packaged
mkdir -p %{buildroot}%{_datadir}/asterisk/moh
mkdir -p %{buildroot}%{_datadir}/asterisk/sounds
mkdir -p %{buildroot}%{_localstatedir}/lib/asterisk
mkdir -p %{buildroot}%{_localstatedir}/log/asterisk/cdr-custom
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/festival
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/monitor
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/outgoing
mkdir -p %{buildroot}%{_localstatedir}/spool/asterisk/uploads

# We're not going to package any of the sample AGI scripts
rm -f %{buildroot}%{_datadir}/asterisk/agi-bin/*

# Don't package the sample voicemail user
rm -rf %{buildroot}%{_localstatedir}/spool/asterisk/voicemail/default

# Don't package example phone provision configs
rm -rf %{buildroot}%{_datadir}/asterisk/phoneprov/*

# these are compiled with -O0 and thus include unfortified code.
rm -rf %{buildroot}%{_sbindir}/hashtest
rm -rf %{buildroot}%{_sbindir}/hashtest2

rm -rf %{buildroot}%{_datadir}/asterisk/firmware/iax/*

find doc/api/html -name \*.map -size 0 -delete

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

%pre dahdi
%{_sbindir}/usermod -a -G dahdi asterisk

%pre misdn
%{_sbindir}/usermod -a -G misdn asterisk

%files
%defattr(-,root,root,-)
%doc README* *.txt ChangeLog BUGS CREDITS configs

%doc doc/asterisk.sgml
%doc doc/backtrace.txt
%doc doc/callfiles.txt
%doc doc/externalivr.txt
%doc doc/macroexclusive.txt
%doc doc/manager_1_1.txt
%doc doc/modules.txt
%doc doc/PEERING
%doc doc/queue.txt
%doc doc/rtp-packetization.txt
%doc doc/siptls.txt
%doc doc/smdi.txt
%doc doc/sms.txt
%doc doc/speechrec.txt
%doc doc/ss7.txt
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
%{_libdir}/asterisk/modules/app_image.so
%{_libdir}/asterisk/modules/app_macro.so
%{_libdir}/asterisk/modules/app_milliwatt.so
%{_libdir}/asterisk/modules/app_mixmonitor.so
%{_libdir}/asterisk/modules/app_morsecode.so
%{_libdir}/asterisk/modules/app_nbscat.so
%{_libdir}/asterisk/modules/app_parkandannounce.so
%{_libdir}/asterisk/modules/app_playback.so
%{_libdir}/asterisk/modules/app_privacy.so
%{_libdir}/asterisk/modules/app_queue.so
%{_libdir}/asterisk/modules/app_readexten.so
%{_libdir}/asterisk/modules/app_readfile.so
%{_libdir}/asterisk/modules/app_read.so
%{_libdir}/asterisk/modules/app_record.so
%{_libdir}/asterisk/modules/app_sayunixtime.so
%{_libdir}/asterisk/modules/app_senddtmf.so
%{_libdir}/asterisk/modules/app_sendtext.so
%{_libdir}/asterisk/modules/app_setcallerid.so
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
%{_libdir}/asterisk/modules/app_waituntil.so
%{_libdir}/asterisk/modules/app_while.so
%{_libdir}/asterisk/modules/app_zapateller.so
%{_libdir}/asterisk/modules/cdr_csv.so
%{_libdir}/asterisk/modules/cdr_custom.so
%{_libdir}/asterisk/modules/cdr_manager.so
%{_libdir}/asterisk/modules/chan_agent.so
%{_libdir}/asterisk/modules/chan_iax2.so
%{_libdir}/asterisk/modules/chan_local.so
%{_libdir}/asterisk/modules/chan_mgcp.so
%{_libdir}/asterisk/modules/chan_phone.so
%{_libdir}/asterisk/modules/chan_sip.so
%{_libdir}/asterisk/modules/codec_adpcm.so
%{_libdir}/asterisk/modules/codec_alaw.so
%{_libdir}/asterisk/modules/codec_a_mu.so
%{_libdir}/asterisk/modules/codec_g722.so
%{_libdir}/asterisk/modules/codec_g726.so
%{_libdir}/asterisk/modules/codec_gsm.so
%{_libdir}/asterisk/modules/codec_lpc10.so
%{_libdir}/asterisk/modules/codec_resample.so
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
%{_libdir}/asterisk/modules/format_sln16.so
%{_libdir}/asterisk/modules/format_vox.so
%{_libdir}/asterisk/modules/format_wav_gsm.so
%{_libdir}/asterisk/modules/format_wav.so
%{_libdir}/asterisk/modules/func_audiohookinherit.so
%{_libdir}/asterisk/modules/func_base64.so
%{_libdir}/asterisk/modules/func_blacklist.so
%{_libdir}/asterisk/modules/func_callerid.so
%{_libdir}/asterisk/modules/func_cdr.so
%{_libdir}/asterisk/modules/func_channel.so
%{_libdir}/asterisk/modules/func_config.so
%{_libdir}/asterisk/modules/func_cut.so
%{_libdir}/asterisk/modules/func_db.so
%{_libdir}/asterisk/modules/func_devstate.so
%{_libdir}/asterisk/modules/func_dialgroup.so
%{_libdir}/asterisk/modules/func_dialplan.so
%{_libdir}/asterisk/modules/func_enum.so
%{_libdir}/asterisk/modules/func_env.so
%{_libdir}/asterisk/modules/func_extstate.so
%{_libdir}/asterisk/modules/func_global.so
%{_libdir}/asterisk/modules/func_groupcount.so
%{_libdir}/asterisk/modules/func_iconv.so
%{_libdir}/asterisk/modules/func_lock.so
%{_libdir}/asterisk/modules/func_logic.so
%{_libdir}/asterisk/modules/func_math.so
%{_libdir}/asterisk/modules/func_md5.so
%{_libdir}/asterisk/modules/func_module.so
%{_libdir}/asterisk/modules/func_rand.so
%{_libdir}/asterisk/modules/func_realtime.so
%{_libdir}/asterisk/modules/func_sha1.so
%{_libdir}/asterisk/modules/func_shell.so
%{_libdir}/asterisk/modules/func_speex.so
%{_libdir}/asterisk/modules/func_strings.so
%{_libdir}/asterisk/modules/func_sysinfo.so
%{_libdir}/asterisk/modules/func_timeout.so
%{_libdir}/asterisk/modules/func_uri.so
%{_libdir}/asterisk/modules/func_version.so
%{_libdir}/asterisk/modules/func_volume.so
%{_libdir}/asterisk/modules/pbx_ael.so
%{_libdir}/asterisk/modules/pbx_config.so
%{_libdir}/asterisk/modules/pbx_dundi.so
%{_libdir}/asterisk/modules/pbx_loopback.so
%{_libdir}/asterisk/modules/pbx_realtime.so
%{_libdir}/asterisk/modules/pbx_spool.so
%{_libdir}/asterisk/modules/res_adsi.so
%{_libdir}/asterisk/modules/res_ael_share.so
%{_libdir}/asterisk/modules/res_agi.so
%{_libdir}/asterisk/modules/res_clioriginate.so
%{_libdir}/asterisk/modules/res_convert.so
%{_libdir}/asterisk/modules/res_crypto.so
%{_libdir}/asterisk/modules/res_indications.so
%{_libdir}/asterisk/modules/res_http_post.so
%{_libdir}/asterisk/modules/res_limit.so
%{_libdir}/asterisk/modules/res_monitor.so
%{_libdir}/asterisk/modules/res_musiconhold.so
%{_libdir}/asterisk/modules/res_phoneprov.so
%{_libdir}/asterisk/modules/res_realtime.so
%{_libdir}/asterisk/modules/res_smdi.so
%{_libdir}/asterisk/modules/res_speech.so
%{_libdir}/asterisk/modules/res_timing_pthread.so
%{_libdir}/asterisk/modules/test_dlinklists.so
%{_libdir}/asterisk/modules/test_heap.so

%{_sbindir}/aelparse
%{_sbindir}/astcanary
%{_sbindir}/asterisk
%{_sbindir}/astgenkey
%{_sbindir}/astman
%{_sbindir}/autosupport
%{_sbindir}/conf2ael
%{_sbindir}/muted
%{_sbindir}/rasterisk
%{_sbindir}/refcounter
%{_sbindir}/safe_asterisk
%{_sbindir}/smsq
%{_sbindir}/stereorize
%{_sbindir}/streamplayer

%{_mandir}/man8/asterisk.8*
%{_mandir}/man8/astgenkey.8*
%{_mandir}/man8/autosupport.8*
%{_mandir}/man8/safe_asterisk.8*

%attr(0750,asterisk,asterisk) %dir %{_sysconfdir}/asterisk
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/adsi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/adtranvofr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/agents.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/alarmreceiver.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/amd.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/asterisk.adsi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/asterisk.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_custom.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_manager.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cli.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/codecs.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dnsmgr.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dsp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dundi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/enum.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extconfig.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.ael
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/features.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/followme.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/h323.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/http.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/iax.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/iaxprov.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/indications.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/logger.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/manager.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/mgcp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/modules.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/musiconhold.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/muted.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/osp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/phone.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/phoneprov.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/queuerules.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/queues.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/rpt.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/rtp.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/say.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sip.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sip_notify.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/sla.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/smdi.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/telcordia-1.adsi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/udptl.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/users.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/vpb.conf

%config(noreplace) %{_sysconfdir}/logrotate.d/asterisk

%dir %{_datadir}/asterisk
%dir %{_datadir}/asterisk/agi-bin
%dir %{_datadir}/asterisk/firmware
%dir %{_datadir}/asterisk/firmware/iax
%{_datadir}/asterisk/images
%attr(0750,asterisk,asterisk) %{_datadir}/asterisk/keys
%{_datadir}/asterisk/phoneprov
%{_datadir}/asterisk/static-http
%dir %{_datadir}/asterisk/moh
%dir %{_datadir}/asterisk/sounds

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/lib/asterisk

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk/cdr-csv
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/log/asterisk/cdr-custom

%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk
%attr(0770,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/monitor
%attr(0770,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/outgoing
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/tmp
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/uploads
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/voicemail

%attr(0755,asterisk,asterisk) %dir %{_localstatedir}/run/asterisk

%files ais
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/ais.conf
%{_libdir}/asterisk/modules/res_ais.so

%files alsa
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/alsa.conf
%{_libdir}/asterisk/modules/chan_alsa.so

%files apidoc
%defattr(-,root,root,-)
%doc doc/api/html/*

%files curl
%defattr(-,root,root,-)
%doc contrib/scripts/dbsep.cgi
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/dbsep.conf
%{_libdir}/asterisk/modules/func_curl.so
%{_libdir}/asterisk/modules/res_config_curl.so
%{_libdir}/asterisk/modules/res_curl.so

%files dahdi
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/meetme.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/chan_dahdi.conf
%{_libdir}/asterisk/modules/app_flash.so
%{_libdir}/asterisk/modules/app_meetme.so
%{_libdir}/asterisk/modules/app_page.so
%{_libdir}/asterisk/modules/app_dahdibarge.so
%{_libdir}/asterisk/modules/app_dahdiras.so
%{_libdir}/asterisk/modules/app_dahdiscan.so
%{_libdir}/asterisk/modules/chan_dahdi.so
%{_libdir}/asterisk/modules/codec_dahdi.so
%{_libdir}/asterisk/modules/res_timing_dahdi.so

%files devel
%defattr(-,root,root,-)
%doc doc/CODING-GUIDELINES
%doc doc/datastores.txt
%doc doc/modules.txt
%doc doc/valgrind.txt

%dir %{_includedir}/asterisk
%{_includedir}/asterisk.h
%{_includedir}/asterisk/*.h

%files fax
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/app_fax.so

%files festival
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/festival.conf
%attr(0750,asterisk,asterisk) %dir %{_localstatedir}/spool/asterisk/festival
%{_libdir}/asterisk/modules/app_festival.so

%files ices
%defattr(-,root,root,-)
%doc contrib/asterisk-ices.xml
%{_libdir}/asterisk/modules/app_ices.so

%files jabber
%defattr(-,root,root,-)
%doc doc/jabber.txt
%doc doc/jingle.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/gtalk.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/jabber.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/jingle.conf
%{_libdir}/asterisk/modules/chan_gtalk.so
%{_libdir}/asterisk/modules/chan_jingle.so
%{_libdir}/asterisk/modules/res_jabber.so

%files jack
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/app_jack.so

%files lua
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions.lua
%{_libdir}/asterisk/modules/pbx_lua.so

%files ldap
%defattr(-,root,root,-)
%doc doc/ldap.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_ldap.conf
%{_libdir}/asterisk/modules/res_config_ldap.so

%files ldap-fds
%defattr(-,root,root,-)
%{_sysconfdir}/dirsrv/schema/99asterisk.ldif

%files minivm
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/extensions_minivm.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/minivm.conf
%{_libdir}/asterisk/modules/app_minivm.so

%files misdn
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/misdn.conf
%{_libdir}/asterisk/modules/chan_misdn.so

%files odbc
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_adaptive_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/func_odbc.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_odbc.conf
%{_libdir}/asterisk/modules/cdr_adaptive_odbc.so
%{_libdir}/asterisk/modules/cdr_odbc.so
%{_libdir}/asterisk/modules/func_odbc.so
%{_libdir}/asterisk/modules/res_config_odbc.so
%{_libdir}/asterisk/modules/res_odbc.so

%files oss
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/oss.conf
%{_libdir}/asterisk/modules/chan_oss.so

%files portaudio
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/console.conf
%{_libdir}/asterisk/modules/chan_console.so

%files postgresql
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_pgsql.conf
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_pgsql.conf
%doc contrib/scripts/realtime_pgsql.sql
%{_libdir}/asterisk/modules/cdr_pgsql.so
%{_libdir}/asterisk/modules/res_config_pgsql.so

%files radius
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/cdr_radius.so

%files skinny
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/skinny.conf
%{_libdir}/asterisk/modules/chan_skinny.so

%files snmp
%defattr(-,root,root,-)
%doc doc/asterisk-mib.txt
%doc doc/digium-mib.txt
%doc doc/snmp.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/res_snmp.conf
%{_datadir}/snmp/mibs/ASTERISK-MIB.txt
%{_datadir}/snmp/mibs/DIGIUM-MIB.txt
%{_libdir}/asterisk/modules/res_snmp.so

%files sqlite
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_sqlite3_custom.conf
%{_libdir}/asterisk/modules/cdr_sqlite3_custom.so

%files tds
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/cdr_tds.conf
%{_libdir}/asterisk/modules/cdr_tds.so

%files unistim
%defattr(-,root,root,-)
%doc doc/unistim.txt
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/unistim.conf
%{_libdir}/asterisk/modules/chan_unistim.so

%files usbradio
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/usbradio.conf
%{_libdir}/asterisk/modules/chan_usbradio.so

%files voicemail
%defattr(-,root,root,-)
%attr(0640,asterisk,asterisk) %config(noreplace) %{_sysconfdir}/asterisk/voicemail.conf
%{_libdir}/asterisk/modules/func_vmcount.so

%files voicemail-imap
%defattr(-,root,root,)
%{_libdir}/asterisk/modules/app_directory_imap.so
%{_libdir}/asterisk/modules/app_voicemail_imap.so

%files voicemail-odbc
%defattr(-,root,root,-)
%doc doc/voicemail_odbc_postgresql.txt
%{_libdir}/asterisk/modules/app_directory_odbc.so
%{_libdir}/asterisk/modules/app_voicemail_odbc.so

%files voicemail-plain
%defattr(-,root,root,-)
%{_libdir}/asterisk/modules/app_directory_plain.so
%{_libdir}/asterisk/modules/app_voicemail_plain.so

%changelog
* Wed Nov  4 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.9-1
- Update to 1.6.1.9 to fix AST-2009-009/CVE-2008-7220 and AST-2009-008
- Fix obsoletes for firmware subpackage

* Tue Oct 27 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.8-1
- Update to 1.6.1.8 to fix bug 531199:
-
- http://downloads.asterisk.org/pub/security/AST-2009-007.html
-
- A missing ACL check for handling SIP INVITEs allows a device to make
- calls on networks intended to be prohibited as defined by the "deny"
- and "permit" lines in sip.conf. The ACL check for handling SIP
- registrations was not affected.

* Sat Oct 24 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.7-0.4.rc2
- Add an AST_EXTRA_ARGS option to the init script
- have the init script to cd to /var/spool/asterisk to prevent annoying message

* Sat Oct 24 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.7-0.3.rc2
- Compile against gmime 2.2 instead of gmime 2.4 because the patch to convert the API calls from 2.2 to 2.4 caused crashes.

* Fri Oct  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.7-0.2.rc2
- Require latex2html used in static-http documents

* Thu Oct  8 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.7-0.1.rc2
- Update to 1.6.1.7-rc2
- Merge firmware subpackage back into main package
- No longer need to strip tarball since it no longer contains any non-free items
- Tighten up permissions/ownership of config files.
- Fix up some more paths
- Drop unneeded patch

* Wed Sep  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.6-2
- Enable building of API docs.
- Depend on version 1.2 or newer of speex

* Sun Sep  6 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1.6-1
- Update to 1.6.1.6
- Drop patches that are too troublesome to maintain anymore or have been integrated upstream.

* Tue Sep  1 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.26.rc1
- Add a patch from Quentin Armitage and rebuld.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.1-0.25.rc1
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-0.24.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.23.rc1
- Rebuild to pick up new AIS and ODBC deps.
- Update script that strips out bad content from tarball to do the
  download and to check the GPG signature.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-0.22.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.21.rc1
- Update to 1.6.1-rc1
- Add backport of conference bridging that is slated for 1.6.2
- Add patches to conference bridging that implement CLI apps

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.1-0.13.beta4
- rebuild with new openssl

* Sun Jan  4 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.12.beta4
- Fedora Directory Server compatibility patch/subpackage.

* Sun Jan  4 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.10.beta4
- Fix up paths. BZ#477238

* Sat Jan  3 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.9.beta4
- Update patches

* Sat Jan  3 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.8.beta4
- Update to 1.6.1-beta4

* Tue Dec  9 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.7.beta3
- Update to 1.6.1-beta3

* Tue Dec  9 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.6.1-0.6.beta2
- Rebuild for new gmime

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.5.beta2
- Add patch to fix missing variable on PPC.

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.4.beta2
- Update PPC systems don't have sys/io.h patch.

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.3.beta2
- PPC systems don't have sys/io.h

* Fri Nov  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-0.2.beta2
- Update to 1.6.1 beta 2

* Wed Nov  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0.1-3
- Fix issue with init script giving wrong path to config file.

* Thu Oct 16 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0.1-2
- Explicitly require dahdi-tools-libs to see if we can get this to build.

* Fri Oct 10 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-1
- Update to final release.

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> - 1.6.0-0.22.beta9
- Rebuild

* Wed Jul 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.21.beta9
- Replace app_rxfax/app_txfax with app_fax taken from upstream SVN.

* Tue Jul 29 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.20.beta9
- Bump release and rebuild with new libpri and zaptel.

* Fri Jul 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.19.beta9
- Add patch pulled from upstream SVN that fixes AST-2008-010 and AST-2008-011.

* Fri Jul 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.18.beta9
- Add patch for LDAP extracted from upstream SVN (#442011)

* Thu Jul  2 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.17.beta9
- Add patch that unbreaks cdr_tds with FreeTDS 0.82.
- Properly obsolete conference subpackage.

* Thu Jun 12 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.16.beta9
- Disable building cdr_tds since new FreeTDS in rawhide no longer provides needed library.

* Wed Jun 11 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.15.beta9
- Bump release and rebuild to fix libtds breakage.

* Mon May 19 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.14.beta9
- Update to 1.6.0-beta9.
- Update patches so that they apply cleanly.
- Temporarily disable app_conference patch as it doesn't compile
- config/scripts/postgres_cdr.sql has been merged into realtime_pgsql.sql
- Re-add the asterisk-strip.sh script as a source file.

* Tue Apr 22 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.13.beta8
- Update to 1.6.0-beta8
- Contains fixes for AST-2008-006 / CVE-2008-1897

* Wed Apr  2 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.12.beta7.1
- Return to stripped tarballs since there's more non-free content in
  the Asterisk tarballs than I thought.

* Sun Mar 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.11.beta7.1
- Update to 1.6.0-beta7.1
- Update patches
- Back out some changes that were made because beta7 was tagged from
  the wrong branch.

* Fri Mar 28 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.10.beta7
- Update to 1.6.0-beta7
- The Asterisk tarball no longer contains the iLBC code, so we can
  directly use the upstream tarball without having to modify it.
- Get rid of the asterisk-strip.sh script since it's no longer needed.
- Diable build of codec_ilbc and format_ilbc (these do not contain any
  legally suspect code so they can be included in the tarball but it's
  pointless building them).
- Update chan_mobile patch to fix API breakages.
- Add a patch to chan_usbradio to fix API breakages.

* Thu Mar 27 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.9.beta6
- Add Postgresql schemas from contrib as documentation to the Postgresql subpackage.

* Tue Mar 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.8.beta6
- Update patches.
- Add patch to compile against external libedit rather than using the
  in-tree version.
- Add -Werror-implicit-function-declaration to optflags.
- Get rid of hashtest and hashtest2 binaries that link to unfortified
  versions of *printf functions.  They are compiled with -O0 which
  somehow pulls in the wrong versions.  These programs aren't
  necessary to the operation of the package anyway.

* Wed Mar 19 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.6.beta6
- Update to 1.6.0-beta6 to fix some security issues.
-
- AST-2008-002 details two buffer overflows that were discovered in
- RTP codec payload type handling.
-  * http://downloads.digium.com/pub/security/AST-2008-002.pdf
-  * All users of SIP in Asterisk 1.4 and 1.6 are affected.
-
- AST-2008-003 details a vulnerability which allows an attacker to
- bypass SIP authentication and to make a call into the context
- specified in the general section of sip.conf.
-  * http://downloads.digium.com/pub/security/AST-2008-003.pdf
-  * All users of SIP in Asterisk 1.0, 1.2, 1.4, or 1.6 are affected.
-
- AST-2008-004 Logging messages displayed using the ast_verbose
- logging API call are not displayed as a character string, they are
- displayed as a format string.
-  * http://downloads.digium.com/pub/security/AST-2008-004.pdf
-
- AST-2008-005 details a problem in the way manager IDs are caculated.
-  * http://downloads.digium.com/pub/security/AST-2008-005.pdf

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.0-0.5.beta5
- add Requires for versioned perl (libperl.so)

* Wed Mar  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.4.beta5
- Update to 1.6.0-beta5
- Remove upstreamed patches.

* Mon Mar  3 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.3.beta4
- Package the directory used to store monitor recordings.

* Tue Feb 26 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.2.beta4
- Add patch from David Woodhouse that fixes building on PPC64.

* Tue Feb 26 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.0-0.1.beta4
- Update to 1.6.0 beta 4

* Wed Feb 13 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.18-1
- Update to 1.4.18.
- Use -march=i486 on i386 builds for atomic operations (GCC 4.3
  compatibility).
- Use "logger reload" instead of "logger rotate" in logrotate file
  (#432197).
- Don't explicitly specify a group in in the init script to prevent
  Zaptel breakage (#426629).
- Split app_ices out to a separate package so that the ices package
  can be required.
- pbx_kdeconsole has been dropped, don't specifically exclude it from
  the build anymore.
- Update app_conference patch.
- Drop upstreamed libcap patch.

* Wed Jan  2 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.17-1
- Update to 1.4.17 to fix AST-2008-001.

* Fri Dec 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16.2-1
- Update to 1.4.16.2

* Sat Dec 22 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16.1-2
- Bump release and rebuild to fix broken dep on uw-imap.

* Wed Dec 19 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.16.1-1
- Update to the real 1.4.16.1.

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

