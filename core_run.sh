runmpact 2a 1 | tee logfile
line=$(head -n 1 logfile)
filename=${line:48:72}'/2a.out'

echo $filename

python run_checker.py <<EOF
$filename
EOF
