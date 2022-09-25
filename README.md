# DevSocial-Users-MS
Micro-service for handling user-oriented activities

### Directory Structure

```
├── LICENSE
├── README.md
└── app
    ├── api
    │   ├── __init__.py
    │   ├── auth
    │   │   └── __init__.py
    │   ├── endpoints
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   └── routers.py
    │   ├── handlers
    │   │   └── __init__.py
    │   └── utils
    │       └── __init__.py
    ├── ds-users-ms
    │   ├── __init__.py
    │   └── settings
    ├── main.py
    └── users
        ├── __init__.py
        ├── config.py
        ├── kafka
        └── utils
```

### System Design
V - 0.1

![DevSocialSystemDesign](https://user-images.githubusercontent.com/58564635/192140565-48a7a0b9-3b8f-4d8d-bd61-3f82169ad27a.png)
