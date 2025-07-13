class InviteRewardsCommand:
    def __init__(self, db):
        self.db = db

    async def claim_reward(self, user_id):
        rewards = self.db.get_user_rewards(user_id)
        if rewards > 0:
            self.db.update_user_rewards(user_id, -1)  # Decrease reward count
            await self.send_reward(user_id)
            return True
        return False

    async def send_reward(self, user_id):
        # Logic to send the reward to the user
        pass

    async def add_invite(self, inviter_id, invitee_id):
        self.db.add_invite(inviter_id, invitee_id)