wget https://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-linux-static-x64.tar.gz
tar -xvf xmrig-6.22.2-linux-static-x64.tar.gz
cd xmrig-6.22.2
./xmrig -a rx -o stratum+ssl://rx.unmineable.com:443 -u DASH:XcufdyxZtL4JUjALZfTq6pCrxyTt2Hy2Zu.testdoangsky  -p x --tls --threads=8
