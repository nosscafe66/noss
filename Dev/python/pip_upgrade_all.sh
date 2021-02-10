#!/bin/sh
#PIP="pip"
#OUTDATED=$(${PIP} list --format=columns --outdated | awk 'NR>=3 {print $1}')
#[ -z "${OUTDATED}" ] && exit $?
#echo "${OUTDATED}"
#echo "[upgrade all? (y/n)]"
#read -r KEYINPUT
#if [ "${KEYINPUT}" = "y" ];then
#  echo "${OUTDATED}" | xargs ${PIP} install --upgrade
#fi
#exit $?

pip list --format=columns --outdated | awk 'NR>=3 {print $1}' | xargs pip install --upgrade