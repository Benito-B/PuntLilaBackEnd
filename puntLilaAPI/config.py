import os
SERVER_IP = "0.0.0.0"
SERVER_PORT = 5000
token="eyJhbGciOiJSUzI1NiIsImtpZCI6IjIwMTEwOTFkYTAzYmFhNDA5MTllNmZmODM2YzhlN2Y5YWZhYmE5YTgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiNzg3NTA1NjIwMDE0LTFha2dvbXZ1bGI5OHFyY245NmNtMGVyM3M0ams2a3M1LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiNzg3NTA1NjIwMDE0LTFha2dvbXZ1bGI5OHFyY245NmNtMGVyM3M0ams2a3M1LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTA3OTA0MjE2NzU0NTYwNDg0NTk3IiwiaGQiOiJhbHUuaWVzc2VycGlzLm9yZyIsImVtYWlsIjoiYWFycGVpQGFsdS5pZXNzZXJwaXMub3JnIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJiTGxtYTNWaURMLVZuc3VVd3pnaFZnIiwibmFtZSI6IkFBUk9OIFBBTE1FUiBQRUlSTyIsInBpY3R1cmUiOiJodHRwczovL2xoNC5nb29nbGV1c2VyY29udGVudC5jb20vLVQxcnlZeDZ3Z1dnL0FBQUFBQUFBQUFJL0FBQUFBQUFBQUFBL0FDSGkzcmVhLVNwQmM1OUpjNDdlazVaV3J2ZmFVZ2pLTVEvczk2LWMvcGhvdG8uanBnIiwiZ2l2ZW5fbmFtZSI6IkFBUk9OIiwiZmFtaWx5X25hbWUiOiJQQUxNRVIgUEVJUk8iLCJsb2NhbGUiOiJlcyIsImlhdCI6MTU3NjUxMTEyOCwiZXhwIjoxNTc2NTE0NzI4LCJqdGkiOiIzNmQ4MjVkNDIxMzMwYzI2ZjIwNTQ2ODJmMzk2ODUxYTlhMjZhOWFjIn0.t-eO5ccIYvSr4rfvX8MvBKz9Sxq5Vi1mRI_SBZFBwyvsvd2ZGD24Z8mK5J44zDA84HlbZ8k43w5cxPNzMWY4hnC0CMqN3ptIjRIG92Y0LVTvcbTqcLrw4HRfXs_IbkuyK9uIM4ug0PQXh18RHIwE1cV5HA5j6IW8gNzrCnEObBeJanMkbJe4Rzb_AkcnrEd6s1cvPCuM42jaTVAOmkIUxa-psjClaenAQd7uJAYyUFF-1XPhLMaJoNiT_Dd3xwKxA4hTsFR4J1dINaY71hTh67lWOzHkcLdEF_2IEJUXdEbwVT7hUKQ3bSPlvs5g9H38Msf3e8JNSOub-PUm9mY0hA"
id="787505620014-1akgomvulb98qrcn96cm0er3s4jk6ks5.apps.googleusercontent.com"
firebase_config = {
    "apiKey": os.getenv('FIREBASE_API_KEY'),
    "authDomain": "puntlilaserpis-9a9ed.firebaseapp.com",
    "databaseURL": "https://puntlilaserpis-9a9ed.firebaseio.com",
    "projectId": "puntlilaserpis-9a9ed",
    "storageBucket": "puntlilaserpis-9a9ed.appspot.com",
    "serviceAccount": "puntLilaAPI/firebase-private-key.json",
    "messagingSenderId": "274165429499"
}