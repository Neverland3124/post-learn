#!/bin/bash

# neeed to copy the file to the postgres directory
cat "/cmshome/wangl157/cscd43w24_space/hw/hw2/code_my/nodeHashjoin.c" > "/cmshome/wangl157/postgresql-7.4.13/src/backend/executor/nodeHashjoin.c"
cat "/cmshome/wangl157/cscd43w24_space/hw/hw2/code_my/nodeHash.c" > "/cmshome/wangl157/postgresql-7.4.13/src/backend/executor/nodeHash.c"
cat "/cmshome/wangl157/cscd43w24_space/hw/hw2/code_my/execnodes.h" > "/cmshome/wangl157/postgresql-7.4.13/src/include/nodes/execnodes.h"
cat "/cmshome/wangl157/cscd43w24_space/hw/hw2/code_my/plannodes.h" > "/cmshome/wangl157/postgresql-7.4.13/src/include/nodes/plannodes.h"
cat "/cmshome/wangl157/cscd43w24_space/hw/hw2/code_my/nodeHash.h" > "/cmshome/wangl157/postgresql-7.4.13/src/include/executor/nodeHash.h"
cat "/cmshome/wangl157/cscd43w24_space/hw/hw2/code_my/nodeHashjoin.h" > "/cmshome/wangl157/postgresql-7.4.13/src/include/executor/nodeHashjoin.h"

# need to re gmake everything
cd /cmshome/wangl157/postgresql-7.4.13
gmake clean && gmake uninstall && gmake && gmake install
cd /cmshome/wangl157/cscd43w24_space/hw/hw2/

# /cmshome/wangl157/postgresql-7.4.13/bin/postmaster -p 54323 -D /cmshome/wangl157/postgresql-7.4.13/data > /cmshome/wangl157/cscd43w24_space/hw/hw2/logfile 2>&1 &

# /cmshome/wangl157/postgresql-7.4.13/bin/psql test -p 54323

# /cmshome/wangl157/postgresql-7.4.13/bin/pg_ctl stop -p 54323 -D /cmshome/wangl157/postgresql-7.4.13/data
