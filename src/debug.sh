#!/bin/bash
#TODO: add variables and parameters
echo "Start of the debug script"

echo "Generation of the text file"
python utils/generate_text.py -n 1 -o resources/text.txt

echo "Encoding and formation of the signal"
python transmitter_script.py -i resources/text.txt -o resources/signal.txt -d

echo "Send text to server"
python channel_access/client.py --input_file=resources/signal.txt --output_file=resources/recv.txt --srv_hostname=iscsrv72.epfl.ch --srv_port=80

echo "Received signal"
cat resources/recv.txt
