#!/bin/sh

# --------------------------------------
#
#
#
# --------------------------------------

. ../.scripts/students.sh --source-only

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

