#!/bin/sh

version=$1

if [ -z $version ]; then
    echo "Please specify a version!"
    exit 1
fi

wget --continue --timestamping http://downloads.digium.com/pub/telephony/asterisk/releases/asterisk-$version.tar.gz \
                               http://downloads.digium.com/pub/telephony/asterisk/releases/asterisk-$version.tar.gz.asc

if [ ! $? ]; then
    echo "Unable to download!"
    exit 1
fi

if [ ! -f asterisk-$version.tar.gz ]; then
    echo "Can't find asterisk-$version.tar.gz!"
    exit 1
fi

if [ ! -f asterisk-$version.tar.gz.asc ]; then
    echo "Can't find asterisk-$version.tar.gz.asc!"
    exit 1
fi

gpg --keyring=$(pwd)/asterisk-developer-pubring.gpg --verify asterisk-$version.tar.gz.asc asterisk-$version.tar.gz

if [ ! $? ]; then
    echo "Bad signature!!!!"
    exit 1
fi

echo
read -p "Does the GPG signature look OK? " -n 1
echo

if [ $REPLY != "Y" -a $REPLY != "y" ]; then
    exit 1
fi

tar xf asterisk-$version.tar.gz
rm asterisk-$version/sounds/*.tar.gz
tar czf asterisk-$version-stripped.tar.gz asterisk-$version
rm -rf asterisk-$version

echo "# MD5 Sums"
echo "# ========"
md5sum asterisk-$version.tar.gz  asterisk-$version-stripped.tar.gz | sed -e 's/^/# /'
echo "#"
echo "# SHA1 Sums"
echo "# ========="
sha1sum asterisk-$version.tar.gz  asterisk-$version-stripped.tar.gz  | sed -e 's/^/# /'
echo "#"
echo "# SHA256 Sums"
echo "# ========="
sha256sum asterisk-$version.tar.gz  asterisk-$version-stripped.tar.gz  | sed -e 's/^/# /'

make new-sources FILES="asterisk-$version-stripped.tar.gz asterisk-$version.tar.gz.asc asterisk-developer-pubring.gpg"
