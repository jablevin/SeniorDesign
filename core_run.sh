core=$'smr_7x7'
processors=37
runmpact $core $processors | tee logfile
line=$(head -n 1 logfile)
file=${line:48:72}'/'$core'.out'
location=${line:48:72}'/'

echo $location

python run_checker.py <<EOF
$file
EOF

#Change location to your needs
copy_location=$'/share/casl/jablevin/core_runs/core1/'

cp $location$core'.out' $copy_location
cp $location$core'.log' $copy_location
cp $location$core'.h5' $copy_location
