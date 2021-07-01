# configure

```json
{
    "pages":[
        {
            "Page_name": "Welcome Page",
            "Title": "Hi",
            "Description": "This page is used for Welcome new users",
            "Emojis" : ["U0001F44D", "U0001F44E"],
            "Color": "blue",
            "Url": "https://discord.com/channels/741527808400031854/849631605660057630/849631816557133874",
            "Extra_fields":[]

        },
        {
            "Page_name": "Degree Page",
            "Title": "Degree",
            "Description": "Please select your degree .....",
            "emojis" : ["U0001F44D", "U0001F44E"],
            "Color": "blue",
            "Url": "https://discord.com/channels/741527808400031854/849631605660057630/849631816557133874",
            "Extra_fields":[
                {"field_name": "Master",
                 "field_content": "I'm a master ....",
                 "field_url":"https://discord.com/channels/741527808400031854/849631605660057630/849631816557133874"
                }
            ]

        }
    ]
    
}
```



# DB schema

## User Table

| Field Name | Is required? | Is key? | Description |
| ---------- | ------------ | ------- | ----------- |
| User ID | Yes | Yes |  |
| User Name | Yes | Yes |  |

Key : User ID/User Name

Optional: Institution abbr/Program Degree/Program Name/Program Start Year/Program End Year/LinkedIn/Create Dt/Last Update Time/Last Update User/User Leave Server Dt

## School Table

Key:ID/縮寫

Optional: School Name/ Region
