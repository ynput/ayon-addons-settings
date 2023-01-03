from __future__ import annotations
import os
from typing import Any
from nxtools import logging

from openpype.addons import BaseServerAddon

from .settings.main import SlackSettings, DEFAULT_SLACK_SETTING
from .version import __version__


class Slack(BaseServerAddon):
    name = "slack"
    version = __version__

    settings_model = SlackSettings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_SLACK_SETTING)

    def get_local_client_info(
            self,
            base_url: str | None = None,
    ) -> dict[str, Any] | None:
        """Returns information on local copy of the client code."""
        logging.info("private:: {}".format(self.get_private_dir()))
        if (pdir := self.get_private_dir()) is None:
            return None
        if base_url is None:
            base_url = ""
        client_zip = "{}_{}.zip".format(self.name, self.version)
        logging.info("client_zip:: {}".format(client_zip))
        local_path = os.path.join(pdir, client_zip)
        logging.info("local_path:: {}".format(local_path))
        if not os.path.exists(local_path):
            return None
        return {
            "type": "http",
            "path": f"{base_url}/addons/{self.name}/{self.version}/private/{client_zip}",  # noqa
        }
