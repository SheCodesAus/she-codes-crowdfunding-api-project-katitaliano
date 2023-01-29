# {{ Bored by Taxes (aka ADHaiD) }}
​
{{ Target audience: Adults with ADHD who are need in financial or material assistance due to the impacts of “ADHD Tax”

ADHD tax is best understood as “the price you pay for costly mistakes due to symptoms of ADHD” (Avery 2019). The obvious examples are late fees, forgotten and spoiled groceries, impulsive purchases and similar consequences of the poor memory, executive function, and impulse control known in ADHD. It is also understood as the hidden costs that are not measured in dollars, but “measured in wasted time, physical well-being, mental health, personal freedom (vs. incarceration), and — yes — years on your life.” (Avery 2019)

This crowdfunding platform will focus on the most important needs of persons with ADHD that have large upfront costs, and that are related to quality and longevity of life. Things that that they may struggle to afford due to the accumulated effects of every day “ADHD tax” on their finances or large and unexpected “ADHD tax” expenses. It may also be to access services/support that may help prevent future “ADHD tax”.
}}
​
## Features
{{ ​Create user accounts with username, email, password as required fields. Users are able post their own projects and pledge to other’s projects. Ability to change password. }}

## Future additional features

{{ An annual limit on projects to deter abuse (attempted this feature but not completed).  Ability to update and/or delete projects and pledges. Ability to like and respond to comments. Ability to report projects that are inappropriate. Ability to filter projects by owner. Ability to add categories and/or tags and filter by these. }}

### User Accounts
​
- [X] Username
- [X] Email Address
- [X] Password
​
### Project
​
- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [ ] Destroy
- Pledge
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [ ] Destroy
​
### Implement suitable permissions
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Limit who can create
  - [ ] Limit who can retrieve
  - [X] Limit who can update
  - [ ] Limit who can delete
- Pledge
  - [X] Limit who can create
  - [ ] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete
- Pledge
  - [ ] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete
​
### Implement relevant status codes
​
- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404
​
### Handle failed requests gracefully 
​
- [ ] 404 response returns JSON rather than text
​
### Use token authentication
​
- [X] impliment /api-token-auth/
​
​
### External libraries used
​
- [ ] django-filter
​
​
## Part A Submission
​
- [ ] A link to the deployed project. https://wild-meadow-5490.fly.dev/projects/
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint- SEE GITHUB
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint. SEE GITHUB
- [ ] A screenshot of Insomnia, demonstrating a token being returned. SEE GITHUB
- [ ] Your refined API specification and Database Schema. SEE GITHUB
​
### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://localhost:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username":	"Test2."
	,
	"email":
		"test2@test.com"
,
	"password": 
		"not-real-password"	
}
```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://localhost:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "admin",
	"password": "not-real-password"
}
'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://localhost:8000/projects/ \
  --header 'Authorization: Token fe8568a49428ac40341e0689e72c870ddac64492' \
  --header 'Content-Type: application/json' \
  --data '{
        "title": "Donate a rabbit",
        "description": "Please help, we need a cat for she codes plus, our class lacks hops.",
        "target": 1,
        "image": "https://www.readersdigest.ca/wp-content/uploads/2020/04/GettyImages-694542042-e1586274805503.jpg",
        "is_open": true,
        "date_created": "2023-01-29T14:53:44.238Z",
        "owner": 1
    }
    ```