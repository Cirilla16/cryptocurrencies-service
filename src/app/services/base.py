class BaseService(object):

    auth_data: dict = {}
    user_id: str = 'qqq'

    dao = None
    schema = None
    model = None

    def __init__(self, userId: str = 0, auth_data: dict = {}):
        """Service初始化."""

        self.user_id = userId
        self.auth_data = auth_data