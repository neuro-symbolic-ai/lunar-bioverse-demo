#!/usr/bin/env sh

wf_descriptor=$1
source ./lunarverse_config.env

if [ $wf_descriptor != "all" ]; then
    python -m lunarverse.core.lunar_prefect.engine $wf_descriptor
else
    for path in `python util/workflow_index.py paths`; do
        echo $path
    done
fi
