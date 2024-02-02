wget https://github.com/XrayR-project/XrayR/releases/download/v0.9.1/XrayR-linux-64.zip
unzip XrayR-linux-64.zip  -d xrayr
cd xrayr/

nohup ./XrayR -config config.yml > 1.log 2>&1 &