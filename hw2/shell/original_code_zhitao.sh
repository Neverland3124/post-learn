#!/bin/bash

# neeed to copy the file to the postgres directory
cat "/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/code_original/nodeHashjoin.c" > "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/src/backend/executor/nodeHashjoin.c"
cat "/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/code_original/nodeHash.c" > "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/src/backend/executor/nodeHash.c"
cat "/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/code_original/execnodes.h" > "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/src/include/nodes/execnodes.h"
cat "/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/code_original/plannodes.h" > "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/src/include/nodes/plannodes.h"
cat "/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/code_original/nodeHash.h" > "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/src/include/executor/nodeHash.h"
cat "/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/code_original/nodeHashjoin.h" > "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/src/include/executor/nodeHashjoin.h"

# need to re gmake everything
cd /cmshome/xuzhitao/cscd43/postgresql-7.4.13
gmake clean && gmake uninstall && gmake && gmake install