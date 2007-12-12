#!/bin/sh

version=$1
if [ ! -f asterisk-$version.tar.gz ]; then
    echo "Can't find asterisk-$version.tar.gz!"
    exit 1
fi


tar xf asterisk-$version.tar.gz
rm asterisk-$version/codecs/codec_ilbc.c
rm -rf asterisk-$version/codecs/ilbc
rm asterisk-$version/codecs/ilbc_slin_ex.h
rm asterisk-$version/codecs/slin_ilbc_ex.h
rm asterisk-$version/formats/format_ilbc.c
tar czf asterisk-$version-stripped.tar.gz asterisk-$version
rm -rf asterisk-$version

echo "MD5 Sums"
echo "========"
md5sum asterisk-$version.tar.gz  asterisk-$version-stripped.tar.gz
echo
echo "SHA1 Sums"
echo "========="
sha1sum asterisk-$version.tar.gz  asterisk-$version-stripped.tar.gz

