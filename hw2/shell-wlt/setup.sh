#!/bin/bash

cd /cmshome/wangl157
rm -rf postgresql-7.4.13
rm -f postgresql-7.4.13.tar.gz
wget http://ftp-archives.postgresql.org/pub/source/v7.4.13/postgresql-7.4.13.tar.gz
tar -zxvf postgresql-7.4.13.tar.gz
cd postgresql-7.4.13

# Install PostgreSQL. 
./configure CFLAGS='-O0 -pipe -fcommon' --prefix=/cmshome/wangl157/postgresql-7.4.13/ --enable-depend --without-readline
make
make install

# Initialize a directory where PostgreSQL stores its data. 
mkdir data
./bin/initdb -D ./data
