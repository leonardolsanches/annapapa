import base64

base64_message = 'UEsDBBQACAgIAM1s7VIAAAAAAAAAAAAAAAAHAAAAYXNzZXRzL1VUCQADUeApZ1HgKVl1eAsAAQT1AQAABBQAAAAFAAAAAAAAUEsDBBQACAgIAM1s7VIAAAAAAAAAAAAAAAAOAAAAYXNzZXRzL2ltZy9VVAkAA1HgKVlR4ClZdXgLAAEE9QEAAAQUAAAAIAAAAAAAAFBLAwQUAAgICADN
bOy1UgAAAAAAAAAAAAAAADYAAABhc3NldHMvaW1nL2ZvdG8tYW5uYS1wYXBhLnBuZ1VUCQADVeApZ1XgKVl1eAsAAQT1AQAABBQAAABgAAAAAAAAVVBLAwQUAAgICADNbOy1UgAAAAAAAAAAAAAAAGQAAABhc3NldHMvaW1nL2ljb25lLXRlY25vbG9naWEtbGlkZXJhbmNh
LnBuZ1VUCQADV+ApZ1fgKVl1eAsAAQT1AQAABBQAAAC4AAAAAAAAVVBLAwQUAAgICADNbOy1UgAAAAAAAAAAAAAAAGgAAABhc3NldHMvaW1nL2ZpZ3VyYS1lbmNvbnRyby1lcXVpcGUtMDEucG5nVVQJAANY4ClnW+ApWXV4CwABBPUBAAAEFAAAALAAAAAAAABVUEsDBBQACAgIAM1s
7VIAAAAAAAAAAAAAAABoAAAAYXNzZXRzL2ltZy9maWd1cmEtZW5jb250cm8tZXF1aXBlLTAyLnBuZ1VUCQADW+ApZ1vgKVl1eAsAAQT1AQAABBQAAADkAAAAAAAAVVBLAwQUAAgICADNbOy1UgAAAAAAAAAAAAAAAGgAAABhc3NldHMvaW1nL2ZpZ3VyYS1ub3ZhLnBuZ1VUCQADY+ApZ2Pg
KVl1eAsAAQT1AQAABBQAAACwAAAAAAAAVVBLAwQUAAgICADNbOy1UgAAAAAAAAAAAAAAADgAAABtYW5pZmVzdC5qc29uVVQJAAPZ4Cln2eApWXV4CwABBPUBAAAEFAAAACwAAAAAAABVUEsDBBQACAgIAM1s7VIAAAAAAAAAAAAAAAAwAAAAb3Blbi1ncmFwaC5tZXRh
VVQJAANf4ClnX+ApWXV4CwABBPUBAAAEFAAAAGwAAAAAAABVUEsDBBQACAgIAM1s7VIAAAAAAAAAAAAAAAAALAAAAHJlYWRtZS5tZFVUCQADZ+ApZ2fgKVl1eAsAAQT1AQAABBQAAAC8AAAAAAAAVVBLAwQUAAgICADNbOy1UgAAAAAAAAAAAAAAACwAAABzdHlsZS5jc3NVVAkAA2fgKWdn4ClZdXgLAAEE9QEAAAQUAAAA
wAAAAAAAAAAAAAAALAAAAHJlYWRtZS5tZFVUCQADZ+ApZ2fgKVl1eAsAAQT1AQAABBQAAAC8AAAAAAAAVVBLVVBLBQYAAAAAAQABADYAAABnAAAAAAA='
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)
