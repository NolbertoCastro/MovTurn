#! /usr/bin/bash
declare files=( "testlex1.txt" "testlex2.txt" "testlex3.txt" "testlex4.txt" )
declare results=( "No error" "Error" "Error" "No error" )

for ((i = 1; i<=4; i++)); do
	var=$(../compiler/robot ./"${files[i]}" 2>&1)
	if [[ "$var" =~ "syntax error" ]]; then
		declare out="Error"
	else
	declare out="No error"
	fi
	if [[ "$out" =~ "${results[i]}" ]]; then
		echo "test  $i passed"
	else
		echo "test $i failed"
	fi
done
