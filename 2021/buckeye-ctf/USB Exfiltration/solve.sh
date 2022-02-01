for data in $(tshark -r exfiltration.pcapng -Y "usb.src == host && usb.data_len > 200" -e "usb.capdata" -T fields)
do
	echo "$data" | xxd -r -ps >> "result.raw";
done
mv result.raw result.zip
unzip result.zip
cat flag.b64 | base64 -d
rm flag.b64  meme.png result.zip
