#!/bin/sh

git filter-branch -f --commit-filter '
    if [ "$GIT_COMMITTER_NAME" = "Finnian Anderson" ];
    then
            skip_commit "$@";
    else
            git commit-tree "$@";
    fi' HEAD
