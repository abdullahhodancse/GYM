🏋️ Gym Management System





📍 PROJECT OVERVIEW

━━━━━━━━━━━━━━━━━━━━━━━

A backend-only REST API built using Django and Django REST Framework for managing gym operations across multiple branches with secure role-based access.






🎯 BUSINESS GOAL

━━━━━━━━━━━━━━━━━━━━━━━

The system is designed to solve the following problems:

• Centralized gym branch management
• Role-based access control
• Structured workout planning
• Secure member activity tracking
• Branch-level data isolation






🧩 KEY FEATURES

━━━━━━━━━━━━━━━━━━━━━━━

✔ Multi-branch gym management
✔ Role-Based Access Control (RBAC)
✔ Workout plan creation & assignment
✔ Member progress tracking
✔ Backend-only scalable architecture





🛠 TECHNOLOGY STACK

━━━━━━━━━━━━━━━━━━━━━━━

Layer	Technology


Backend	Django, Django REST Framework


Database	PostgreSQL


Security	RBAC


Deployment	Render


API Testing	Postman


Rate limit for login 1 min 5 login request






⚙️ LOCAL DEVELOPMENT SETUP

━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Repository Setup

Clone the repository   from https://github.com/abdullahhodancse/GYM

Step 2: Virtual Environment

Create and activate a Python virtual environment.

Step 3: Dependencies

Install all required dependencies from the requirements file.

Step 4: Environment Configuration

Create a .env file and configure database credentials and secret keys.

Step 5: Database Initialization

Run migrations to create all database tables.

Step 6: Admin Access

Create a Django superuser to access the admin panel.

Step 7: Run Server

Start the development server. You need to uncomment the settings line  130 to 139 umber line

Local Base URL:
http://127.0.0.1:8000/


You have to add it in.env,,,it given beacude just for testing


POSTGRES_DB=GYM


POSTGRES_USER=postgres


POSTGRES_PASSWORD=1234


DB_HOST=localhost


DB_PORT=5432



Admin_pass=GYM@1234567890


PROJECT_PASS_KEY=django-insecure-x_+2#dqo4zv-b3ju6a$d)rcv0uf!2ow(ok9xfmo^!2f8%3+$qo










🌐 APPLICATION ACCESS

━━━━━━━━━━━━━━━━━━━━━━━


🔐 Django Admin Panel

URL: {base_url}/admin/

Email: admin@gmail.com

Password: 1234








🌍 Live Deployment

Hosted API Base URL:
https://gym-51v6.onrender.com



user_regisration:https://gym-51v6.onrender.com/accounts/reg/

LogIn:https://gym-51v6.onrender.com/accounts/login/

profile:https://gym-51v6.onrender.com/accounts/profile/

Profile_update:https://gym-51v6.onrender.com/accounts/profile/update/

admin_reg:https://gym-51v6.onrender.com/accounts/admin/register/

Make_Manager:https://gym-51v6.onrender.com/accounts/make_manager/

manager_list:https://gym-51v6.onrender.com/accounts/managers/list/

member_list_for_admin:https://gym-51v6.onrender.com/accounts/branch_members/


branch_create:http://gym-51v6.onrender.com/branches/create/

branch_list:https://gym-51v6.onrender.com/branches/list/

branch_update:https://gym-51v6.onrender.com/branches/update/<int:Id>/

make_trainer:https://gym-51v6.onrender.com/accounts/make_trainer/

trainer_list:https://gym-51v6.onrender.com/accounts/trainers_list/

member_list_for_manager:https://gym-51v6.onrender.com/accounts/branch_members

assign_member_branch:https://gym-51v6.onrender.com/accounts/assign_member/

work_out_plan:https://gym-51v6.onrender.com/trainer/workout_plan/create/

status_update_by_trainer:https://gym-51v6.onrender.com/workout/own_status_update/<int:Id>/

work_out_list:https://gym-51v6.onrender.com/workout/workout-plans/list/

assing_plan_to_member:https://gym-51v6.onrender.com/workout/assign_plan_member/

work_out_task:https://gym-51v6.onrender.com/trainer/workout_task/create/

Status_update_by_member:https://gym-51v6.onrender.com/workout/own_status_update/<int:Id>/


Own_plan_list:https://gym-51v6.onrender.com/workout/own_plan_list/










👥 ROLE-BASED ACCESS CONTROL (RBAC)

━━━━━━━━━━━━━━━━━━━━━━━






🔑 SUPER ADMIN

───────────────────────

Access Level: System-wide

Responsibilities
• Manage all gym branches
• Create & manage Managers
• Full control over all users
• System-level configurations







🧑‍💼 MANAGER

───────────────────────

Access Level: Branch-specific

Responsibilities
• Manage assigned branch
• Create Trainers & Members
• Assign Trainers to Members
• View branch-level reports

Restrictions
• Cannot access other branches
• Cannot manage Super Admin data







🏋️‍♂️ TRAINER

───────────────────────

Access Level: Branch-specific

Responsibilities
• Create workout plans
• Assign plans to Members
• Update workout tasks
• Track Member progress

Restrictions
• No access to other branches
• No system-level permissions







🧍 MEMBER


───────────────────────

Access Level: Individual

Responsibilities
• View assigned workout plans
• Update workout status
– Pending
– In Progress
– Completed
• View personal profile

Restrictions
• No admin or management access
• Cannot view other Members’ data






List of API Endpoint:
───────────────────────

user_regisration:http://127.0.0.1:8000/accounts/reg/

LogIn:http://127.0.0.1:8000/accounts/login/

profile:http://127.0.0.1:8000/accounts/profile/

Profile_update: http://127.0.0.1:8000/accounts/profile/update/

admin_reg:http://127.0.0.1:8000/accounts/admin/register/

Make_Manager:http://127.0.0.1:8000/accounts/make_manager/

manager_list:http://127.0.0.1:8000/accounts/managers/list/

member_list_for_admin:http://127.0.0.1:8000/accounts/branch_members/


branch_create:http://127.0.0.1:8000/branches/create/

branch_list:http://127.0.0.1:8000/branches/list/

branch_update:127.0.0.1:8000/branches/update/<int:Id>/

make_trainer:http://127.0.0.1:8000/accounts/make_trainer/

trainer_list:http://127.0.0.1:8000/accounts/trainers_list/

member_list_for_manager:http://127.0.0.1:8000/accounts/branch_members

assign_member_branch:http://127.0.0.1:8000/accounts/assign_member/

work_out_plan:http://127.0.0.1:8000/workout/trainer/workout_plan/create/

status_update_by_trainer: http://127.0.0.1:8000/workout/own_status_update/<int:Id>/

work_out_list:http://127.0.0.1:8000/workout/workout-plans/list/

assing_plan_to_member:http://127.0.0.1:8000/workout/assign_plan_member/

work_out_task:http://127.0.0.1:8000/workout/trainer/workout_task/create/

Status_update_by_member:http://127.0.0.1:8000/workout/own_status_update/<int:Id>/


Own_plan_list:http://127.0.0.1:8000/workout/own_plan_list/







How to use the Postman collection

───────────────────────

1.Import Collection into Postman



2.Authentication (JWT)  means after registration then login by email and password then you will get access_token

3.Authorization Header (Auto).....Authorization: Bearer {{access_token}}





Pre-created Test Users :

Admin:{
  "email": "admi11@gym.com",
  "password": "Hodan@1234567890",
  "password2": "Hodan@1234567890",
  "secret_key":"GYM@1234567890"
  "role":"admin"
  
}


trainer:{
    "email": "member1@gym.com",
    "password": "Hodan@1234567890"
    "branch_name": "Dhaka12332 Branch(id:5)"
    "role":"trainer"
}


member:{
    "email": "member2@gym.com",
    "password": "Hodan@1234567890"
    "branch_name": "Dhaka12332 Branch(id:5)"
    "role":"member"
    
}

manager:{
    "email": "manager@gym.com",
    "password": "Hodan@1234567890"
    "branch_name": "Dhaka12332 Branch(id:5)"
    "role":"manager"
}









































