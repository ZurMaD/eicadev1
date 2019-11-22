#!/bin/sh
echo 'Porfavor conecta el celular en modo debug - desarrollador'
#buildozer android deploy run logcat | grep -i -e "python  :"
buildozer -v android debug