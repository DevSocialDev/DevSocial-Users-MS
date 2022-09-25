from fastapi import HTTPException, Request


class UserUserInteractionHandler:
    def __init__(self, request: Request) -> None:
        self.request = request

    async def follow_user(self, username: str, username_to_follow: str):
        user_to_follow = await self.request.app.mongodb["users"].find_one(
            {"username": username_to_follow}
        )
        user = await self.request.app.mongodb["users"].find_one({"username": username})
        self.request.app.mongodb["users"].update_one(
            {"username": username}, {"$push": {"following": user_to_follow["_id"]}}
        )
        self.request.app.mongodb["users"].update_one(
            {"username": username_to_follow}, {"$push": {"followers": user["_id"]}}
        )

        # count of number of following for current user
        count = len(user["following"]) + 1
        myquery = {"username": username}
        newvalues = {"$set": {"following_count": count}}
        self.request.app.mongodb["users"].update_one(myquery, newvalues)

        # count of number of followers for user which was followed
        count_u = len(user_to_follow["followers"]) + 1
        myquery_u = {"username": username_to_follow}
        newvalues_u = {"$set": {"followers_count": count_u}}
        self.request.app.mongodb["users"].update_one(myquery_u, newvalues_u)

        # self.request.app.mongodb["users"].update_one({"username":username},{'following_count' :count })
        if len(user_to_follow) == 0:
            raise HTTPException(
                status_code=404, detail=f"Username : {username_to_follow} not found"
            )
        return {"message": f"{username_to_follow} followed"}

    async def unfollow_user(
        self, username: str, username_to_unfollow: str, request: Request
    ):
        user_to_unfollow = await self.request.app.mongodb["users"].find_one(
            {"username": username_to_unfollow}
        )
        user = await self.request.app.mongodb["users"].find_one({"username": username})
        self.request.app.mongodb["users"].update_one(
            {"username": username}, {"$pull": {"following": user_to_unfollow["_id"]}}
        )
        self.request.app.mongodb["users"].update_one(
            {"username": username_to_unfollow}, {"$pull": {"followers": user["_id"]}}
        )

        # count of number of following for current user
        count = len(user["following"]) - 1
        myquery = {"username": username}
        newvalues = {"$set": {"following_count": count}}
        self.request.app.mongodb["users"].update_one(myquery, newvalues)

        # count of number of followers for user which was unfollowed
        count_u = len(user_to_unfollow["followers"]) - 1
        myquery_u = {"username": username_to_unfollow}
        newvalues_u = {"$set": {"followers_count": count_u}}
        self.request.app.mongodb["users"].update_one(myquery_u, newvalues_u)

        if len(user_to_unfollow) == 0:
            raise HTTPException(
                status_code=404, detail=f"Username : {username_to_unfollow} not found"
            )
        return {"message": f"{user_to_unfollow} unfollowed"}


class UserInteractionHandler:
    def __init__(self) -> None:
        pass
