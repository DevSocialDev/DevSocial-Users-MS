from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from api.endpoints.models import User, Login, UpdateUserModel
from api.handlers.UserHandler import (
    UserLoginHandler,
    UserLogoutHandler,
    UserSignupHandler,
)
from api.handlers.UsersInteractionHandler import (
    UserUserInteractionHandler,
    UserInteractionHandler,
)

# router object for handling api routes
router = APIRouter()

# get user data {user_id},{username} -> user profile page
@router.get("/{username}/details", response_description="Show all details about a user")
async def list_user(username: str, request: Request):
    user_details = UserInteractionHandler(request).list_user(username)
    return user_details


# get all users
@router.get("/users/all", response_description="List all users")
async def list_all(request: Request):
    all_users = UserInteractionHandler(request).list_all()
    return all_users


# login
@router.post("/login")
async def login(request: Request, user_to_login: Login = Body(...)):
    login_user = UserLoginHandler(request).login_user(user_to_login)
    return login_user


# logout
@router.post("/logout", response_description="Logout of the app")
async def logout(username: str, request: Request):
    logout_user = UserLogoutHandler(request).logout_user(username)
    return logout_user


# signup
@router.post("/signup", response_description="Signup for a new user")
async def create_user(request: Request, user: User = Body(...)):
    signup_user = UserSignupHandler(request).add_user_to_db(user)


# follow a user
@router.post(
    "/{username}/follow/{username_to_follow}", response_description="Follow a user"
)
async def follow_user(username: str, username_to_follow: str, request: Request):
    follow_user = UserUserInteractionHandler(request).follow_user(
        username, username_to_follow
    )
    return follow_user


# unfollow a user
@router.post(
    "/{username}/unfollow/{username_to_unfollow}",
    response_description="unfollow a user",
)
async def unfollow_user(username: str, username_to_unfollow: str, request: Request):
    unfollow_user


# delete user
@router.delete("/{id}/delete", response_description="Delete user account")
async def delete_user(request: Request, id: str):
    pass


# Current active users :
@router.get("/users/active", response_description="Show all active users")
async def active_users(request: Request):
    pass


# Edit user profile
@router.put("/update/{id}", response_description="Update user profile")
async def update_user(id: str, request: Request, user: UpdateUserModel = Body(...)):
    pass
