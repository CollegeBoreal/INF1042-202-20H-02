#!/bin/sh

# --------------------------------------
#
#
#
# --------------------------------------

#source ../.scripts/students.sh --source-only

ETUDIANTS=(
300111441
300115065
300115140
300116593
300116670
300116685
300116973
300117178
300117314
300117444
300117705
300117782
300117784
300117806
300118196
300118524
)

   
echo "# Participation au `date +"%d-%m-%Y %H:%M"`"
echo "\n"


echo "| Table des matières            | Description                                             |"
echo "|-------------------------------|---------------------------------------------------------|"
echo "| :a: [Présence](#a-présence)   | L'étudiant.e a fait son travail    :heavy_check_mark:   |"
echo "| :b: [Précision](#b-précision) | L'étudiant.e a réussi son travail  :tada:               |"

echo "\n## Légende\n"

echo "| Signe              | Signification                 |"
echo "|--------------------|-------------------------------|"
echo "| :heavy_check_mark: | Prêt à être corrigé           |"
echo "| :x:                | Projet inexistant             |"


echo "\n## :a: Présence\n"
echo "|:hash:| Boréal :id:                | Fait               |"
echo "|------|----------------------------|--------------------|"

i=1

for id in "${ETUDIANTS[@]}"
do
   FILE=b${id}.py
   OK="| ${i} | [${id}](../${FILE}) | [:heavy_check_mark:](Execution.md#etudiant-${id}) | "
   KO="| ${i} | [${id}](../${FILE}) | [:x:](Execution.md#etudiant-${id})                | "
   if [ -f "$FILE" ]; then
       echo ${OK}
   else
       echo ${KO}
   fi
   let "i++"
done
