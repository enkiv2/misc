total=$(ls part?/Page*.htm | wc -l)
count=0
for i in part?/Page*.htm; do 
	count=$((count+1))
	pct=$((count*100/total))
	echo; echo -e "Linking $i (${pct}%)...\c"
	sed -i 's/Page Title/MiniatureBinoculars.com/g' $i ; printf .

	#echo;  echo "German origins ($i)..."

	sed -i 's|GERMAN ORIGINS #1|<a href="/part1/Page304.htm">GERMAN ORIGINS #1</a>|g' $i ; printf .
	sed -i 's|GERMAN ORIGINS #2|<a href="/part1/Page577.htm">GERMAN ORIGINS #2</a>|g' $i ; printf .
	sed -i 's|GERMAN ORIGINS #3|<a href="/part1/Page823.htm">GERMAN ORIGINS #3</a>|g' $i ; printf .
	sed -i 's|GERMAN ORIGINS #4|<a href="/part1/Page1008.htm">GERMAN ORIGINS #4</a>|g' $i ; printf .
	sed -i 's|GERMAN ORIGINS #5|<a href="/part1/Page1187.htm">GERMAN ORIGINS #5</a>|g' $i ; printf .
	sed -i 's|GERMAN ORIGINS #6|<a href="/part1/Page5797.htm">GERMAN ORIGINS #6</a>|g' $i ; printf .

	#echo;  echo "Japanese origins ($i)..."

	sed -i 's|JAPANESE ORIGINS #1|<a href="/part1/Page1353.htm">JAPANESE ORIGINS #1</a>|g' $i ; printf .
	sed -i 's|JAPANESE ORIGINS #2|<a href="/part1/Page1581.htm">JAPANESE ORIGINS #2</a>|g' $i ; printf .
	sed -i 's|JAPANESE ORIGINS #3|<a href="/part1/Page1781.htm">JAPANESE ORIGINS #3</a>|g' $i ; printf .
	sed -i 's|JAPANESE ORIGINS #4|<a href="/part1/Page1930.htm">JAPANESE ORIGINS #4</a>|g' $i ; printf .
	sed -i 's|JAPANESE ORIGINS #5|<a href="/part1/Page2265.htm">JAPANESE ORIGINS #5</a>|g' $i ; printf .
	sed -i 's|JAPANESE ORIGINS #6|<a href="/part1/Page2445.htm">JAPANESE ORIGINS #6</a>|g' $i ; printf .
	sed -i 's|JAPANESE ORIGINS #7|<a href="/part1/Page15683.htm">JAPANESE ORIGINS #7</a>|g' $i ; printf .

	#echo;  echo "Introduction ($i)..."

	sed -i 's|INTRODUCTION #2|<a href="/part1/Page3007.htm">INTRODUCTION #2</a>|g' $i ; printf .
	sed -i 's|INTRODUCTION #1|<a href="/part1/Page2725.htm">INTRODUCTION #1</a>|g' $i ; printf .

	#echo;  echo "Distribution ($i)..."

	sed -i 's|DISTRIBUTION #1|<a href="/part1/Page3204.htm">DISTRIBUTION #1</a>|g' $i ; printf .
	sed -i 's|DISTRIBUTION #2|<a href="/part1/Page3232.htm">DISTRIBUTION #2</a>|g' $i ; printf .
	sed -i 's|DISTRIBUTION #3|<a href="/part1/Page3503.htm">DISTRIBUTION #3</a>|g' $i ; printf .
	sed -i 's|DISTRIBUTION #4|<a href="/part1/Page3779.htm">DISTRIBUTION #4</a>|g' $i ; printf .
	sed -i 's|DISTRIBUTION #5|<a href="/part1/Page4071.htm">DISTRIBUTION #5</a>|g' $i ; printf .
	sed -i 's|DISTRIBUTION #6|<a href="/part1/Page4342.htm">DISTRIBUTION #6</a>|g' $i ; printf .
	sed -i 's|DISTRIBUTION #7|<a href="/part1/Page4616.htm">DISTRIBUTION #7</a>|g' $i ; printf .
	sed -i 's|DISTRIBUTION #8|<a href="/part1/Page4842.htm">DISTRIBUTION #8</a>|g' $i ; printf .
	sed -i 's|DISTRIBUTION #9|<a href="/part1/Page16559.htm">DISTRIBUTION #9</a>|g' $i ; printf .

	#echo;  echo "Fun analyzing brands ($i)..."

	sed -i 's|FUN ANALYZING BRANDS #1|<a href="/part1/Page5077.htm">FUN ANALYZING BRANDS #1</a>|g' $i ; printf .
	sed -i 's|FUN ANALYZING BRANDS #2|<a href="/part1/Page5528.htm">FUN ANALYZING BRANDS #2</a>|g' $i ; printf .
	sed -i 's|FUN ANALYZING BRANDS #3|<a href="/part1/Page5747.htm">FUN ANALYZING BRANDS #3</a>|g' $i ; printf .
	sed -i 's|FUN ANALYZING BRANDS #4|<a href="/part1/Page6009.htm">FUN ANALYZING BRANDS #4</a>|g' $i ; printf .

	#echo;  echo "Binoculars by brand ($i)..."

	sed -i 's|BINOCULARS BY BRAND A-B|<a href="/part1/Page6170.htm">BINOCULARS BY BRAND A-B</a>|g' $i ; printf .
	sed -i 's|BINOCULARS BY BRAND C-G|<a href="/part1/Page6218.htm">BINOCULARS BY BRAND C-G</a>|g' $i ; printf .
	sed -i 's|BINOCULARS BY BRAND H-M|<a href="/part1/Page6259.htm">BINOCULARS BY BRAND H-M</a>|g' $i ; printf .
	sed -i 's|BINOCULARS BY BRAND N-Q|<a href="/part1/Page6309.htm">BINOCULARS BY BRAND N-Q</a>|g' $i ; printf .
	sed -i 's|BINOCULARS BY BRAND R-S|<a href="/part1/Page6358.htm">BINOCULARS BY BRAND R-S</a>|g' $i ; printf .
	sed -i 's|BINOCULARS BY BRAND T-Z|<a href="/part1/Page6394.htm">BINOCULARS BY BRAND T-Z</a>|g' $i ; printf .

	#echo;  echo "Photo gallery ($i)..."

	sed -i 's|PHOTO GALLERY #10|<a href="/part2/Page14785.htm">PHOTO GALLERY #<!--space-->10</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #11|<a href="/part2/Page21470.htm">PHOTO GALLERY #<!--space-->11</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #12|<a href="/part2/Page11207.htm">PHOTO GALLERY #<!--space-->12</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #1|<a href="/part2/Page6442.htm">PHOTO GALLERY #1</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #2|<a href="/part2/Page7322.htm">PHOTO GALLERY #2</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #3|<a href="/part2/Page8216.htm">PHOTO GALLERY #3</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #4|<a href="/part2/Page9165.htm">PHOTO GALLERY #4</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #5|<a href="/part2/Page10185.htm">PHOTO GALLERY #5</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #6|<a href="/part2/Page11139.htm">PHOTO GALLERY #6</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #7|<a href="/part2/Page12096.htm">PHOTO GALLERY #7</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #8|<a href="/part2/Page13028.htm">PHOTO GALLERY #8</a>|g' $i ; printf .
	sed -i 's|PHOTO GALLERY #9|<a href="/part2/Page13950.htm">PHOTO GALLERY #9</a>|g' $i ; printf .

	#echo;  echo "Vintage advertising ($i)..."

	sed -i 's|VINTAGE ADVERTISING #1|<a href="/part3/Page15446.htm">VINTAGE ADVERTISING #1</a>|g' $i ; printf .
	sed -i 's|VINTAGE ADVERTISING #2|<a href="/part3/Page15680.htm">VINTAGE ADVERTISING #2</a>|g' $i ; printf .
	sed -i 's|VINTAGE ADVERTISING #3|<a href="/part3/Page15934.htm">VINTAGE ADVERTISING #3</a>|g' $i ; printf .
	sed -i 's|VINTAGE ADVERTISING #4|<a href="/part3/Page16224.htm">VINTAGE ADVERTISING #4</a>|g' $i ; printf .
	sed -i 's|VINTAGE ADVERTISING #5|<a href="/part3/Page16535.htm">VINTAGE ADVERTISING #5</a>|g' $i ; printf .
	sed -i 's|VINTAGE ADVERTISING #6|<a href="/part3/Page16805.htm">VINTAGE ADVERTISING #6</a>|g' $i ; printf .
	sed -i 's|VINTAGE ADVERTISING #7|<a href="/part3/Page17055.htm">VINTAGE ADVERTISING #7</a>|g' $i ; printf .
	sed -i 's|VINTAGE ADVERTISING #8|<a href="/part3/Page17284.htm">VINTAGE ADVERTISING #8</a>|g' $i ; printf .

	#echo;  echo "Original boxes ($i)..."

	sed -i 's|ORIGINAL BOXES #1|<a href="/part3/Page17550.htm">ORIGINAL BOXES #1</a>|g' $i ; printf .
	sed -i 's|ORIGINAL BOXES #2|<a href="/part3/Page17848.htm">ORIGINAL BOXES #2</a>|g' $i ; printf .

	#echo;  echo "Repair ($i)..."

	sed -i 's|CAN YOU REPAIR THESE\?|<a href="/part3/Page18076.htm">CAN YOU REPAIR THESE?</a>|g' $i ; printf .
	sed -i 's|REPAIR SEIZED OCULARS IF|<a href="/part3/Page18378.htm">REPAIR SEIZED OCULARS IF</a>|g' $i ; printf .
	sed -i 's|COLLIMATE AND REPAIR CF|<a href="/part3/Page18719.htm">COLLIMATE AND REPAIR CF</a>|g' $i ; printf .

	#echo;  echo "More repairs ($i)..."

	sed -i 's|MORE REPAIRS #1|<a href="/part3/Page19097.htm">MORE REPAIRS #1</a>|g' $i ; printf .
	sed -i 's|MORE REPAIRS #2|<a href="/part3/Page19423.htm">MORE REPAIRS #2</a>|g' $i ; printf .
	sed -i 's|MORE REPAIRS #3|<a href="/part3/Page19776.htm">MORE REPAIRS #3</a>|g' $i ; printf .

	#echo;  echo "Identify ($i)..."

	sed -i 's|IDENTIFY THIS|<a href="/part3/Page19988.htm">IDENTIFY THIS</a>|g' $i ; printf .

	#echo;  echo "Misc ($i)..."

	sed -i 's|SWAP SHOP|<a href="/part3/Page20420.htm">SWAP SHOP</a>|g' $i ; printf .
	sed -i 's|MISC #1|<a href="/part3/Page20799.htm">MISC #1</a>|g' $i ; printf .
	sed -i 's|MISC #2|<a href="/part3/Page21116.htm">MISC #2</a>|g' $i ; printf .
	sed -i 's|BIG &amp\; SMALL #1|<a href="/part4/Page3708.htm">BIG \&amp\; SMALL #1</a>|g' $i ; printf .
	sed -i 's|BIG &amp\; SMALL #2|<a href="/part4/Page3802.htm">BIG \&amp\; SMALL #2</a>|g' $i ; printf .
	sed -i 's|BIG &amp\; SMALL #3|<a href="/part4/Page3552.htm">BIG \&amp\; SMALL #3</a>|g' $i ; printf .
	sed -i 's|BIG &amp\; SMALL #4|<a href="/part4/Page6190.htm">BIG \&amp\; SMALL #4</a>|g' $i ; printf .
	sed -i 's|BIG &amp\; SMALL #5|<a href="/part4/Page994.htm">BIG \&amp\; SMALL #5</a>|g' $i ; printf .
	sed -i 's|BIG &amp\; SMALL #6|<a href="/part4/Page1585.htm">BIG \&amp\; SMALL #6</a>|g' $i ; printf .
	sed -i 's|INDEX #1|<a href="/part6/Page21283.htm">INDEX #1</a>|g' $i ; printf .
	sed -i 's|INDEX #2|<a href="/part6/Page493.htm">INDEX #2</a>|g' $i ; printf .
	sed -i 's|OTHER BINOCULARS #10|<a href="/part5/Page290.htm">OTHER BINOCULARS #10</a>|g' $i ; printf .
	sed -i 's|OTHER BINOCULARS #1\([^0]\)|<a href="/part5/Page21222.htm">OTHER BINOCULARS #1</a>\1|g' $i ; printf .
	sed -i 's|OTHER BINOCULARS #2|<a href="/part5/Page2762.htm">OTHER BINOCULARS #2</a>|g' $i ; printf .
	sed -i 's|OTHER BINOCULARS #3|<a href="/part5/Page3047.htm">OTHER BINOCULARS #3</a>|g' $i ; printf .
	sed -i 's|OTHER BINOCULARS #4|<a href="/part5/Page3260.htm">OTHER BINOCULARS #4</a>|g' $i ; printf .
	sed -i 's|OTHER BINOCULARS #5|<a href="/part5/Page3540.htm">OTHER BINOCULARS #5</a>|g' $i ; printf .
	sed -i 's|OTHER BINOCULARS #6|<a href="/part5/Page3595.htm">OTHER BINOCULARS #6</a>|g' $i ; printf .
	sed -i 's|OTHER BINOCULARS #7|<a href="/part5/Page4610.htm">OTHER BINOCULARS #7</a>|g' $i ; printf .
	sed -i 's|OTHER BINOCULARS #8|<a href="/part5/Page3090.htm">OTHER BINOCULARS #8</a>|g' $i ; printf .
	sed -i 's|OTHER BINOCULARS #9|<a href="/part5/Page4508.htm">OTHER BINOCULARS #9</a>|g' $i ; printf .
	sed -i 's|BINOCULARS CATALOGS #10|<a href="/part6/Page1464.htm">BINOCULAR CATALOGS #10</a>|g' $i ; printf .
	sed -i 's|BINOCULARS CATALOGS #1\([^0]\)|<a href="/part6/Page21320.htm">BINOCULAR CATALOGS #01</a>\1|g' $i ; printf .
	sed -i 's|BINOCULARS CATALOGS #2|<a href="/part6/Page22377.htm">BINOCULAR CATALOGS #02</a>|g' $i ; printf .
	sed -i 's|BINOCULARS CATALOGS #3|<a href="/part6/Page4115.htm">BINOCULAR CATALOGS #03</a>|g' $i ; printf .
	sed -i 's|BINOCULARS CATALOGS #4|<a href="/part6/Page1604.htm">BINOCULAR CATALOGS #04</a>|g' $i ; printf .
	sed -i 's|BINOCULARS CATALOGS #5|<a href="/part6/Page13012.htm">BINOCULAR CATALOGS #05</a>|g' $i ; printf .
	sed -i 's|BINOCULARS CATALOGS #6|<a href="/part6/Page2379.htm">BINOCULAR CATALOGS #06</a>|g' $i ; printf .
	sed -i 's|BINOCULARS CATALOGS #7|<a href="/part6/Page21529.htm">BINOCULAR CATALOGS #07</a>|g' $i ; printf .
	sed -i 's|BINOCULARS CATALOGS #8|<a href="/part6/Page21697.htm">BINOCULAR CATALOGS #08</a>|g' $i ; printf .
	sed -i 's|BINOCULARS CATALOGS #9|<a href="/part6/Page1013.htm">BINOCULAR CATALOGS #09</a>|g' $i ; printf .
	sed -i 's|DATA BINOCULARS BRANDS|<a href="/part6/Page21739.htm">DATA BINOCULARS BRANDS</a>|g' $i ; printf .

	#echo;  echo "Logos ($i)..."

	sed -i 's|JB JE MFGR. CODE LIST|<a href="/part6/Page289.htm">JB JE MFGR. CODE LIST</a>|g' $i ; printf .
	sed -i 's|TRADEMARKED LOGOS|<a href="/part6/Page538.htm">TRADEMARKED LOGOS</a>|g' $i ; printf .

	# echo;  echo "Reformatting PDF buttons..."
	cat $i | tr '\r' '\n' | tr '\n' ' ' | sed 's/>/>\n/g' |  
		sed 's/\(<img\)/\n\1/g' |  sed 's/\(<img\)\([^>]*alt="[^"]*I WANT TO SEE[^>]*\)/\1 id="nav" \2/g' |
		tr '\n' '\r' | sed 's/\(<img\)\([^>]*HERE[^>]*>\)/<a href\=\"#nav\">\1\2<\/a>/g' | tr '\r' '\n' > foo; mv foo $i; 
	sed -i 's|</style>|a:link { color=#0000CC\;}\na { color=#0000CC\;}\n</style>|g' $i
	sed -i 's/TO VIEW/TO VIEW /g' $i
	printf .

	#echo; echo "Linking PDFs ($i) (${pct}%)..."
	printf ' '
	for j in "1052LASZLO.PDF" "1897MONTGOMERYWARD.PDF" "1903GOERZ.PDF" "1905ARMSTRONG.PDF" "1906VOIGTLANDER.PDF" "1908GOERZ.PDF" "1911SEARSCATALOG.PDF" "1913ZEISSFLYER.PDF" "1922MANUFRANCE.PDF" "1923ZEISS.PDF" "1924PACIFIC.PDF" "1925ZEISS2.PDF" "1925ZEISSB.PDF" "1925ZEISS.PDF" "1925ZEISSVP.PDF" "1927ZEISSCATALOG.PDF" "1928EZEISS.PDF" "1928ZEISSCATALOGUE.PDF" "1928ZEISSGEMELOS.PDF" "1928ZEISSG..PDF" "1928ZEISSG.PDF" "1928ZEISSINC.PDF" "1928ZEISSi.PDF" "1928ZEISSPRICES.PDF" "1929ZEISS.PDF" "1930BL.PDF" "1930GALEFCATALOGUE.PDF" "1930ZEISS.PDF" "1931ZEISS.PDF" "1932ZEISS.PDF" "1934BAUSCH.PDF" "1934DUMAURIERCATALOGUE.PDF" "1934MANUFRANCE.PDF" "1934OPPLEMAN.PDF" "1935BAUSCHANDLOMB.PDF" "1935LEITZ.PDF" "1936LEITZ.PDF" "1936ZEISS.PDF" "1937BAUSCH1.PDF" "1937BAUSCH2.PDF" "1937HENSOLDT.PDF" "1937HUDSON.PDF" "1937HUSON.PDF" "1937ZEISSFLYER.PDF" "1937ZEISSINC.PDF" "1938OPPELMANCATALOG.PDF" "1938OPPELMANCATALOGUE.PDF" "1938OPPLEMANCATALOGUE.PDF" "1938SELSI.PDF" "1938ZEISS.PDF" "1938ZEISSUK.PDF" "1939HENSOLDT.PDF" "1939LASZLO.PDF" "1939LEITZCATALOG.PDF" "1940BAUSCH.PDF" "1940BECKEN.PDF" "1947MONTGOMERYWARD.PDF" "1947WARD.PDF" "1948BAUSCHANDLOMB.PDF" "1948BAUSCH.PDF" "1948BROWNSCOPE3.PDF" "1949BROWNSCOPE1.PDF" "1949BROWNSCOPE.PDF" "1950GALEFCATALOGUE.PDF" "1950MONTGOMERYWARDCATALOGUE.PDF" "1950STOEGERCATALOGUE.PDF" "1950UNITEDFLYER.PDF" "1950ZEISSFLYER.PDF" "1951BARRANDSTROUD.PDF" "1951BAUSCHANDLOMB.PDF" "1951MANUFRANCECATALOG.PDF" "1951MANUFRANCE.PDF" "1951MIKRONFLYERS.PDF" "1951OCEAN.PDF" "1952BL.PDF" "1952BUSHNELLDEALERFLYER.PDF" "1952DAVECOOKFLYER.PDF" "1952FAREASTERNFLYER.PDF" "1952LASZLO.PDF" "1952MONTGOMERYWARDCATALOGUE.PDF" "1952SCOPECATALOGUE.PDF" "1952UNITED.PDF" "1952ZEISS.PDF" "1953KERSHAWFLYER.PDF" "1953LEEROBERTCATALOGUE.PDF" "1953ROSSFLYERBAKER.PDF" "1953ROSSFLYERHEB.PDF" "1953UNITEDCATALOGUEA.PDF" "1953UNITEDCATALOGUEB.PDF" "1953ZEISS.PDF" "1954CRITERION.PDF" "1954LAFAYETTECATALOG.PDF" "1954LASZLOCATALOGUE.PDF" "1954LEITZFLYER.PDF" "1954THALSON.PDF" "1954WRAYBOOKLET.PDF" "1955BUSHNELL.PDF" "1955LAFAYETTECATALOG.PDF" "1955THALSONCATALOGUE.PDF" "1955UNITEDCATALOGUE.PDF" "1956ALCAN.PDF" "1956BAUSCHANDLOMB.PDF" "1956BUSHNELLMAILER.PDF" "1956CADILLACOPTICALCATALOGUE.PDF" "1956CARRCAMERACATALOGUE.PDF" "1956CONCORDRADIO.PDF" "1956DENHILL.PDF" "1956DOLLANDS.PDF" "1956HENSOLDT.PDF" "1956JADAVIS.PDF" "1956LAFAYETTECATALOG.PDF" "1956LEITZ.PDF" "1956PEERLESSCATALOGUE.PDF" "1956PEERLESSSCATALOGUE.PDF" "1956SWIFTANDANDERSON.PDF" "1956UNITEDCATALOGUE.PDF" "1956WHOLESALE.PDF" "1957LAFAYETTECATALOG.PDF" "1957UNITEDCATALOGUE.PDF" "1957ZEISSCATALOGUE.PDF" "1957ZEISS.PDF" "1958ALCANCATALOGUE.PDF" "1958LEITZ.PDF" "1958SEARS.PDF" "1958WARDSCATALOGUE.PDF" "1958ZEISSCATALOGUE.PDF" "1959CENTRAL.PDF" "1959DAVISCATALOGUE.PDF" "1959WARD.PDF" "1959ZEISSKATALOG.PDF" "1959ZEISS.PDF" "1960CENTRAL.PDF" "1960CHARLESFRANK.PDF" "1960HENSOLDT.PDF" "1960UNITED.PDF" "1960WARD.PDF" "1960WHOLESALE.PDF" "1960ZEISSCATALOGUE.PDF" "1960ZEISS.PDF" "1961CARLZEISSJENA.PDF" "1961CENTRALCAMERACATALOGUE.PDF" "1961HENSOLDPRICES.PDF" "1961MUTSUMIDOHONTEN.PDF" "1961PARKERCATALOGUE.PDF" "1961TRYON.PDF" "1961ZEISSPRICES.PDF" "1961ZEISSRETAILPRICES.PDF" "1962COLONIALCATALOGUE.PDF" "1962DOLLONDSCATALOG.PDF" "1962DOLLONDS.PDF" "1962HENSOLDT.PDF" "1962HERTELREUSS.PDF" "1962HERTERSCATALOGUE.PDF" "1962MATSUSHIMACATALOG.PDF" "1962ROSSCATALOG.PDF" "1962ZEISS.PDF" "1963ASAHIUKFLYER.PDF" "1963BUSHNELLFLYER.PDF" "1963KLEINSCATALOGUE.PDF" "1963UNITEDCATALOGUE.PDF" "1963UTS2.PDF" "1963WARD.PDF" "1963ZEISSDEALER.PDF" "1964ASAHIOPTICALCATALOGUE.PDF" "1964CURRY.PDF" "1964GANDER.PDF" "1964JAPANESECAMERAS.PDF" "1964MATSUSHIMA2.PDF" "1964ZEISSCATALOG.PDF" "1965ACTINACATALOGUE.PDF" "1965BUSHNELL.PDF" "1965KUNKELS.PDF" "1965LAFAYETTECATALOG.PDF" "1965NIKONBOOKLET.PDF" "1965 SWIFTFLYER.PDF" "1965SWIFTFLYER.PDF" "1966BERNSCATALOGUE.PDF" "1966BINOLUXCATALOGUE.PDF" "1966HEDLER.PDF" "1966JAEGERSCATALOGUE.PDF" "1966LASZLOCATALOGUE.PDF" "1966UNITEDCATALOGUE.PDF" "1967BUSHNELL.PDF" "1967GREENCATCATALOGUE.PDF" "1967GREENKATCATALOGUE.PDF" "1967HEROCATALOGUE.PDF" "1968BUSHNELLCATALOG.PDF" "1968COMPASSMAILER.PDF" "1968HERTERS.PDF" "1968TASCOFLYER.PDF" "1969LEITZCATALOGUE.PDF" "1969ZEISS.PDF" "1970ASHREHCATALOGUE.PDF" "1972HERTERSCATALOGUE.PDF" "1972SOUTHERN.PDF" "1973BUSHNELL.PDF" "1974EDMUND.PDF" "1975COLONIAL.PDF" "1976BUSHNELL.PDF" "1976COMPASSCATALOGUE.PDF" "1976TASCOCATALOGUE.PDF" "1977LEITZCATALOG.PDF" "1979ASAHI.PDF" "1979FUJINON.PDF" "1980LEICA.PDF" "1982PENTAX.PDF" "1983SWIFTFLYER.PDF" "1983SWIFT.PDF" "1984PENTAXCATALOGUE.PDF" "1988AUSJENA.PDF" "2000NIKON.PDF" "AGFACATALOGUE.PDF" "ALOE.PDF" "ASAHIENGLISHCATALOGUE.PDF" "ASAHIITALIANCATALOGUE.PDF" "ASAHIOPTICALCOCATALOGUE.PDF" "ASAHIUKFLYER.PDF" "BARKER.PDF" "BECKKASSEL1.PDF" "BECKKASSEL2.PDF" "BECK.PDF" "BROWNSCOPE2.PDF" "BROWNSCOPE.PDF" "BUSCHFR.PDF" "CADILLAC.PDF" "CHARLESFRANKCATALOGUE.PDF" "DAVISHOW.PDF" "DAVIS.PDF" "DENHILLCATALOGUE.PDF" "FRANZRAPSCH.PDF" "FUJIKOSHI.PDF" "GALLOWAYS.PDF" "GENEVA.PDF" "GOPHER.PDF" "GUNDLACHOPTICAL.PDF" "HARTMANN.PDF" "HEADQUARTER.PDF" "HENSOLDT.PDF" "HENSOLDTPRICES.PDF" "HENSOLDTPRICESUNDATED.PDF" "HENSOLDTSCOPES.PDF" "HEROLA.PDF" "HUET.PDF" "HURRICANE.PDF" "JDAVIS.PDF" "KALIMARCATALOGUE.PDF" "KNIRPS.PDF" "KOWAFLYER.PDF" "MANONFLYERONE.PDF" "MANONFLYER.PDF" "MANONFLYERTWO.PDF" "MARCUS.PDF" "MATSUSHIMACATALOGUE.PDF" "MILLER.PDF" "MINOXBDSHEET.PDF" "NEWBOLDANDBULFORD.PDF" "NIKON.PDF" "NIPPONKOGAKU.PDF" "ODUBER.PDF" "OTAKECATALOGUE.PDF" "PENTAXUK.PDF" "PHOTOBINDER.PDF" "PINI.PDF" "RALEIGHCATALOGUE.PDF" "RODENSTOCK.PDF" "S&A2.PDF" "S&AHOWTO.PDF" "SAHOWTO.PDF" "SCHUTZ.PDF" "SPERBER.PDF" "SPINDLERHOYER.PDF" "STEINHEIL.PDF" "STELLAR.PDF" "SUKIYA.PDF" "SWIFTANDANDERSON.PDF" "TAYLOROPTICAL.PDF" "TM9.PDF" "UNITEDCATALOG.PDF" "UTSCATALOG2.PDF" "UTSCATALOGUE.PDF" "WOLLENSAK.PDF" "WRAYFLYER.PDF" "YASHICA.PDF" "YORKCATALOGUE.PDF" "ZEISSINC.PDF" "ZEISSJANA.PDF" "ZEISSPRICES.PDF" 
do 
		cat $i | sed 's/$/\\n/g' | tr '\n' ' ' |  sed 's/ VIEW\([^ ]\)/ VIEW \1/g;s/ CATALOGUE\.PDF/CATALOGUE.PDF/g' | sed 's|\(<img[^>]*alt="[^"]*'"$j"'[^>]*>\)|<a href="/'"$j"'.pdf">\1</a>|' | sed 's/\\n/\n/g' > foo ; mv foo $i
		sed -i 's|<a href="\.PDF\.pdf">\(.*\)</a>$|\1|' $i
		printf . 
	done; echo
done ; echo


