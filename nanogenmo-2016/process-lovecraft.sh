#!/usr/bin/env zsh
givenNamesGrep=$(cat lovecraft-given-names.txt | tr '\n' '|' | sed 's/^/\\(/;s/|*$/\\)/;s/|/\\|/g')
surnamesGrep=$(cat lovecraft-surnames.txt | tr '\n' '|' | sed 's/^/\\(/;s/|*$/\\)/;s/|/\\|/g')
cultsGrep=$(cat lovecraft-cults.txt | tr '\n' '|' | sed 's/^/\\(/;s/|*$/\\)/;s/|/\\|/g')
textsGrep=$(cat lovecraft-texts.txt | tr '\n' '|' | sed 's/^/\\(/;s/|*$/\\)/;s/|/\\|/g')

echo "#include lovecraft-fixtures.gg"
echo "#import lovecraft-para-helper.py"
echo "output:=\$lovecraftParas"
cat lovecraft-full.txt | tr -d '\0'| tr '{}' '()' | sed 's/^$/\\n/g' | tr '\n' ' ' | sed 's/\\n/\n/g;s/   */ /g'| sed 's/^  *//;s/  *$//' | grep '\. .*\. .*\.$' | sed "s/$givenNamesGrep $surnamesGrep/{\$\$protagonistName}/g;s/$surnamesGrep/{\$\$protagonistLName}/g;s/$cultsGrep/{\$\$cult}/g;s/$textsGrep/{\$\$arcaneText}/g" | sed 's/,/\\,/g;s/"/\\"/g;s/\$\([0-9]\)/\1/g' | awk 'BEGIN{ORS=","} {if(!i) { print "\nlovecraftPara" (++j) ":=" ; i=100 }; print $0; i-- } END { print "\nlovecraftPara:=" ; while(j) { print "$lovecraftPara" j ; j-- ;} print "\n"}' | sed 's/=,/=/;s/,$//'

