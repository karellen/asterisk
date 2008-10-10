#!/bin/sh

version=$1
if [ ! -f asterisk-$version.tar.gz ]; then
    echo "Can't find asterisk-$version.tar.gz!"
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


