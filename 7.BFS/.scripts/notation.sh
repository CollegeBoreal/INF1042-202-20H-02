#!/bin/sh

# --------------------------------------
# Grader
#
#
# --------------------------------------

source ../.scripts/students.sh --source-only

echo "# Correction au `date +"%d-%m-%Y %H:%M"`"

echo "\n## Légende\n"

echo "| Signe              | Signification                 |"
echo "|--------------------|-------------------------------|"
echo "| :heavy_check_mark: | Prêt à être corrigé           |"
echo "| :x:                | Projet inexistant             |"


echo "\n## Résultat\n"
echo "|:hash:| Boréal :id:                |  Notation         |"
echo "|------|----------------------------|-------------------|"

i=1

for id in "${ETUDIANTS[@]}"
do
   FILE=b${id}.py
   OK="| ${i} | [${id}](../${FILE}) | [:bar_chart:](Exexution.md#etudiant-${id}) | "
   KO="| ${i} | [${id}](../${FILE}) | [:x:](Exexution.md#etudiant-${id}) | "
   pytest .scripts/b${id}0000.py 2>&1 >  /dev/null
   RES=`echo $?`
   if [ $RES = 0 ]; then
       echo ${OK}
   else
       echo ${KO}
   fi
   let "i++"
done

