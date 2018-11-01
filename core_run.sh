core=$'smr_7x7'
processors=37
copy_location=$'/share/casl/jablevin/SeniorDesign/core_runs/core2/'

runmpact $core $processors | tee logfile
line=$(head -n 1 logfile)
file=${line:48:72}'/'$core'.out'
location=${line:48:72}'/'

echo $location
echo $copy_location

python run_checker.py <<EOF
$file
$location
$copy_location
EOF


cp $location$core'.out' $copy_location
cp $location$core'.log' $copy_location
cp $location$core'.h5' $copy_location

for i in $(seq 1 $END); do
	cp $location'deck.37.'$i'.dnb.out' $copy_location
done
