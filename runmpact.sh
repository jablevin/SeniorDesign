# ssh -tt jablevin@login.hpc.ncsu.edu << EOF
#     cd /share/casl/jablevin
#     bash script.sh
#     exit
# EOF
runtime=20
python Texting.py <<EOF
$runtime
EOF
