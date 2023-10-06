org_str = {
    "company_name": "ABC limited",
    "departments": {
        "HR": {
            "employees": {
                "101": {
                        "name": "Rubel",
                        "position": "HR Head",
                        "salay": 60000,
                },
                "102": {
                        "name": "Bob",
                        "position": "Junior HR",
                        "salay": 25000,
                }
            },
        },
        "IT":{
            "employees":{
                "201": {
                    "name": "Rohan",
                    "position": "Seniour IT Manager",
                    "salary": 100000
                },
                "202": {
                    "name": "Jojo",
                    "position": "Jounier IT Devloper",
                    "salary": 30000
                }
            }
        }
        
    }
}



# Find Jojo Salary

print(org_str["departments"]["IT"]["employees"]["202"]["salary"])
