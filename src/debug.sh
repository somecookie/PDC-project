#!/bin/bash
#TODO: add variables and parameters
echo "Start of the debug script"

echo "Generation of the text file"

python utils/generate_text.py -n 160 -o resources/sent.txt

echo "Text generated"

echo "Send text to server"

python channel_access/client.py --input_file=resources/sent.txt --output_file=resources/recv.txt --srv_hostname=iscsrv72.epfl.ch --srv_port=80

echo "Received text from server"

diff --brief <(sort resources/sent.txt) <(sort resources/recv.txt) >/dev/null
comp_value=$?

if [ $comp_value -eq 1 ]
then
    echo "Not equal"
else
    echo "Equal"
fi
