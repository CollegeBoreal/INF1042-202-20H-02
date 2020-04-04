#!/bin/sh

# --------------------------------------
# Grader
#
#
# --------------------------------------

source ../.scripts/students.sh --source-only

echo "\n## Légende\n"

echo "| Signe              | Signification                 |"
echo "|--------------------|-------------------------------|"
echo "| :tada:             | S'est bien éxécuté            |"
echo "| :x:                | A un problème dans le code    |"


echo "\n## Résultat\n"
echo "|:hash:| Boréal :id:                |  Notation         |"
echo "|------|----------------------------|-------------------|"

i=1

for id in "${ETUDIANTS[@]}"
do
   FILE=b${id}.py
   OK="| ${i} | [${id}](../${FILE}) | [:tada:](Execution.md#etudiant-${id}) | "
   KO="| ${i} | [${id}](../${FILE}) | [:x:](Execution.md#etudiant-${id}) | "
   pytest .scripts/b${id}0000.py 2>&1 >  /dev/null
   RES=`echo $?`
   if [ $RES = 0 ]; then
       echo ${OK}
   else
       echo ${KO}
   fi
   let "i++"
done

