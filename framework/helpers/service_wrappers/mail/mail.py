import json

from framework.internal.clients.http.mail_api.apis.mail_api import MailApi
from framework.internal.clients.http.mail_api.models.api_models import Messages


class MailApiClient(MailApi):
    def search_messages(
        self, query: str, limit: int = 10, start: int = 0, kind: str = "containing"
    ) -> Messages:
        return self.get_mail_search(limit=limit, kind=kind, query=query, start=start)

    def search_confirmation_token(self, email: str) -> str | None:
        mails = self.search_messages(query=email, kind="containing", limit=1)
        if len(mails.items) == 0:
            return None

        body = mails.items[0].content.body
        try:
            json_body = json.loads(body)
        except json.JSONDecodeError:
            return None

        if activation_link := json_body.get("ConfirmationLinkUrl"):
            token = activation_link.split("/")[-1]
            return token

        return None
